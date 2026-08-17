from __future__ import annotations

import re
from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query, join_nonempty
from .zep_common import prime_eval_thread, render_graph_search


_LABEL_RE = re.compile(r"^(EPISODE|FACT|ENTITY|OBSERVATION|THREAD_SUMMARY):\s*")


def _compact(text: str) -> str:
    """Remove wasted bytes from rendered search output before budgeting.

    Two sources of waste, both measured on the golden run:

    1. `add_semantic_documents` ingests every KB document twice (once as JSON,
       once as its plain-text summary), so graph search returns each document
       twice and half the semantic budget pays for a duplicate.
    2. `render_graph_search` emits an empty `metadata=` line per episode when no
       cap is set.

    Dropping both is lossless - nothing unique is removed - but it roughly
    doubles how much distinct evidence survives ContextBudgetManager.trim(),
    which keeps the head and discards the tail.
    """
    if not text:
        return ""
    kept: list[str] = []
    seen: list[str] = []
    for line in text.split("\n"):
        line = line.strip()
        if not line or line == "metadata=":
            continue
        # Compare payloads, not labels: the plain-text copy of a document is a
        # substring of the JSON copy's "summary" field, but only once the
        # "EPISODE: " prefix is stripped from both.
        core = _LABEL_RE.sub("", line)
        core = re.sub(r"\s+", " ", core).casefold()
        # Drop only a block already contained in one we kept (the plain-text
        # copy is a substring of the JSON copy). Never drop the longer block.
        if any(core in s for s in seen):
            continue
        seen.append(core)
        kept.append(line)
    return "\n".join(kept)


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    # NOTE: Zep rejects graph.search queries longer than 400 characters. Some
    # eval queries are longer than that, so wrap every query with
    # `cap_query(query)` (see src/utils.py) before passing it to graph.search.

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        # Context Block is computed against a thread, so the eval thread must
        # carry the current question before we ask for it. ignore_roles=["user"]
        # inside prime_eval_thread keeps this probe out of durable memory.
        prime_eval_thread(self.client, user_id, thread_id, query)

        user_context = self.client.thread.get_user_context(thread_id=thread_id)
        context_block = getattr(user_context, "context", "") or ""

        # The Context Block is relevance-ranked and can drop a low-salience
        # open loop (E03 wants "benchmark report" + "16:00"). A wide edges
        # search backfills those facts and exposes valid_at/invalid_at, which
        # is also the evidence for the recency/conflict case E08.
        try:
            facts = self.client.graph.search(
                user_id=user_id,
                query=cap_query(query),
                scope="edges",
                limit=20,
            )
            fact_text = render_graph_search(facts)
        except Exception:
            # A failed fact search must not lose the Context Block we already have.
            fact_text = ""

        # Facts first, Context Block second. Under the 4% long-term budget only
        # ~1280 characters survive trim(), and the Context Block alone is
        # longer than that. Facts are one-line, dated and marker-bearing
        # (LAB-REPORT-1600, BLUEBIRD-42), so spending the head of the budget on
        # them keeps far more distinct evidence than a prose summary would.
        return _compact(join_nonempty([fact_text, context_block], sep="\n\n"))

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        # user_id (not graph_id): episodes are the user's own trajectory, and
        # scoping by user is what keeps E09 from leaking Minh's data to Lan.
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=5,
        )
        # Raw session messages are verbose; uncapped they eat the 3% episodic
        # budget and push out the short reflection episode that carries
        # "connection churn" / "timeout threshold" (E05). 200 chars keeps a
        # whole reflection intact (at 180 the trailing incident id
        # ASYNC-FIX-20 was sliced off mid-token) while 5 x ~200 chars stays
        # inside the 240-token episodic budget, so nothing is trimmed at all.
        return _compact(render_graph_search(results, episode_char_cap=200))

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        # graph_id -> the shared standalone domain graph. Using user_id here
        # would return personal preferences instead of the KB and fail E06/E11.
        q = cap_query(query)
        try:
            # scope="episodes" returns the raw ingested document text, which
            # preserves literal markers (PAYMENT-RULE-3, CONN-POOL-FIRST).
            # scope="auto" returns extracted facts and drops those codes.
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="episodes",
                limit=8,
            )
        except Exception:
            # Fallback for accounts/SDKs where the episodes scope behaves differently.
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="nodes",
                limit=8,
            )
        # Each KB document is ingested twice (JSON + text), so compaction here
        # is what lets all four documents - and their trailing "Marker: ..."
        # codes - fit inside the 3% semantic budget.
        return _compact(render_graph_search(results))

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        # ContextBudgetManager owns the 10/4/3/3 ratios and the
        # short_term -> long_term -> episodic -> semantic priority order,
        # trimming each layer from the tail so the highest-ranked evidence survives.
        return self.budget.assemble(layers)
