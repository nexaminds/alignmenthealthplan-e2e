"""Text size toggle — E2E-35.

Execution note: real click-driven visual behavior this authoring session could
not pre-verify against a live browser (see case-matrix.md 'Execution note on
interactive cases'). CI is the first real run.
"""

import pytest
from playwright.sync_api import Page


@pytest.mark.readonly
def test_e2e_35_large_text_size_increases_font_size(page: Page, base_url: str) -> None:
    """E2E-35: clicking 'Large' increases the computed font-size of body copy."""
    page.goto(base_url, wait_until="domcontentloaded")

    reference = page.locator("p").first
    before = reference.evaluate("el => parseFloat(getComputedStyle(el).fontSize)")

    page.get_by_role("link", name="Large", exact=True).first.click()

    after = reference.evaluate("el => parseFloat(getComputedStyle(el).fontSize)")

    assert after > before, f"expected font-size to increase after selecting Large, got {before}px -> {after}px"
