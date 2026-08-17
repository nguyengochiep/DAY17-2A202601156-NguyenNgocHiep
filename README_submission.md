# README_submission - Lab 17 Multi-Memory Agent

**11/11 PASS, hit rate 100%** (`reports/benchmark.md`). Baseline no-memory: 2/11.

## 3 cau bat buoc

**Layer quan trong nhat: `long_term`.** Quyet dinh 4/11 case (E02, E03, E08, E09 = 20d) va cap `Python` cho E07. Cung la layer duy nhat bi test ca recency (E08) lan user isolation (E09).

**Trade-off Zep Context Block vs Redis + Qdrant.** Zep lo phan kho: trich xuat fact tu transcript, gan `valid_at`/`invalid_at` de xu ly conflict, xep hang relevance theo thread - E08 pass la nho co che nay. Doi lai: latency mang 1.3-3.4s/query (Redis ~0ms), phu thuoc vendor, it kiem soat - Context Block bo roi open loop do noi thap nen toi phai backfill bang `graph.search(scope="edges", limit=20)` cho E03. Redis + Qdrant nhanh va minh bach hon nhung phai tu viet extraction, versioning va conflict resolution.

**Guardrail chong memory poisoning.** `require_memory_consent` chan ghi khi chua opt-in; `minimize_pii` redact PII truoc ingest; `prime_eval_thread` dung `ignore_roles=["user"]` de cau probe khong lot vao durable memory; `heartbeat.py` read-only - background pass khong duoc tu cap quyen. Nen bo sung provenance bat buoc va human review truoc khi ghi de preference cu.

## 4 cau phan tich benchmark

1. **Hit rate thap nhat:** khong co - moi layer 100%. Baseline no-memory: `long_term`/`episodic`/`semantic` deu 0%, chi `short_term` 2/2 vi evidence con trong thread.
2. **Ton token nhat: E03 - 1407 token**, roi E08 (1398), E02 (1395). Ca ba deu `long_term` vi Context Block + 20 edges la payload nang nhat.
3. **E07 = `long_term` + `semantic`.** Evidence bat buoc: `Python` (user graph) va `Idempotency-Key` (standalone graph). Thieu mot la FAIL.
4. **Reduction 14.2% vs 81.8% (no-memory).** No-memory cao vi khong retrieve gi ca - reduction chi co nghia khi doc kem hit rate. 9/11 case reduction = 0 vi transcript nguon qua ngan (221 token) so voi Context Block. Chi 2 case semantic giam that (67.8%, 74.2%) va van PASS.

## E08 recency va E10 compaction

**E08:** fact "Python cho backend" bi **thu hep scope** chu khong bi xoa. Zep gan `invalid_at` cho fact cu, giu TypeScript/NestJS la current cho BLUEBIRD-42, nen ORCHID-27 van uu tien Python: recency **cong** scope, khong phai ghi de mu.

**E10:** sliding window evict raw turn, nhung `extract_durable_notes` giu constraint co marker (`REVIEW-DEADLINE-1600`, `Friday`, `16:00`) vao `DURABLE_NOTES`. Buffer khong du vi chi cat theo do dai.

Bang chung: `submission/long_term.png`, `episodic.png`, `semantic.png`, `privacy.png`.
