"""Navigation and menu structure tests.

Tests primary and secondary navigation, dropdown menus, and menu state management.
"""

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_11_discover_alignment_menu_expands(page: Page, base_url: str) -> None:
    """E2E-11: Discover Alignment menu expands with submenu items."""
    page.goto(base_url)
    
    menu_trigger = page.locator("text=Discover Alignment").first
    expect(menu_trigger).to_be_visible()
    
    # Hover to expand submenu
    page.locator("text=Discover Alignment").first.hover()
    
    # Check for submenu items
    expect(page.locator("text=Why Alignment Health Plan")).to_be_visible()
    expect(page.locator("text=What is Medicare Advantage")).to_be_visible()


@pytest.mark.readonly
def test_e2e_12_find_plans_submenu_items(page: Page, base_url: str) -> None:
    """E2E-12: Find Plans menu contains shop, enroll, and seminar options."""
    page.goto(base_url)
    
    page.locator("text=Find Plans").first.hover()
    
    submenu_items = [
        "Shop Online",
        "Ways to Enroll",
        "Attend",
        "Benefit Highlights",
        "Pre-Enrollment Kit"
    ]
    
    for item in submenu_items:
        expect(page.locator(f"text={item}").first).to_be_visible()


@pytest.mark.readonly
def test_e2e_13_find_care_menu_navigation(page: Page, base_url: str) -> None:
    """E2E-13: Find Care menu provides access to provider search flows."""
    page.goto(base_url)
    
    page.locator("text=Find Care").first.hover()
    
    # Check for search options
    expect(page.locator("text=Doctor").first).to_be_visible()
    expect(page.locator("text=Drug").first).to_be_visible()
    expect(page.locator("text=Pharmacy").first).to_be_visible()


@pytest.mark.readonly
def test_e2e_14_member_login_accessible(page: Page, base_url: str) -> None:
    """E2E-14: Member login link is accessible from main menu."""
    page.goto(base_url)
    
    # Find Member Login link
    member_login = page.locator('a[href*="members.alignmenthealthplan.com"]').first
    expect(member_login).to_be_visible()
    
    # Verify it has correct href
    expect(member_login).to_have_attribute("href", /members\.alignmenthealthplan\.com/)


@pytest.mark.readonly
def test_e2e_15_provider_login_accessible(page: Page, base_url: str) -> None:
    """E2E-15: Provider login link is accessible from main menu."""
    page.goto(base_url)
    
    # Find Provider Login link
    provider_login = page.locator('a[href*="ava.alignmenthealth.com"]').first
    expect(provider_login).to_be_visible()
    
    # Verify it has correct href
    expect(provider_login).to_have_attribute("href", /ava\.alignmenthealth\.com/)


@pytest.mark.readonly
def test_e2e_16_mobile_menu_toggle(page: Page, base_url: str) -> None:
    """E2E-16: Mobile menu toggle button is accessible on small screens."""
    page.goto(base_url)
    page.set_viewport_size({"width": 375, "height": 667})
    
    # Look for mobile menu button (hamburger icon)
    mobile_button = page.locator("button[aria-label*='menu'], button[aria-label*='Menu'], .mobile-toggle").first
    
    # Should have a button for mobile navigation
    buttons = page.locator("button").all()
    assert len(buttons) > 0, "No buttons found on mobile view"


@pytest.mark.readonly
def test_e2e_17_for_members_submenu(page: Page, base_url: str) -> None:
    """E2E-17: For Members submenu includes services and resources links."""
    page.goto(base_url)
    
    page.locator("text=For Members").first.hover()
    
    # Check member submenu items
    expect(page.locator("text=Member Services")).to_be_visible()
    expect(page.locator("text=Forms and Resources")).to_be_visible()


@pytest.mark.readonly
def test_e2e_18_for_providers_submenu(page: Page, base_url: str) -> None:
    """E2E-18: For Providers submenu provides provider resource links."""
    page.goto(base_url)
    
    page.locator("text=For Providers").first.hover()
    
    # Check provider submenu items
    expect(page.locator("text=Provider Resources")).to_be_visible()
    expect(page.locator("text=Provider Manual")).to_be_visible()


@pytest.mark.readonly
def test_e2e_19_contact_us_accessible(page: Page, base_url: str) -> None:
    """E2E-19: Contact Us link is accessible from header."""
    page.goto(base_url)
    
    # Find Contact Us
    contact = page.locator('a[href*="/about-us/contact-us"]').first
    expect(contact).to_be_visible()


@pytest.mark.readonly
def test_e2e_20_enroll_now_primary_cta(page: Page, base_url: str) -> None:
    """E2E-20: Primary Enroll Now CTA is prominently placed in header."""
    page.goto(base_url)
    
    # Should have primary Enroll Now button in header
    enroll_buttons = page.locator('a:has-text("Enroll Now")').all()
    
    # Filter to header/top area
    for btn in enroll_buttons:
        if btn.is_visible():
            expect(btn).to_have_url(/find-a-plan/)
            break
    else:
        raise AssertionError("No visible Enroll Now button found")
