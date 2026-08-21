"""Regression test suite for Alignment Health Plan website.

Covers the following pages:
- Homepage: hero, navigation, key sections, responsive behavior
- Find a Plan page: page load, form fields, CTAs
- Contact Us page: page load, contact sections, phone numbers, form structure
- Legal Notices page: footer link, page structure, content presence
- Privacy Notices page: footer link, page structure, content presence

One behavior per test. Each test maps to the E2E test matrix.
"""

import re

import pytest
from playwright.sync_api import Page, expect


# ============================================================================
# HOMEPAGE TESTS (E2E-02 to E2E-07)
# ============================================================================


@pytest.mark.readonly
def test_e2e_02_homepage_loads_with_title(page: Page, base_url: str) -> None:
    """E2E-02: homepage loads with expected page title."""
    response = page.goto(base_url, wait_until="domcontentloaded")

    assert response is not None
    assert response.status < 400, f"HTTP {response.status}"
    expect(page).to_have_title(
        re.compile(r"Medicare Advantage Plans.*Alignment Health Plan")
    )


@pytest.mark.readonly
def test_e2e_03_homepage_logo_visible(page: Page, base_url: str) -> None:
    """E2E-03: homepage displays Alignment Health Plan logo."""
    page.goto(base_url, wait_until="domcontentloaded")

    # Logo is typically an img with alt text or link with logo image
    logo = page.locator("img[alt*='Alignment']").first
    assert logo.count() > 0, "Logo image not found"
    expect(logo).to_be_visible()


@pytest.mark.readonly
def test_e2e_04_homepage_navigation_menu_present(page: Page, base_url: str) -> None:
    """E2E-04: homepage navigation menu contains key sections."""
    page.goto(base_url, wait_until="domcontentloaded")

    # Check for navigation links for main sections
    menu_items = ["Discover Alignment", "Find Plans", "Find Care", "For Members"]
    for item in menu_items:
        link = page.locator(f"text={item}").first
        assert link.count() > 0, f"Menu item '{item}' not found"


@pytest.mark.readonly
def test_e2e_05_homepage_hero_section_contains_zipcode_form(page: Page, base_url: str) -> None:
    """E2E-05: homepage hero section contains zipcode search form."""
    page.goto(base_url, wait_until="domcontentloaded")

    # Look for zipcode input
    zipcode_input = page.locator("input[placeholder*='ip']").first
    # Alternative: search for 'Zip code' label or placeholder
    if zipcode_input.count() == 0:
        # Try finding by label or nearby text
        zipcode_label = page.locator("text=Zip code").first
        assert zipcode_label.count() > 0, "Zipcode form element not found"
    else:
        expect(zipcode_input).to_be_visible()


@pytest.mark.readonly
def test_e2e_06_homepage_benefits_section_visible(page: Page, base_url: str) -> None:
    """E2E-06: homepage displays benefits section with plan features."""
    page.goto(base_url, wait_until="domcontentloaded")

    # Look for benefits heading or text mentioning benefits
    benefits_heading = page.locator("text=benefits").first
    assert benefits_heading.count() > 0, "Benefits section not found"
    expect(benefits_heading).to_be_visible()


@pytest.mark.readonly
def test_e2e_07_homepage_footer_links_present(page: Page, base_url: str) -> None:
    """E2E-07: homepage footer contains legal and policy links."""
    page.goto(base_url, wait_until="domcontentloaded")

    # Scroll to footer
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    # Check for common footer links
    footer_links = ["Legal Notices", "Privacy", "Terms of Use"]
    found_count = 0
    for link_text in footer_links:
        link = page.locator(f"text={link_text}").first
        if link.count() > 0:
            found_count += 1

    assert found_count >= 2, "Expected at least 2 footer legal links"


# ============================================================================
# FIND A PLAN PAGE TESTS (E2E-08 to E2E-12)
# ============================================================================


@pytest.mark.readonly
def test_e2e_08_find_plan_page_loads(page: Page, base_url: str) -> None:
    """E2E-08: Find a Plan page loads with correct title."""
    response = page.goto(f"{base_url}/find-a-plan", wait_until="domcontentloaded")

    assert response is not None
    assert response.status < 400
    expect(page).to_have_title(re.compile(r"Find a Plan"))


@pytest.mark.readonly
def test_e2e_09_find_plan_page_contains_form(page: Page, base_url: str) -> None:
    """E2E-09: Find a Plan page displays contact form fields."""
    page.goto(f"{base_url}/find-a-plan", wait_until="domcontentloaded")

    # Look for form fields: First Name, Last Name, Email, Phone
    form_fields = ["First Name", "Last Name", "Email", "Phone"]
    for field in form_fields:
        field_label = page.locator(f"text={field}").first
        assert field_label.count() > 0, f"Form field '{field}' not found"


@pytest.mark.readonly
def test_e2e_10_find_plan_page_heading_visible(page: Page, base_url: str) -> None:
    """E2E-10: Find a Plan page contains page heading."""
    page.goto(f"{base_url}/find-a-plan", wait_until="domcontentloaded")

    # Look for main heading or CTA text
    heading = page.locator("h1, h2").filter(has_text=re.compile(r"Need Help|Contact")).first
    assert heading.count() > 0, "Page heading not found"
    expect(heading).to_be_visible()


@pytest.mark.readonly
def test_e2e_11_find_plan_page_cta_button_present(page: Page, base_url: str) -> None:
    """E2E-11: Find a Plan page contains CTA button or submit element."""
    page.goto(f"{base_url}/find-a-plan", wait_until="domcontentloaded")

    # Look for button with submit-like text
    cta = page.locator("button, input[type='submit']").filter(
        has_text=re.compile(r"Submit|Send|Get|Help", re.IGNORECASE)
    ).first
    assert cta.count() > 0, "CTA button not found"
    expect(cta).to_be_visible()


@pytest.mark.readonly
def test_e2e_12_find_plan_page_phone_number_visible(page: Page, base_url: str) -> None:
    """E2E-12: Find a Plan page displays phone number for assistance."""
    page.goto(f"{base_url}/find-a-plan", wait_until="domcontentloaded")

    # Look for phone number pattern or direct phone link
    phone_pattern = re.compile(r"\d{1,3}-\d{3}-\d{4}")
    phone_text = page.locator(f"text={phone_pattern}").first
    # Alternative: look for tel: link
    if phone_text.count() == 0:
        phone_link = page.locator("a[href^='tel:']").first
        assert phone_link.count() > 0, "Phone number or tel link not found"
    else:
        expect(phone_text).to_be_visible()


# ============================================================================
# CONTACT US PAGE TESTS (E2E-13 to E2E-16)
# ============================================================================


@pytest.mark.readonly
def test_e2e_13_contact_us_page_loads(page: Page, base_url: str) -> None:
    """E2E-13: Contact Us page loads with correct title."""
    response = page.goto(
        f"{base_url}/about-us/contact-us", wait_until="domcontentloaded"
    )

    assert response is not None
    assert response.status < 400
    expect(page).to_have_title(re.compile(r"Contact Us"))


@pytest.mark.readonly
def test_e2e_14_contact_us_page_heading_present(page: Page, base_url: str) -> None:
    """E2E-14: Contact Us page displays main heading."""
    page.goto(f"{base_url}/about-us/contact-us", wait_until="domcontentloaded")

    # Look for h1 or h2 with Contact Us text
    heading = page.locator("h1, h2").filter(has_text=re.compile(r"Contact", re.IGNORECASE)).first
    assert heading.count() > 0, "Contact Us heading not found"
    expect(heading).to_be_visible()


@pytest.mark.readonly
def test_e2e_15_contact_us_page_multiple_contact_options(page: Page, base_url: str) -> None:
    """E2E-15: Contact Us page displays multiple contact methods."""
    page.goto(f"{base_url}/about-us/contact-us", wait_until="domcontentloaded")

    # Look for contact sections or categories
    contact_sections = ["Member", "Provider", "Sales", "Pharmacy"]
    found_count = 0
    for section in contact_sections:
        section_elem = page.locator(f"text={section}").first
        if section_elem.count() > 0:
            found_count += 1

    assert found_count >= 2, "Expected at least 2 contact section options"


@pytest.mark.readonly
def test_e2e_16_contact_us_page_phone_links(page: Page, base_url: str) -> None:
    """E2E-16: Contact Us page contains clickable phone links."""
    page.goto(f"{base_url}/about-us/contact-us", wait_until="domcontentloaded")

    # Look for tel: links (phone numbers)
    tel_links = page.locator("a[href^='tel:']")
    assert tel_links.count() > 0, "No phone links found"


# ============================================================================
# LEGAL NOTICES PAGE TESTS (E2E-17 to E2E-18)
# ============================================================================


@pytest.mark.readonly
def test_e2e_17_legal_notices_page_loads(page: Page, base_url: str) -> None:
    """E2E-17: Legal Notices page loads with correct title."""
    response = page.goto(
        f"{base_url}/about-us/legal-notices", wait_until="domcontentloaded"
    )

    assert response is not None
    assert response.status < 400
    expect(page).to_have_title(re.compile(r"Legal Notices"))


@pytest.mark.readonly
def test_e2e_18_legal_notices_page_contains_disclaimer(page: Page, base_url: str) -> None:
    """E2E-18: Legal Notices page displays plan disclaimer content."""
    page.goto(f"{base_url}/about-us/legal-notices", wait_until="domcontentloaded")

    # Look for plan type text or disclaimer
    disclaimer = page.locator("text=HMO").first
    # Alternative: look for Medicare or plan-related text
    if disclaimer.count() == 0:
        disclaimer = page.locator("text=Medicare").first

    assert disclaimer.count() > 0, "Legal disclaimer content not found"
    expect(disclaimer).to_be_visible()


# ============================================================================
# PRIVACY NOTICES PAGE TESTS (E2E-19 to E2E-20)
# ============================================================================


@pytest.mark.readonly
def test_e2e_19_privacy_notices_page_loads(page: Page, base_url: str) -> None:
    """E2E-19: Privacy Notices page loads with correct title."""
    response = page.goto(
        f"{base_url}/about-us/privacy-notices", wait_until="domcontentloaded"
    )

    assert response is not None
    assert response.status < 400
    expect(page).to_have_title(re.compile(r"Privacy"))


@pytest.mark.readonly
def test_e2e_20_privacy_notices_page_contains_privacy_content(page: Page, base_url: str) -> None:
    """E2E-20: Privacy Notices page displays privacy policy content."""
    page.goto(f"{base_url}/about-us/privacy-notices", wait_until="domcontentloaded")

    # Look for privacy-related content
    privacy_content = page.locator("text=Protected Health Information").first
    # Alternative: look for HIPAA or privacy disclosure
    if privacy_content.count() == 0:
        privacy_content = page.locator("text=privacy").first

    assert privacy_content.count() > 0, "Privacy content not found"
    expect(privacy_content).to_be_visible()
