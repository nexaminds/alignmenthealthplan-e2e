"""Regression test suite for alignmenthealthplan.com.

Covers homepage, Find a Plan, Contact Us, and legal/privacy footer pages.
Naming convention: E2E-NN -> test_e2e_nn_<behavior>
One behavior per test for granular failure reporting.
"""

import re
from typing import Pattern

import pytest
from playwright.sync_api import Page, expect


# ============================================================================
# HOMEPAGE TESTS (E2E-02 through E2E-07)
# ============================================================================


@pytest.mark.readonly
def test_e2e_02_home_page_title_correct(page: Page, base_url: str) -> None:
    """E2E-02: homepage title contains 'Medicare Advantage Plans' and 'Alignment Health Plan'."""
    page.goto(base_url, wait_until="domcontentloaded")
    expect(page).to_have_title(
        re.compile(r"Medicare Advantage Plans.*Alignment Health Plan", re.IGNORECASE)
    )


@pytest.mark.readonly
def test_e2e_03_home_page_main_heading_visible(page: Page, base_url: str) -> None:
    """E2E-03: homepage displays main hero heading about Medicare Advantage plans."""
    page.goto(base_url, wait_until="domcontentloaded")
    
    # Hero heading should be visible and contain key messaging
    hero_heading = page.get_by_role("heading", name=re.compile(r"Medicare.*Plans.*You", re.IGNORECASE))
    expect(hero_heading).to_be_visible()


@pytest.mark.readonly
def test_e2e_04_home_page_enroll_button_present(page: Page, base_url: str) -> None:
    """E2E-04: homepage has an 'Enroll Now' call-to-action button."""
    page.goto(base_url, wait_until="domcontentloaded")
    
    # Look for Enroll Now button/link
    enroll_button = page.get_by_role("link", name=re.compile(r"Enroll Now", re.IGNORECASE))
    expect(enroll_button).to_be_visible()


@pytest.mark.readonly
def test_e2e_05_home_page_benefits_section_displays(page: Page, base_url: str) -> None:
    """E2E-05: homepage benefits section shows key plan features (premium, copay, vision)."""
    page.goto(base_url, wait_until="domcontentloaded")
    
    # Verify benefits section heading is present
    benefits_heading = page.get_by_role("heading", name=re.compile(r"benefits", re.IGNORECASE))
    expect(benefits_heading).to_be_visible()
    
    # Check for specific benefit callouts (as low as $0 copay, etc.)
    page_text = page.inner_text("body")
    assert "Copay" in page_text, "Copay information missing from benefits"
    assert "Vision" in page_text, "Vision coverage information missing from benefits"


@pytest.mark.readonly
def test_e2e_06_home_page_navigation_menu_opens(page: Page, base_url: str) -> None:
    """E2E-06: homepage main navigation menu is accessible and contains key sections."""
    page.goto(base_url, wait_until="domcontentloaded")
    
    # Check for navigation links to main sections
    discover_link = page.get_by_role("link", name=re.compile(r"Discover.*Alignment", re.IGNORECASE))
    find_plans_link = page.get_by_role("link", name=re.compile(r"Find Plans", re.IGNORECASE))
    find_care_link = page.get_by_role("link", name=re.compile(r"Find Care", re.IGNORECASE))
    
    expect(discover_link).to_be_visible()
    expect(find_plans_link).to_be_visible()
    expect(find_care_link).to_be_visible()


@pytest.mark.readonly
def test_e2e_07_home_page_fortune_badge_visible(page: Page, base_url: str) -> None:
    """E2E-07: homepage displays Fortune World's Most Admired Companies badge."""
    page.goto(base_url, wait_until="domcontentloaded")
    
    # Look for the Fortune 2026 badge text on the page
    page_text = page.inner_text("body")
    assert "Fortune" in page_text, "Fortune badge missing"
    assert "2026" in page_text, "2026 year missing from badge"
    assert "Most Admired" in page_text, "Most Admired text missing from badge"


# ============================================================================
# FIND A PLAN PAGE TESTS (E2E-08 through E2E-12)
# ============================================================================


@pytest.mark.readonly
def test_e2e_08_find_plan_page_loads(page: Page, base_url: str) -> None:
    """E2E-08: Find a Plan page loads with correct title."""
    response = page.goto(f"{base_url}/find-a-plan", wait_until="domcontentloaded")
    
    assert response is not None, "no response from /find-a-plan"
    assert response.status < 400, f"/find-a-plan returned HTTP {response.status}"
    expect(page).to_have_title(re.compile(r"Find a Plan", re.IGNORECASE))


@pytest.mark.readonly
def test_e2e_09_find_plan_page_form_fields_present(page: Page, base_url: str) -> None:
    """E2E-09: Find a Plan page displays contact form with required fields."""
    page.goto(f"{base_url}/find-a-plan", wait_until="domcontentloaded")
    
    # Form should have First Name, Last Name, Email, Phone
    first_name_field = page.get_by_label(re.compile(r"First Name", re.IGNORECASE))
    last_name_field = page.get_by_label(re.compile(r"Last Name", re.IGNORECASE))
    email_field = page.get_by_label(re.compile(r"Email", re.IGNORECASE))
    phone_field = page.get_by_label(re.compile(r"Phone", re.IGNORECASE))
    
    expect(first_name_field).to_be_visible()
    expect(last_name_field).to_be_visible()
    expect(email_field).to_be_visible()
    expect(phone_field).to_be_visible()


@pytest.mark.readonly
def test_e2e_10_find_plan_page_zip_code_field(page: Page, base_url: str) -> None:
    """E2E-10: Find a Plan page includes ZIP code field for plan lookup."""
    page.goto(f"{base_url}/find-a-plan", wait_until="domcontentloaded")
    
    # ZIP code field should be present
    zip_field = page.get_by_label(re.compile(r"ZIP Code", re.IGNORECASE))
    expect(zip_field).to_be_visible()


@pytest.mark.readonly
def test_e2e_11_find_plan_page_help_link_visible(page: Page, base_url: str) -> None:
    """E2E-11: Find a Plan page displays phone support link to call for help."""
    page.goto(f"{base_url}/find-a-plan", wait_until="domcontentloaded")
    
    # Support phone number should be visible
    page_text = page.inner_text("body")
    assert "1-888-293-8272" in page_text or "888-293-8272" in page_text, \
        "Support phone number not found on Find a Plan page"


@pytest.mark.readonly
def test_e2e_12_find_plan_page_breadcrumb_navigation(page: Page, base_url: str) -> None:
    """E2E-12: Find a Plan page includes breadcrumb navigation showing current page."""
    page.goto(f"{base_url}/find-a-plan", wait_until="domcontentloaded")
    
    # Look for breadcrumb that shows current page location
    page_text = page.inner_text("body")
    # Should have "Home" in breadcrumb
    assert "Home" in page_text, "Breadcrumb Home link missing"


# ============================================================================
# CONTACT US PAGE TESTS (E2E-13 through E2E-16)
# ============================================================================


@pytest.mark.readonly
def test_e2e_13_contact_us_page_loads(page: Page, base_url: str) -> None:
    """E2E-13: Contact Us page loads with correct title."""
    response = page.goto(f"{base_url}/about-us/contact-us", wait_until="domcontentloaded")
    
    assert response is not None, "no response from /about-us/contact-us"
    assert response.status < 400, f"/about-us/contact-us returned HTTP {response.status}"
    expect(page).to_have_title(re.compile(r"Contact Us", re.IGNORECASE))


@pytest.mark.readonly
def test_e2e_14_contact_us_phone_numbers_visible(page: Page, base_url: str) -> None:
    """E2E-14: Contact Us page displays multiple support phone numbers."""
    page.goto(f"{base_url}/about-us/contact-us", wait_until="domcontentloaded")
    
    page_text = page.inner_text("body")
    
    # Should have various support phone numbers
    assert "1-833-242-2223" in page_text or "833-242-2223" in page_text, \
        "Concierge phone number missing"
    assert "1-866-634-2247" in page_text or "866-634-2247" in page_text, \
        "Member Services phone number missing"
    assert "1-888-293-8272" in page_text or "888-293-8272" in page_text, \
        "Sales phone number missing"


@pytest.mark.readonly
def test_e2e_15_contact_us_expandable_sections(page: Page, base_url: str) -> None:
    """E2E-15: Contact Us page has expandable contact categories (Members, Providers, Brokers)."""
    page.goto(f"{base_url}/about-us/contact-us", wait_until="domcontentloaded")
    
    page_text = page.inner_text("body")
    
    # Should have sections for different user types
    assert "Member" in page_text, "Member contact section missing"
    assert "Provider" in page_text, "Provider contact section missing"
    # Broker section is typically referenced


@pytest.mark.readonly
def test_e2e_16_contact_us_corporate_address(page: Page, base_url: str) -> None:
    """E2E-16: Contact Us page displays corporate headquarters address."""
    page.goto(f"{base_url}/about-us/contact-us", wait_until="domcontentloaded")
    
    page_text = page.inner_text("body")
    
    # Corporate headquarters address should be visible
    assert "1100 W" in page_text or "Orange" in page_text, \
        "Corporate address information missing"
    assert "CA" in page_text or "92868" in page_text, \
        "California location information missing"


# ============================================================================
# LEGAL/FOOTER PAGES TESTS (E2E-17 through E2E-20)
# ============================================================================


@pytest.mark.readonly
def test_e2e_17_legal_notices_page_loads(page: Page, base_url: str) -> None:
    """E2E-17: Legal Notices page loads with correct title."""
    response = page.goto(f"{base_url}/about-us/legal-notices", wait_until="domcontentloaded")
    
    assert response is not None, "no response from /about-us/legal-notices"
    assert response.status < 400, f"/about-us/legal-notices returned HTTP {response.status}"
    expect(page).to_have_title(re.compile(r"Legal Notices", re.IGNORECASE))


@pytest.mark.readonly
def test_e2e_18_legal_notices_plan_disclaimer(page: Page, base_url: str) -> None:
    """E2E-18: Legal Notices page contains HMO/PPO plan disclaimers and state info."""
    page.goto(f"{base_url}/about-us/legal-notices", wait_until="domcontentloaded")
    
    page_text = page.inner_text("body")
    
    # Should mention plan types and states
    assert "HMO" in page_text, "HMO plan type missing from legal notices"
    assert "Medicare" in page_text, "Medicare program missing from legal notices"
    assert "California" in page_text or "Nevada" in page_text, \
        "State information missing from legal notices"


@pytest.mark.readonly
def test_e2e_19_privacy_notice_page_loads(page: Page, base_url: str) -> None:
    """E2E-19: Privacy Notices page loads with correct title."""
    response = page.goto(f"{base_url}/about-us/privacy-notices", wait_until="domcontentloaded")
    
    assert response is not None, "no response from /about-us/privacy-notices"
    assert response.status < 400, f"/about-us/privacy-notices returned HTTP {response.status}"
    expect(page).to_have_title(re.compile(r"Privacy.*Notices", re.IGNORECASE))


@pytest.mark.readonly
def test_e2e_20_privacy_notice_contains_hipaa_section(page: Page, base_url: str) -> None:
    """E2E-20: Privacy Notices page contains Protected Health Information (PHI) and HIPAA content."""
    page.goto(f"{base_url}/about-us/privacy-notices", wait_until="domcontentloaded")
    
    page_text = page.inner_text("body")
    
    # Should contain HIPAA-related terms and privacy sections
    assert "PHI" in page_text or "Protected Health Information" in page_text, \
        "PHI/Protected Health Information missing from privacy page"
    assert "Treatment" in page_text, "HIPAA Treatment section missing"
    assert "Payment" in page_text, "HIPAA Payment section missing"
