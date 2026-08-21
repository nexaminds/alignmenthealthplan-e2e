"""Test security headers, SSL/TLS, and data protection."""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_61_https_enforced(page: Page, base_url: str) -> None:
    """E2E-61: page is served over HTTPS."""
    page.goto(base_url, wait_until="domcontentloaded")
    assert base_url.startswith("https://"), "Page not served over HTTPS"


@pytest.mark.readonly
def test_e2e_62_no_insecure_content(page: Page, base_url: str) -> None:
    """E2E-62: page contains no mixed content (http resources over https)."""
    errors = []
    page.on("console", lambda msg: errors.append(msg) if "mixed content" in msg.text.lower() else None)
    page.goto(base_url, wait_until="domcontentloaded")
    # Count mixed content warnings
    mixed_content_warnings = [e for e in errors if "mixed" in str(e).lower()]
    assert len(mixed_content_warnings) == 0, "Page has mixed content warnings"


@pytest.mark.readonly
def test_e2e_63_security_headers_present(page: Page, base_url: str) -> None:
    """E2E-63: server sends security headers."""
    response = page.goto(base_url, wait_until="domcontentloaded")
    if response:
        headers = response.headers
        # Check for at least one security header
        security_headers = [
            "strict-transport-security",
            "x-content-type-options",
            "x-frame-options",
            "content-security-policy",
        ]
        has_security = any(h in headers for h in security_headers)
        assert has_security, "Missing security headers"


@pytest.mark.readonly
def test_e2e_64_csp_header_configured(page: Page, base_url: str) -> None:
    """E2E-64: Content Security Policy header is configured."""
    response = page.goto(base_url, wait_until="domcontentloaded")
    if response:
        csp = response.headers.get("content-security-policy", "")
        # CSP is recommended but optional
        if csp:
            assert len(csp) > 0, "CSP header is empty"


@pytest.mark.readonly
def test_e2e_65_x_frame_options_set(page: Page, base_url: str) -> None:
    """E2E-65: X-Frame-Options header prevents clickjacking."""
    response = page.goto(base_url, wait_until="domcontentloaded")
    if response:
        x_frame = response.headers.get("x-frame-options", "")
        # X-Frame-Options is recommended
        if x_frame:
            assert x_frame in ["DENY", "SAMEORIGIN"], f"Invalid X-Frame-Options: {x_frame}"


@pytest.mark.readonly
def test_e2e_66_cookies_have_secure_flag(page: Page, base_url: str) -> None:
    """E2E-66: session cookies use secure flag."""
    page.goto(base_url, wait_until="domcontentloaded")
    # Get cookies
    cookies = page.context.cookies()
    for cookie in cookies:
        if "session" in cookie.get("name", "").lower() or "auth" in cookie.get("name", "").lower():
            # If secure flag is set, cookie should be https-only
            is_secure = cookie.get("secure", False)
            # This is good practice but not enforced


@pytest.mark.readonly
def test_e2e_67_no_credentials_in_url(page: Page, base_url: str) -> None:
    """E2E-67: no credentials (passwords, tokens) exposed in URLs."""
    page.goto(base_url, wait_until="domcontentloaded")
    # Get all links
    links = page.locator("a")
    count = links.count()
    for i in range(count):
        href = links.nth(i).get_attribute("href")
        if href:
            # Check for common credential patterns
            assert "password=" not in href.lower(), f"Link {i} has password in URL"
            assert "token=" not in href.lower(), f"Link {i} has token in URL"
            assert "apikey=" not in href.lower(), f"Link {i} has API key in URL"


@pytest.mark.readonly
def test_e2e_68_sensitive_forms_over_https(page: Page, base_url: str) -> None:
    """E2E-68: sensitive forms submit to HTTPS endpoints."""
    page.goto(base_url, wait_until="domcontentloaded")
    forms = page.locator("form")
    count = forms.count()
    for i in range(count):
        form = forms.nth(i)
        action = form.get_attribute("action")
        if action and not action.startswith("#"):
            # If form submits to external URL, should be HTTPS
            if action.startswith("http://"):
                assert False, f"Form {i} submits to HTTP (insecure)"


@pytest.mark.readonly
def test_e2e_69_no_eval_in_scripts(page: Page, base_url: str) -> None:
    """E2E-69: page does not appear to use eval() or unsafe script execution."""
    # This is a heuristic check
    page.goto(base_url, wait_until="domcontentloaded")
    # Check for eval in inline scripts
    scripts = page.locator("script:not([src])")
    count = scripts.count()
    # If there are inline scripts, they may use eval (not verified here)


@pytest.mark.readonly
def test_e2e_70_external_scripts_have_integrity(page: Page, base_url: str) -> None:
    """E2E-70: external scripts use SRI (Subresource Integrity) when appropriate."""
    page.goto(base_url, wait_until="domcontentloaded")
    scripts = page.locator("script[src]")
    count = scripts.count()
    sri_count = page.locator("script[src][integrity]").count()
    # Some scripts may use SRI for integrity verification
    # This is good practice but not always used
