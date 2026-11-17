# RALPH LOOP Rule: Rate-Limit Resilience & Fallbacks

> **Mandate:** An autonomous agent must never panic or enter an infinite crash loop when an external API rate limit or transient network error occurs.

---

## Fallback Strategies

1. **Transient API Errors & Rate Limits (HTTP 429 / 503):**
   - Apply exponential backoff with jitter: wait 2s, 4s, 8s, up to 30s.
   - Do not hammer the endpoint.
   - If quota is exhausted on the primary provider, invoke fallback provider configured in `SERVICES/provider_manager.py`.

2. **Timeout Handling:**
   - Every external process or HTTP request must have an explicit timeout (default: 10s for API calls, 30s for test execution).
   - Never allow a blocking call without a timeout to freeze the engine.

3. **Disk Recovery Checkpoint:**
   - In case of unexpected session disconnect, simply re-read `progress.txt` upon restart to resume exactly where execution halted.

