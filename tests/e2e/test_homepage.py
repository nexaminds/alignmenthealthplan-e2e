"""Homepage and hero section tests.

Tests the primary entry point, hero section, key CTAs, and top-level navigation.
"""

import re
import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_01_homepage_loads(page: Page, base_url: str) -> None:
    """E2E-01: Homepage loads with valid HTTP response and non-empty title."""
    response = page.goto(base_url, wait_until="domcontentloaded")
    
    assert response is not None
    assert response.status < 400, f"Got HTTP {response.status}"
    expect(page).to_have_title(re.compile(r"Medicare Advantage.*Alignment"))


@pytest.mark.readonly
def test_e2e_02_hero_section_visible(page: Page, base_url: str) -> None:
    """E2E-02: Hero section with main headline and CTA renders."""
    page.goto(base_url)
    
    # Check for main headline
    expect(page.locator("text=Medicare Advantage")).to_be_visible()
    expect(page.locator("text=Plans that Put You First")).to_be_visible()
    
    # Check for Enroll Now CTA
    enroll_btn = page.locator('a[href*="/find-a-plan"]').first
    expect(enroll_btn).to_be_visible()


@pytest.mark.readonly
def test_e2e_03_zip_code_form_present(page: Page, base_url: str) -> None:
    """E2E-03: Plan search form with zip code input is present and interactive."""
    page.goto(base_url)
    
    # Find the zip code input
    zip_input = page.locator('input[type="text"]').first
    expect(zip_input).to_be_visible()
    
    # Verify placeholder or label text
    page_text = page.content()
    assert "Zip code" in page_text or "zip" in page_text.lower()


@pytest.mark.readonly
def test_e2e_04_main_navigation_menu(page: Page, base_url: str) -> None:
    """E2E-04: Main navigation menu items are visible and clickable."""
    page.goto(base_url)
    
    # Check for primary nav sections
    nav_items = [
        "Discover Alignment",
        "Find Plans",
        "Find Care",
        "For Members",
        "For Providers"
    ]
    
    for nav_item in nav_items:
        nav_elem = page.locator(f"text={nav_item}").first
        expect(nav_elem).to_be_visible()


@pytest.mark.readonly
def test_e2e_05_logo_links_to_home(page: Page, base_url: str) -> None:
    """E2E-05: Logo/branding element links back to homepage."""
    page.goto(base_url)
    
    # Look for logo link (typically in header)
    logo = page.locator("img[alt*='Alignment']").first
    expect(logo).to_be_visible()
    
    # Parent link should exist
    logo_link = logo.locator("..")
    expect(logo_link).to_have_url(re.compile(r"alignmenthealthplan\.com/?$"))


@pytest.mark.readonly
def test_e2e_06_benefits_section_displays(page: Page, base_url: str) -> None:
    """E2E-06: Benefits showcase section renders with key plan benefits."""
    page.goto(base_url)
    page.wait_for_selector("text=benefits")
    
    # Check for benefit callouts
    benefits = [
        "Monthly plan premium",
        "Copay for primary care",
        "Copay on over 10,000 drugs",
        "Vision coverage",
        "Gym membership"
    ]
    
    for benefit in benefits:
        expect(page.locator(f"text={benefit}")).to_be_visible()


@pytest.mark.readonly
def test_e2e_07_concierge_section_visible(page: Page, base_url: str) -> None:
    """E2E-07: ACCESS On-Demand Concierge section is displayed."""
    page.goto(base_url)
    
    # Scroll to find concierge section
    page.locator("text=ACCESS").first.scroll_into_view()
    expect(page.locator("text=ACCESS On-Demand")).to_be_visible()
    expect(page.locator("text=24/7")).to_be_visible()


@pytest.mark.readonly
def test_e2e_08_phone_number_displayed(page: Page, base_url: str) -> None:
    """E2E-08: Customer service phone number is prominently displayed."""
    page.goto(base_url)
    
    # Check for phone number
    phone = page.locator("text=1-888-293-8272")
    expect(phone).to_be_visible()


@pytest.mark.readonly
def test_e2e_09_footer_links_present(page: Page, base_url: str) -> None:
    """E2E-09: Footer contains legal and company links."""
    page.goto(base_url)
    
    # Scroll to footer
    page.locator("text=© Copyright").scroll_into_view()
    
    footer_links = [
        "Legal Notices",
        "Privacy Notices",
        "Terms of Use",
        "Nondiscrimination Policy"
    ]
    
    for link_text in footer_links:
        expect(page.locator(f"text={link_text}").first).to_be_visible()


@pytest.mark.readonly
def test_e2e_10_five_star_rating_badge(page: Page, base_url: str) -> None:
    """E2E-10: 5-star rating badge and claim are visible."""
    page.goto(base_url)
    
    # Check for 5-star references
    expect(page.locator("text=5-star")).to_be_visible()
    expect(page.locator("text=Alignment Health Plan earned")).to_be_visible()
