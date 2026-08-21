"""On-site search — E2E-36..E2E-37.

Execution note: real form-submission interaction this authoring session could
not pre-verify against a live browser (see case-matrix.md 'Execution note on
interactive cases'). CI is the first real run.
"""

import re

import pytest
from playwright.sync_api import Page, expect


def _search_input(page: Page):
    """Resolve the site search control via the most specific accessible role first."""
    for locator in (
        page.get_by_role("searchbox"),
        page.get_by_role("textbox", name=re.compile(r"search", re.I)),
        page.locator("input[type='search']"),
    ):
        if locator.count() > 0:
            return locator.first
    raise AssertionError("no search input control found on the page")


@pytest.mark.readonly
def test_e2e_36_search_common_term_returns_results(page: Page, base_url: str) -> None:
    """E2E-36: searching a common site term does not land on the no-results state."""
    page.goto(base_url, wait_until="domcontentloaded")

    search_box = _search_input(page)
    search_box.fill("Medicare")
    search_box.press("Enter")

    expect(page.get_by_role("heading", name=re.compile(r"site search", re.I)).first).to_be_visible()
    expect(page.get_by_text(re.compile(r"no results were found", re.I))).to_have_count(0)


@pytest.mark.readonly
def test_e2e_37_search_nonsense_term_shows_no_results(page: Page, base_url: str) -> None:
    """E2E-37: searching a string with no matches shows the explicit no-results state."""
    page.goto(base_url, wait_until="domcontentloaded")

    search_box = _search_input(page)
    search_box.fill("zzznonexistentqueryxyz123")
    search_box.press("Enter")

    expect(page.get_by_text(re.compile(r"no results were found", re.I)).first).to_be_visible()
