"""Contact Us accordion interaction — E2E-44.

Execution note: real click-driven accordion behavior this authoring session
could not pre-verify against a live browser (see case-matrix.md 'Execution
note on interactive cases'). CI is the first real run.
"""

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_44_contact_us_expand_all_reveals_concierge_phone(page: Page, base_url: str) -> None:
    """E2E-44: 'Expand all' reveals the ACCESS On-Demand Concierge phone number."""
    page.goto(f"{base_url}/about-us/contact-us", wait_until="domcontentloaded")

    page.get_by_role("link", name="Expand all", exact=True).first.click()

    expect(page.locator("a[href^='tel:1-833-242-2223']").first).to_be_visible()
