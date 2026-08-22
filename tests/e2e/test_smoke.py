"""Seed smoke test - establishes the convention for authored cases.

Naming maps 1:1 to the case matrix ID so the report can join on it:
    E2E-01  ->  test_e2e_01_<behavior>

Keep one behavior per test. A test asserting four things reports as one row
and hides three results.
"""

import re

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def browser_sync():
    """Create a sync browser instance."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()


@pytest.fixture
def page_sync(browser_sync, base_url):
    """Create a page with TLS error tolerance."""
    context = browser_sync.new_context(ignore_https_errors=True)
    page = context.new_page()
    yield page
    page.close()
    context.close()


@pytest.mark.readonly
def test_e2e_01_home_page_renders(page_sync, base_url: str) -> None:
    """E2E-01: the entry point loads and renders a non-empty document title."""
    response = page_sync.goto(base_url, wait_until="domcontentloaded")

    assert response is not None, f"no response from {base_url}"
    assert response.status < 400, f"{base_url} returned HTTP {response.status}"
    assert page_sync.title() and len(page_sync.title()) > 0, "page title is empty"
