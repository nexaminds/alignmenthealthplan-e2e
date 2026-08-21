# Case Matrix — alignmenthealthplan.com public pages

Target: `https://www.alignmenthealthplan.com` (public, unauthenticated, read-only)

Crawl bound: homepage plus Discover Alignment, Find Plans, Find Care, Contact Us,
footer/legal pages, language toggle, text-size toggle, on-site search, two
responsive viewports, and basic accessibility landmarks. Subdomains
(`providersearch.`, `members.`, `ava.`, `agents.`) and other apex domains
(`alignmenthealth.com`, `alignmenthealthcare.com`, `ahcusaweb.com`) are out of
scope — they sit behind gated/authenticated flows or are third-party-managed and
are only checked at the link level (E2E-13, E2E-26, E2E-27) to confirm they
resolve to the expected host, never navigated into.

No case submits a form, creates an account, or writes any record.
`@pytest.mark.readonly` is on every case; there are no `@pytest.mark.writes`
cases in this suite.

## E2E-01..E2E-13 (PR #1 baseline)

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

## E2E-14..E2E-45 (this update)

| ID | Case name | Target URL | Assertion / success condition |
|---|---|---|---|
| E2E-14 | Ways to Enroll page renders | `/find-plans/ways-to-enroll` | HTTP status < 400, `<title>` contains "Ways to Enroll", and the sales `tel:1-888-293-8272` link is visible. |
| E2E-15 | Attend a Seminar page renders | `/find-plans/attend-a-seminar` | HTTP status < 400, `<title>` contains "Attend a Seminar" (case-insensitive), and heading text "Upcoming Seminars Near You" is visible (case-insensitive). |
| E2E-16 | Benefit Highlights page renders | `/find-plans/benefit-highlights` | HTTP status < 400, `<title>` contains "Benefit Highlights", and an H1 "Benefit Highlights" is visible. |
| E2E-17 | Pre-Enrollment Kit breadcrumb targets Ways to Enroll | `/find-plans/ways-to-enroll/pre-enrollment-kit` | HTTP status < 400, `<title>` contains "Pre-Enrollment Kit", and the breadcrumb link "Ways to Enroll" has an `href` containing `/find-plans/ways-to-enroll`. |
| E2E-18 | Group Retiree Options page renders | `/find-plans/group-retiree-options` | HTTP status < 400, `<title>` contains "Group Retiree Options" (case-insensitive), and heading text "HELPING YOU SERVE YOUR RETIREES" is visible (case-insensitive). |
| E2E-19 | Medicare Part D FAQs page renders | `/find-plans/part-d-faqs` | HTTP status < 400, `<title>` contains "Medicare Part D FAQs", and at least 10 "Q. ..." accordion question links are present. |
| E2E-20 | Visit Us page renders | `/find-plans/visit-us` | HTTP status < 400, `<title>` contains "Visit", and at least one "Get Directions" link is visible. |
| E2E-21 | Medicare Advantage FAQs (Discover Alignment) page renders | `/discover-ahp/medicare-advantage-frequently-asked-questions` | HTTP status < 400, `<title>` contains "Medicare Advantage FAQs", and at least 15 H2 article headings are present. |
| E2E-22 | Find a Drug page renders | `/find-care/find-a-drug` | HTTP status < 400, `<title>` contains "Find a Drug", and "Digital Drug Formulary" accordion trigger is visible. |
| E2E-23 | Find a Pharmacy page renders | `/find-care/find-a-pharmacy` | HTTP status < 400, `<title>` contains "Find a Pharmacy", and "Pharmacy Search" accordion trigger is visible. |
| E2E-24 | Find a Care Center page renders | `/find-care/find-a-care-center` | HTTP status < 400, `<title>` contains "Find a Care Center", and a "California" region heading is visible. |
| E2E-25 | Schedule Transportation page renders | `/find-care/schedule-transportation` | HTTP status < 400, `<title>` contains "Schedule Transportation", and heading "Make the Most of your Transportation Benefits" is visible. |
| E2E-26 | Find Care "Doctor" nav link targets provider search | `/` (no navigation) | The "Doctor" nav link's `href` host equals exactly `providersearch.alignmenthealthplan.com`. |
| E2E-27 | Find Care "Hospital" nav link targets provider search | `/` (no navigation) | The "Hospital" nav link's `href` host equals exactly `providersearch.alignmenthealthplan.com`. |
| E2E-28 | Privacy Notices page renders | `/about-us/privacy-notices` | HTTP status < 400, `<title>` contains "Privacy Notices", and an H1 "Privacy Notices" is visible. |
| E2E-29 | Terms of Use page lists sub-policies | `/about-us/terms-of-use` | HTTP status < 400, `<title>` contains "Terms of Use", and at least 4 "Read More" sub-policy links are visible. |
| E2E-30 | Nondiscrimination Policy page renders | `/about-us/terms-of-use/nondiscrimination-policy` | HTTP status < 400, `<title>` contains "Nondiscrimination Policy", and the `tel:1-844-297-5948` link is visible. |
| E2E-31 | Notice of Availability page renders | `/about-us/terms-of-use/notice-of-availability` | HTTP status < 400, `<title>` contains "Notice of Availability", and text "free interpreter services" is visible. |
| E2E-32 | Disaster Policy page renders | `/about-us/disaster-policy` | HTTP status < 400, `<title>` contains "Disaster Policy", and the disaster-support heading is visible. |
| E2E-33 | Language toggle switches nav to Spanish | `/` → click "Español" | The Spanish nav link "Contáctenos" becomes visible. |
| E2E-34 | Language toggle switches back to English | `/?lang=es-mx` → click "English" | The English nav link "Contact Us" becomes visible again. |
| E2E-35 | "Large" text size increases computed font-size | `/` → click "Large" | `getComputedStyle` font-size (px) of a reference paragraph is strictly greater after the click than before. |
| E2E-36 | On-site search for a common term returns results | `/` → search "Medicare" | "Site Search" heading is visible and "No results were found" text is absent. |
| E2E-37 | On-site search for a nonsense term shows no-results state | `/` → search a random unmatched string | "No results were found" text is visible. |
| E2E-38 | Mobile viewport shows the menu toggle | `/` @ 375×812 | The "Menu" toggle control is visible. |
| E2E-39 | Desktop viewport shows primary nav directly | `/` @ 1440×900 | "Discover Alignment" nav item is visible without interacting with any toggle. |
| E2E-40 | Homepage has exactly one H1 | `/` | Count of `<h1>` elements equals 1. |
| E2E-41 | Homepage has a navigation landmark | `/` | Count of elements with role `navigation` is ≥ 1. |
| E2E-42 | Homepage has a contentinfo landmark | `/` | Count of elements with role `contentinfo` is ≥ 1. |
| E2E-43 | Find a Plan zip code field has an accessible label | `/find-a-plan` | The zip code input resolves via `get_by_label("Zip code")` (programmatic label association, not just adjacent text). |
| E2E-44 | Contact Us "Expand all" reveals concierge phone number | `/about-us/contact-us` → click "Expand all" | The `tel:1-833-242-2223` (ACCESS On-Demand Concierge) link becomes visible. |
| E2E-45 | Breadcrumb "Home" link resolves from a nested page | `/find-plans/ways-to-enroll` → click breadcrumb "Home" | HTTP status < 400 on the resulting navigation. |

### Execution note on interactive cases

E2E-33..E2E-39 and E2E-44 exercise real client-side interaction (language
toggle, text-size toggle, on-site search, responsive breakpoints, accordion
expand) that this repo's authoring environment could not pre-verify against a
live browser session this round (sandbox had no Playwright MCP browser access
and egress to the target host is blocked — see PR discussion). Assertions are
designed to be falsifiable either way; the CI workflow (`.github/workflows/e2e.yml`,
open egress) is the first real execution and the source of truth for pass/fail
on these specific cases, consistent with this repo's existing convention for
E2E-01..E2E-13.

## Not covered by this suite

- Provider/doctor search (`providersearch.alignmenthealthplan.com`) — separate host, out of the
  stated crawl bound; link presence/target verified only (E2E-13, E2E-26, E2E-27).
- Member/Provider/Agent portals — require authentication; explicitly excluded by the assignment.
- Any lead-capture, contact, or seminar-registration form **submission** — would write a real record
  against a production third-party system; only field/control *presence* is validated.
