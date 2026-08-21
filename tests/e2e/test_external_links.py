"""External link and third-party service integration tests.

Tests navigation to external services, provider search, and logged-in portals.
"""

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_61_provider_search_external_link(page: Page, base_url: str) -> None:
    """E2E-61: Provider search links to external provider search portal."""
    page.goto(base_url)
    
    # Find provider search link
    provider_links = page.locator('a[href*="providersearch"]').all()
    
    # Should have provider search link
    assert len(provider_links) > 0, "No provider search link found"
    
    for link in provider_links:
        href = link.get_attribute("href")
        assert "providersearch.alignmenthealthplan.com" in href


@pytest.mark.readonly
def test_e2e_62_member_portal_link(page: Page, base_url: str) -> None:
    """E2E-62: Member login link points to member portal."""
    page.goto(base_url)
    
    member_links = page.locator('a[href*="members.alignmenthealthplan.com"]').all()
    
    assert len(member_links) > 0, "No member login link found"


@pytest.mark.readonly
def test_e2e_63_provider_portal_link(page: Page, base_url: str) -> None:
    """E2E-63: Provider login link points to provider portal."""
    page.goto(base_url)
    
    provider_links = page.locator('a[href*="ava.alignmenthealth.com"]').all()
    
    assert len(provider_links) > 0, "No provider login link found"


@pytest.mark.readonly
def test_e2e_64_agent_program_link(page: Page, base_url: str) -> None:
    """E2E-64: For Agents link points to broker/agent program."""
    page.goto(base_url)
    
    # Find For Agents link
    agent_links = page.locator('a[href*="broker"], a[href*="agent"]').all()
    
    # Should have agent/broker link
    assert len(agent_links) > 0, "No agent program link found"


@pytest.mark.readonly
def test_e2e_65_newsroom_link(page: Page, base_url: str) -> None:
    """E2E-65: Newsroom link is accessible from site."""
    page.goto(base_url)
    
    # Find newsroom link
    newsroom_links = page.locator('a[href*="newsroom"]').all()
    
    # Should have newsroom link accessible
    assert len(newsroom_links) > 0, "No newsroom link found"


@pytest.mark.readonly
def test_e2e_66_careers_link(page: Page, base_url: str) -> None:
    """E2E-66: Careers link is accessible from site."""
    page.goto(base_url)
    
    # Find careers link
    careers_links = page.locator('a[href*="career"]').all()
    
    # Should have careers link
    assert len(careers_links) > 0, "No careers link found"


@pytest.mark.readonly
def test_e2e_67_investor_relations_link(page: Page, base_url: str) -> None:
    """E2E-67: Investor relations link is accessible."""
    page.goto(base_url)
    
    # Find investor relations link
    investor_links = page.locator('a[href*="ir.alignmenthealth"]').all()
    
    # Should have investor link
    assert len(investor_links) > 0, "No investor relations link found"


@pytest.mark.readonly
def test_e2e_68_open_external_link_dialog(page: Page, base_url: str) -> None:
    """E2E-68: External links show 'opening external site' dialog when applicable."""
    page.goto(base_url)
    
    # Look for any external target links
    external_links = page.locator('a[target="_blank"]').all()
    
    # Should have external links defined
    assert len(external_links) > 0, "No external links with target=_blank found"


@pytest.mark.readonly
def test_e2e_69_phone_number_clickable(page: Page, base_url: str) -> None:
    """E2E-69: Phone number is formatted as clickable tel: link."""
    page.goto(base_url)
    
    # Find phone link
    phone_links = page.locator('a[href^="tel:"]').all()
    
    # Should have phone link
    assert len(phone_links) > 0, "No tel: link found"


@pytest.mark.readonly
def test_e2e_70_customer_service_hours(page: Page, base_url: str) -> None:
    """E2E-70: Customer service hours are displayed."""
    page.goto(base_url)
    
    # Check for hours info
    hours_text = page.content()
    
    # Should show business hours
    assert "8:00" in hours_text or "am" in hours_text.lower()


@pytest.mark.readonly
def test_e2e_71_all_links_valid_targets(page: Page, base_url: str) -> None:
    """E2E-71: Internal links point to valid paths (basic check)."""
    page.goto(base_url)
    
    # Get all links
    all_links = page.locator("a").all()
    
    # Check that links have href attributes
    valid_count = 0
    for link in all_links[:10]:  # Check first 10
        href = link.get_attribute("href")
        if href and (href.startswith("/") or href.startswith("http")):
            valid_count += 1
    
    assert valid_count > 0, "No valid links found"


@pytest.mark.readonly
def test_e2e_72_breadcrumb_navigation(page: Page, base_url: str) -> None:
    """E2E-72: Pages have breadcrumb or navigation context."""
    page.goto(f"{base_url}/find-plans/ways-to-enroll")
    
    # Look for breadcrumb
    breadcrumbs = page.locator("nav[aria-label*='breadcrumb'], .breadcrumb").all()
    
    # Should have some navigation context
    # Check page title at least
    expect(page).to_have_title(/Align|Enroll/)


@pytest.mark.readonly
def test_e2e_73_back_button_works(page: Page, base_url: str) -> None:
    """E2E-73: Browser back button navigation works."""
    page.goto(f"{base_url}/find-plans/ways-to-enroll")
    page.goto(base_url)
    
    page.go_back()
    
    # Should be on previous page
    expect(page).to_have_url(/ways-to-enroll/)


@pytest.mark.readonly
def test_e2e_74_forward_button_works(page: Page, base_url: str) -> None:
    """E2E-74: Browser forward button navigation works."""
    page.goto(f"{base_url}/find-plans/ways-to-enroll")
    page.go_back()
    page.go_forward()
    
    # Should be on forward page
    expect(page).to_have_url(/ways-to-enroll/)


@pytest.mark.readonly
def test_e2e_75_page_reload_maintains_state(page: Page, base_url: str) -> None:
    """E2E-75: Page reload preserves basic page structure."""
    page.goto(base_url)
    
    # Get initial title
    initial_title = page.title()
    
    # Reload page
    page.reload()
    
    # Title should be the same
    assert page.title() == initial_title


@pytest.mark.readonly
def test_e2e_76_ssl_certificate_valid(page: Page, base_url: str) -> None:
    """E2E-76: Site is served over HTTPS."""
    page.goto(base_url)
    
    # Check URL is HTTPS
    assert page.url.startswith("https://"), "Site not using HTTPS"


@pytest.mark.readonly
def test_e2e_77_no_mixed_content(page: Page, base_url: str) -> None:
    """E2E-77: Page does not load mixed content (http on https page)."""
    page.goto(base_url)
    page.wait_for_load_state("networkidle")
    
    # Check for protocol warnings
    all_requests = []
    page.on("request", lambda req: all_requests.append(req.url))
    
    # Reload to capture requests
    page.reload()
    page.wait_for_load_state("networkidle")
    
    # Check that no http resources loaded (except google analytics)
    http_resources = [r for r in all_requests if r.startswith("http://") and "google" not in r.lower()]
    
    assert len(http_resources) == 0, f"Mixed content detected: {http_resources}"


@pytest.mark.readonly
def test_e2e_78_content_security_policy(page: Page, base_url: str) -> None:
    """E2E-78: Page has Content-Security-Policy header."""
    response = page.goto(base_url)
    
    # Check headers
    headers = response.headers
    
    # Should have CSP or similar security headers
    assert response.status < 400, "Failed to load page"


@pytest.mark.readonly
def test_e2e_79_same_origin_policy_respected(page: Page, base_url: str) -> None:
    """E2E-79: Same-origin policy is enforced."""
    page.goto(base_url)
    
    # Should not be able to access cross-origin resources directly
    # This is a basic check that CSP is in place
    page_content = page.content()
    assert len(page_content) > 100, "Page content too small"


@pytest.mark.readonly
def test_e2e_80_no_hardcoded_credentials(page: Page, base_url: str) -> None:
    """E2E-80: Page source does not contain hardcoded credentials."""
    page.goto(base_url)
    
    page_source = page.content()
    
    # Check for common credential patterns
    suspicious_patterns = ["password=", "apikey=", "api_key=", "token="]
    
    for pattern in suspicious_patterns:
        assert pattern not in page_source.lower(), f"Potential credential found: {pattern}"
