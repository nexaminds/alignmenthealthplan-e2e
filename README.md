# alignmenthealthplan-e2e

Black-box Playwright E2E suite for `https://www.alignmenthealthplan.com`, authored and executed by **NexAI SDET** via the `nexai-playwright-suite-run` skill.

We do not have source access to the target. This repo holds only the tests, driven against the live site from the outside.

## Read-only against production — not optional

The target is a third party's **production** healthcare site. Automated writes there create real records against real members.

- Default posture is **read-only**: navigate, snapshot, assert rendered content, check client-side validation.
- No form submissions, account creation, contact requests, or anything that writes.
- A test that must write carries `@pytest.mark.writes` and is **skipped** unless `E2E_ALLOW_WRITES=1`. Only set that against an environment we own.
- Never use real or realistic personal data. Never commit a screenshot showing member, patient, or account data.
- A flow that cannot be tested without writing is a `NOT RUN - requires a non-production environment` row in the report, not a live submission.

## Running

```bash
pip install -r requirements.txt
playwright install --with-deps chromium

export E2E_BASE_URL=https://www.alignmenthealthplan.com
pytest tests/e2e -v \
  --junit-xml=playwright-run.xml \
  --html=reports/e2e-report.html --self-contained-html \
  --screenshot=only-on-failure --output=reports/artifacts
```

`E2E_BASE_URL` has **no default**. An unset value fails loudly — a silent fallback makes a green run meaningless.

Exit codes worth reading: `0` all passed · `1` failures · `5` **no tests collected**. Exit 5 is a blocked run, not a pass.

## The HTML report

`--html=reports/e2e-report.html --self-contained-html` produces one file: sortable and filterable by outcome, a collapsible detail panel per case, and — because pytest-playwright's `--screenshot=only-on-failure` is wired in — a screenshot embedded (base64, no external files) on every failing case. It opens straight from disk in any browser, no server involved.

It is **not committed to git** — it's regenerated every run and would only rot in history otherwise. It ships as the `playwright-run` CI build artifact (see below) alongside the JUnit XML.

## CI

`.github/workflows/e2e.yml` runs the suite on a GitHub-hosted runner with open egress, which is the reliable path when the agent sandbox cannot reach `cdn.playwright.dev` to install browsers.

Set the repo variable `E2E_BASE_URL` (Settings → Secrets and variables → Actions → Variables), or pass `base_url` when dispatching the workflow manually.

Every run uploads a `playwright-run` build artifact containing `playwright-run.xml` and `reports/` (the HTML report plus failure screenshots). Download it from the workflow run's **Summary** page → *Artifacts*, unzip, and open `e2e-report.html`. **The JUnit XML inside it is the source of truth for every reported result** — the HTML report is a rendering of the same data, not a second source.

## Conventions

- Test names map 1:1 to case matrix IDs: `E2E-01` → `test_e2e_01_<behavior>`.
- One behavior per test. No inter-test ordering dependencies.
- Paths resolve relative to the repo; no dev-machine absolute paths anywhere.
- Run output (`playwright-run.xml`, `reports/`, `test-results/`) is gitignored. Tests are the durable artifact; run output is not.

## Reporting

Every run returns the delivery block from the SDET reporting contract:

```
Repository / Branch / Commit / PR
Verification: ran-and-passed | ran-with-failures | blocked-and-why
Cases: <total> total, <n> passed, <n> failed, <n> errored, <n> not run
Report: <playwright-run artifact URL from the CI run>
```

Counts must reconcile against the JUnit artifact, and a case absent from it is `NOT RUN` — never `PASS`.
