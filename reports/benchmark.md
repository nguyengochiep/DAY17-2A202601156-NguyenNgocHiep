# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **11**
- Passed: **11/11**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **897.2 ms**
- Average token reduction vs full source context: **23.2%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E01 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| E06 | semantic | PASS | 1766.5 | 90 | 80.4% |  |
| E09 | long_term | PASS | 1553.4 | 674 | 0.0% |  |
| E10 | short_term | PASS | 0.4 | 195 | 0.0% |  |
| E02 | long_term | PASS | 1392.9 | 1264 | 0.0% |  |
| E03 | long_term | PASS | 1291.8 | 1327 | 0.0% |  |
| E04 | episodic | PASS | 259.2 | 153 | 30.8% |  |
| E05 | episodic | PASS | 237.1 | 144 | 34.8% |  |
| E07 | mixed | PASS | 1723.0 | 427 | 24.4% |  |
| E11 | semantic | PASS | 279.2 | 89 | 84.2% |  |
| E08 | long_term | PASS | 1365.8 | 1339 | 0.0% |  |

## Evidence excerpts

### E01 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### E06 - semantic

`EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"}`

### E09 - long_term

`FACT: Lan Tran's project is LOTUS-88. [valid_at=2026-08-01T11:00:00Z, invalid_at=None] FACT: Lab Assistant mentioned LOTUS-88. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: Lan Tran does not use Python in the backend. [valid_at=2026-08-01T11:00:00Z, invalid_at=None] FACT: Lab Assistant mentioned Java + Spring Boot for backend examples. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: Lan Tran prioritizes Spring Boot. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Lan Tran prioritizes Java. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] <USER_SUMMARY> The user's project is LOTUS-88, prioritizing Java and Spring Boot for backend examples`

### E10 - short_term

`<SESSION_SUMMARY> user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. | assistant: Acknowledged review constraint. | user: Filler turn 1 about UI spacing. | assistant: Filler answer 1. | user: Filler turn 2 about naming. | assistant: Filler answer 2. | user: Filler turn 3 about logging. | assistant: Filler answer 3. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. - assistant: Acknowledged review constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler turn 4 about tests. assistant: Filler answer 4. user: Filler turn 5 about docs. assistant: Filler answe`

### E02 - long_term

`FACT: Minh Nguyen does not like Java. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:00:20Z] FACT: Minh Nguyen likes Python. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:00:20Z] FACT: Minh Nguyen still prefers Python for personal demos like ORCHID-27. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: Minh Nguyen prefers Python for the personal demo project ORCHID-27. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: Minh Nguyen is currently learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen's personal project is ORCHID-27. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:00:20Z] FACT: The 'demo ca nhan ORCHID-27' p`

### E03 - long_term

`FACT: LAB-REPORT-1600 is an open loop for the benchmark report. [valid_at=2026-08-01T09:04:00Z, invalid_at=None] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen often confuses coroutines with Tasks. [valid_at=2026-08-01T09:02:00Z, invalid_at=2026-08-01T09:02:20Z] FACT: Minh Nguyen suggests reusing aiohttp ClientSession. [valid_at=2026-08-03T10:03:00Z, invalid_at=None] FACT: Minh Nguyen identifies connection churn as the main cause, not the timeout threshold. [valid_at=2026-08-03T10:03:00Z, invalid_at=None] FACT: Minh Nguyen is currently learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen reques`

### E04 - episodic

`EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn.`

### E05 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Voi demo ca nhan cua Minh, ngon ngu uu tien la gi?`

### E07 - mixed

`<LONG_TERM> FACT: When explaining code, Minh Nguyen wants the assistant to use short examples. [valid_at=2026-08-01T09:00:00Z, invalid_at=None] FACT: Minh Nguyen still prefers Python for personal demos like ORCHID-27. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: Minh Nguyen likes Python. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:00:20Z] FACT: Minh Nguyen prefers Python for the personal demo project ORCHID-27. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: Minh Nguyen does not like Java. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:00:20Z] FACT: Minh Nguyen suggests reusing aiohttp ClientSession. [valid_at=2026-08-03T10:03:00Z, invalid_at=None] FAC`

### E11 - semantic

`EPISODE: {"id":"kb-async-http","entity":"Async HTTP Incident Playbook","summary":"When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.","source":"incident-playbook-2026","updated_at":"2026-08-11T00:00:00Z"}`

### E08 - long_term

`FACT: For the BLUEBIRD-42 project, NestJS is required for the backend. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: For the BLUEBIRD-42 project, TypeScript is required for the backend. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: Python is not to be used for the backend of the BLUEBIRD-42 project. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: The Lab Assistant has the scope BLUEBIRD-42. [valid_at=2026-08-05T08:00:20Z, invalid_at=None] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: The 'demo ca nhan ORCHID-27' avoids Java. [valid_at=2026-08-01T09:00:20Z, invalid_at=None] FACT: The 'demo ca nhan ORCHID-27' prioriti`
