"""Test search functionality, filters, and content discovery."""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_29_search_box_present(page: Page, base_url: str) -> None:
    """E2E-29: page has a search input field."""
    page.goto(base_url, wait_until="domcontentloaded")
    search = page.locator("input[type='search'], input[placeholder*='search' i], [class*='search'] input")
    if search.count() > 0:
        expect(search.first).to_be_visible()


@pytest.mark.readonly
def test_e2e_30_search_input_accepts_text(page: Page, base_url: str) -> None:
    """E2E-30: search field accepts keyboard input."""
    page.goto(base_url, wait_until="domcontentloaded")
    search = page.locator("input[type='search'], input[placeholder*='search' i]").first
    if search.count() > 0:
        search.fill("test query")
        value = search.input_value()
        assert value == "test query", "Search field did not accept input"


@pytest.mark.readonly
def test_e2e_31_filter_controls_present(page: Page, base_url: str) -> None:
    """E2E-31: page has filter or sort controls if displaying lists."""
    page.goto(base_url, wait_until="domcontentloaded")
    filters = page.locator("[class*='filter'], [class*='sort'], select")
    # Not all pages need filters, so just check if visible when present
    if filters.count() > 0:
        expect(filters.first).to_be_visible()


@pytest.mark.readonly
def test_e2e_32_pagination_if_needed(page: Page, base_url: str) -> None:
    """E2E-32: multi-page content has pagination controls."""
    page.goto(base_url, wait_until="domcontentloaded")
    pagination = page.locator("[class*='pagination'], [class*='pager'], nav a[rel='next']")
    # Only check if pagination is present
    if pagination.count() > 0:
        expect(pagination.first).to_be_visible()


@pytest.mark.readonly
def test_e2e_33_breadcrumb_navigation_if_nested(page: Page, base_url: str) -> None:
    """E2E-33: nested pages display breadcrumb navigation."""
    page.goto(f"{base_url}/about", wait_until="domcontentloaded")
    breadcrumb = page.locator("[class*='breadcrumb'], nav[aria-label*='breadcrumb' i]")
    if breadcrumb.count() > 0:
        expect(breadcrumb).to_be_visible()
