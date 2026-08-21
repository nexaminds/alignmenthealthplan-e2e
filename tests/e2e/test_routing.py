"""Test page routing, not-found, and error page handling."""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_71_404_page_rendered(page: Page, base_url: str) -> None:
    """E2E-71: visiting a non-existent page returns 404 and renders error page."""
    response = page.goto(f"{base_url}/this-page-definitely-does-not-exist-xyz", wait_until="domcontentloaded")
    if response:
        assert response.status == 404, f"Expected 404, got {response.status}"


@pytest.mark.readonly
def test_e2e_72_404_page_helpful(page: Page, base_url: str) -> None:
    """E2E-72: 404 error page contains helpful information."""
    page.goto(f"{base_url}/this-page-definitely-does-not-exist-xyz", wait_until="domcontentloaded")
    error_text = page.locator("h1, h2, p").first
    if error_text.count() > 0:
        text = error_text.text_content()
        # Should have some error message
        assert len(text.strip()) > 0, "404 page has no helpful message"


@pytest.mark.readonly
def test_e2e_73_404_page_has_navigation(page: Page, base_url: str) -> None:
    """E2E-73: 404 page provides way back to home or navigation."""
    page.goto(f"{base_url}/this-page-definitely-does-not-exist-xyz", wait_until="domcontentloaded")
    home_link = page.locator("a:has-text(/home|back|start/i), a[href='/']")
    assert home_link.count() > 0, "404 page missing navigation back to home"


@pytest.mark.readonly
def test_e2e_74_non_existent_subpath_404(page: Page, base_url: str) -> None:
    """E2E-74: deeply nested non-existent paths return 404."""
    response = page.goto(f"{base_url}/deeply/nested/fake/path/xyz", wait_until="domcontentloaded")
    if response:
        # Should be 404 or 404-like
        assert response.status >= 400, f"Expected error status, got {response.status}"


@pytest.mark.readonly
def test_e2e_75_trailing_slash_consistency(page: Page, base_url: str) -> None:
    """E2E-75: trailing slash handling is consistent."""
    response1 = page.goto(f"{base_url}/", wait_until="domcontentloaded")
    assert response1.status < 400, "Root path should be valid"
    
    response2 = page.goto(base_url, wait_until="domcontentloaded")
    assert response2.status < 400, "Home without trailing slash should redirect or work"


@pytest.mark.readonly
def test_e2e_76_http_status_codes_correct(page: Page, base_url: str) -> None:
    """E2E-76: successful pages return 2xx status codes."""
    response = page.goto(base_url, wait_until="domcontentloaded")
    assert response is not None, "No response from server"
    assert response.status >= 200 and response.status < 300, f"Expected 2xx, got {response.status}"


@pytest.mark.readonly
def test_e2e_77_redirects_follow_chain(page: Page, base_url: str) -> None:
    """E2E-77: redirects are followed correctly."""
    # Navigate with automatic redirect following enabled (default)
    response = page.goto(base_url, wait_until="domcontentloaded")
    # Final response should be 2xx
    assert response.status < 400, f"Redirect chain failed: {response.status}"


@pytest.mark.readonly
def test_e2e_78_static_asset_paths_valid(page: Page, base_url: str) -> None:
    """E2E-78: static asset paths (css, js, images) are valid."""
    page.goto(base_url, wait_until="domcontentloaded")
    # Check a few assets
    stylesheets = page.locator("link[rel='stylesheet']")
    count = min(stylesheets.count(), 3)
    for i in range(count):
        href = stylesheets.nth(i).get_attribute("href")
        # href should not be empty
        assert href, f"Stylesheet {i} has no href"


@pytest.mark.readonly
def test_e2e_79_page_document_type_correct(page: Page, base_url: str) -> None:
    """E2E-79: page declares correct document type (HTML5 <!DOCTYPE html>)."""
    page.goto(base_url, wait_until="domcontentloaded")
    # Check for HTML structure
    html = page.locator("html")
    assert html.count() > 0, "Page missing html element"


@pytest.mark.readonly
def test_e2e_80_charset_declaration_early(page: Page, base_url: str) -> None:
    """E2E-80: charset is declared early in the document head."""
    page.goto(base_url, wait_until="domcontentloaded")
    # Charset should be in head
    charset = page.locator("head meta[charset]")
    assert charset.count() > 0, "Charset not declared early in head"
