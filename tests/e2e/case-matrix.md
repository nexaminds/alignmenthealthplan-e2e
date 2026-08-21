# Case Matrix — alignmenthealthplan.com public pages

Target: `https://www.alignmenthealthplan.com` (public, unauthenticated, read-only)
Crawl bound: entry page + one level of primary navigation (homepage, Find Plans, Discover
Alignment, Contact Us). Subdomains (`providersearch.`, `members.`, `ava.`) and other apex
domains (`alignmenthealth.com`, `alignmenthealthcare.com`, `ahcusaweb.com`) are out of scope —
they sit behind gated/authenticated flows or are third-party-managed and are only checked at
the link level (E2E-13) to confirm they are correctly excluded from the crawl, never navigated
into.

No case submits a form, creates an account, or writes any record. `@pytest.mark.readonly` is
on every case; there are no `@pytest.mark.writes` cases in this suite.

| ID | Case name | Target URL | Assertion / success condition |
|---|---|---|---|
| E2E-01 | Homepage renders | `/` | HTTP status < 400 and document has a non-empty `<title>`. *(pre-existing seed case, `tests/e2e/test_smoke.py`)* |
| E2E-02 | Homepage hero heading renders | `/` | A heading containing "Medicare Advantage" is visible. |
| E2E-03 | Homepage primary navigation present | `/` | Top-level nav labels (Discover Alignment, Find Plans, Find Care, For Members, For Providers) and a "Contact Us" link are visible. |
| E2E-04 | Homepage plan-finder widget present | `/` | "Zip code" and "County" labels are visible, a "See Plans" link/button is visible, and at least one `<select>` control is present. |
| E2E-05 | Find a Plan page renders | `/find-a-plan` | HTTP status < 400 and `<title>` contains "Find a Plan". |
| E2E-06 | Find a Plan lead-capture form fields present | `/find-a-plan` | Field labels (First Name, Last Name, Email, Phone Number, U.S. ZIP Code) are visible and the page has ≥5 native `input`/`select` controls. No submit is clicked. |
| E2E-07 | Why Alignment Health Plan page renders | `/discover-ahp/why-alignment-health-plan` | HTTP status < 400 and a heading containing "Why Alignment Health Plan" is visible. |
| E2E-08 | Medicare Advantage guide page renders | `/discover-ahp/medicare-advantage-plans` | HTTP status < 400 and a heading containing "Medicare Advantage" is visible. |
| E2E-09 | Contact Us phone channels render | `/about-us/contact-us` | A "Contact Us" heading is visible and the page exposes ≥3 `tel:` links. |
| E2E-10 | Contact Us message audience links present | `/about-us/contact-us` | "Send Us a Message" text is visible and the four audience links (I am a Member / Provider / Broker, Other Inquiries) are visible. |
| E2E-11 | Footer legal links present and same-domain | `/` | Legal Notices, Privacy Notices, and Terms of Use links are visible and their `href`s point at `/about-us/...` paths on the target domain. |
| E2E-12 | "Shop Online" nav link targets Find a Plan | `/` → `/find-a-plan` | The "Shop Online" nav link's `href` contains `/find-a-plan`, and navigating there returns HTTP status < 400. |
| E2E-13 | Member/Provider login links stay out of crawl scope | `/` | "Member Login" and "Provider Login" links resolve to a host different from `www.alignmenthealthplan.com` (gated subdomains), confirming they are excluded from this suite rather than silently omitted. |

## Not covered by this suite

- Provider/doctor search (`providersearch.alignmenthealthplan.com`) — separate host, out of the
  stated crawl bound.
- Member/Provider/Agent portals — require authentication; explicitly excluded by the assignment.
- Any lead-capture or contact form **submission** — would write a real record against a
  production third-party system; only field *presence* is validated (E2E-04, E2E-06).
