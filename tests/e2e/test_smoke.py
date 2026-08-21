"""Seed smoke test - establishes the convention for authored cases.

Naming maps 1:1 to the case matrix ID so the report can join on it:
    E2E-01  ->  test_e2e_01_<behavior>

Keep one behavior per test. A test asserting four things reports as one row
and hides three results.
"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_01_home_page_renders(page: Page, base_url: str) -> None:
    """E2E-01: the entry point loads and renders a non-empty document title."""
    response = page.goto(base_url, wait_until="domcontentloaded")

    assert response is not None, f"no response from {base_url}"
    assert response.status < 400, f"{base_url} returned HTTP {response.status}"
    expect(page).to_have_title(re.compile(r"\S"))
