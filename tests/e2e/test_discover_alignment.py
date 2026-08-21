"""Discover Alignment section — E2E-21."""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_21_medicare_advantage_faqs_page_renders(page: Page, base_url: str) -> None:
    """E2E-21: Medicare Advantage FAQs page loads with at least 15 FAQ articles."""
    response = page.goto(
        f"{base_url}/discover-ahp/medicare-advantage-frequently-asked-questions",
        wait_until="domcontentloaded",
    )

    assert response is not None, (
        "no response from /discover-ahp/medicare-advantage-frequently-asked-questions"
    )
    assert response.status < 400, (
        f"medicare-advantage-frequently-asked-questions returned HTTP {response.status}"
    )
    expect(page).to_have_title(re.compile(r"medicare advantage faqs", re.I))

    article_heading_count = page.get_by_role("heading", level=2).count()
    assert article_heading_count >= 15, (
        f"expected at least 15 FAQ article headings, found {article_heading_count}"
    )
