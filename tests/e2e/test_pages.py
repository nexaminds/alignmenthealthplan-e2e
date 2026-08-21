"""Key page navigation tests.

Tests loading and content validation for major public pages.
"""

import re
import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_21_why_alignment_loads(page: Page, base_url: str) -> None:
    """E2E-21: Why Alignment Health Plan page loads with expected content."""
    page.goto(f"{base_url}/discover-ahp/why-alignment-health-plan")
    
    expect(page).to_have_title(re.compile(r"Why.*Alignment"))
    expect(page.locator("text=senior-first")).to_be_visible()


@pytest.mark.readonly
def test_e2e_22_medicare_advantage_page_loads(page: Page, base_url: str) -> None:
    """E2E-22: Medicare Advantage overview page loads with explanation content."""
    page.goto(f"{base_url}/discover-ahp/medicare-advantage-plans")
    
    expect(page).to_have_title(re.compile(r"Medicare Advantage"))
    expect(page.locator("text=Medicare Advantage")).to_be_visible()


@pytest.mark.readonly
def test_e2e_23_faq_page_loads(page: Page, base_url: str) -> None:
    """E2E-23: Medicare Advantage FAQ page loads with Q&A content."""
    page.goto(f"{base_url}/discover-ahp/medicare-advantage-frequently-asked-questions")
    
    expect(page).to_have_title(re.compile(r"[Ff]requently.*[Aa]sked|FAQ"))
    
    # Should have FAQ content
    faq_text = page.content()
    assert "question" in faq_text.lower() or "answer" in faq_text.lower()


@pytest.mark.readonly
def test_e2e_24_find_a_plan_page_loads(page: Page, base_url: str) -> None:
    """E2E-24: Find a Plan page loads with plan selection interface."""
    page.goto(f"{base_url}/find-a-plan")
    
    expect(page).to_have_title(re.compile(r"[Pp]lan"))
    
    # Should have location entry interface
    expect(page.locator("text=Zip code").first).to_be_visible()


@pytest.mark.readonly
def test_e2e_25_ways_to_enroll_page(page: Page, base_url: str) -> None:
    """E2E-25: Ways to Enroll page provides enrollment options."""
    page.goto(f"{base_url}/find-plans/ways-to-enroll")
    
    expect(page).to_have_title(re.compile(r"Enroll"))
    
    # Should describe different enrollment methods
    expect(page.locator("text=Enroll")).to_be_visible()


@pytest.mark.readonly
def test_e2e_26_seminar_page_loads(page: Page, base_url: str) -> None:
    """E2E-26: Seminar/Event page loads with search functionality."""
    page.goto(f"{base_url}/find-plans/attend-a-seminar")
    
    expect(page).to_have_title(re.compile(r"[Ss]eminar|[Ee]vent"))


@pytest.mark.readonly
def test_e2e_27_benefit_highlights_page(page: Page, base_url: str) -> None:
    """E2E-27: Benefit Highlights page displays plan benefits comparison."""
    page.goto(f"{base_url}/find-plans/benefit-highlights")
    
    expect(page).to_have_title(re.compile(r"Benefit"))
    
    # Should show benefit information
    benefits_text = page.content()
    assert "benefit" in benefits_text.lower()


@pytest.mark.readonly
def test_e2e_28_pre_enrollment_kit_page(page: Page, base_url: str) -> None:
    """E2E-28: Pre-Enrollment Kit page provides downloadable resources."""
    page.goto(f"{base_url}/find-plans/ways-to-enroll/pre-enrollment-kit")
    
    expect(page).to_have_title(re.compile(r"[Kk]it|[Rr]esource"))


@pytest.mark.readonly
def test_e2e_29_group_retiree_options_page(page: Page, base_url: str) -> None:
    """E2E-29: Group Retiree Options page loads."""
    page.goto(f"{base_url}/find-plans/group-retiree-options")
    
    response = page.goto(f"{base_url}/find-plans/group-retiree-options", wait_until="domcontentloaded")
    assert response.status < 400


@pytest.mark.readonly
def test_e2e_30_part_d_faq_page(page: Page, base_url: str) -> None:
    """E2E-30: Medicare Part D FAQ page loads with drug coverage info."""
    page.goto(f"{base_url}/find-plans/part-d-faqs")
    
    expect(page).to_have_title(re.compile(r"[Pp]art D|[Dd]rug"))


@pytest.mark.readonly
def test_e2e_31_find_drug_page(page: Page, base_url: str) -> None:
    """E2E-31: Find a Drug page loads with search interface."""
    page.goto(f"{base_url}/find-care/find-a-drug")
    
    expect(page).to_have_title(re.compile(r"[Dd]rug|[Mm]edication"))


@pytest.mark.readonly
def test_e2e_32_find_pharmacy_page(page: Page, base_url: str) -> None:
    """E2E-32: Find a Pharmacy page loads with search functionality."""
    page.goto(f"{base_url}/find-care/find-a-pharmacy")
    
    expect(page).to_have_title(re.compile(r"[Pp]harmacy"))


@pytest.mark.readonly
def test_e2e_33_find_care_center_page(page: Page, base_url: str) -> None:
    """E2E-33: Find Care Centers page loads with center search."""
    page.goto(f"{base_url}/find-care/find-a-care-center")
    
    response = page.goto(f"{base_url}/find-care/find-a-care-center", wait_until="domcontentloaded")
    assert response.status < 400


@pytest.mark.readonly
def test_e2e_34_transportation_page(page: Page, base_url: str) -> None:
    """E2E-34: Transportation page loads with scheduling options."""
    page.goto(f"{base_url}/find-care/schedule-transportation")
    
    expect(page).to_have_title(re.compile(r"[Tt]ransport"))


@pytest.mark.readonly
def test_e2e_35_member_services_page(page: Page, base_url: str) -> None:
    """E2E-35: Member Services page provides member support information."""
    page.goto(f"{base_url}/members/member-services")
    
    expect(page).to_have_title(re.compile(r"[Mm]ember"))


@pytest.mark.readonly
def test_e2e_36_provider_resources_page(page: Page, base_url: str) -> None:
    """E2E-36: Provider Resources page loads for healthcare providers."""
    page.goto(f"{base_url}/providers/provider-resources")
    
    expect(page).to_have_title(re.compile(r"[Pp]rovider"))


@pytest.mark.readonly
def test_e2e_37_contact_us_page(page: Page, base_url: str) -> None:
    """E2E-37: Contact Us page loads with contact methods."""
    page.goto(f"{base_url}/about-us/contact-us")
    
    expect(page).to_have_title(re.compile(r"[Cc]ontact"))
    
    # Should have phone number
    expect(page.locator("text=1-888")).to_be_visible()


@pytest.mark.readonly
def test_e2e_38_legal_notices_page(page: Page, base_url: str) -> None:
    """E2E-38: Legal Notices page loads with compliance information."""
    page.goto(f"{base_url}/about-us/legal-notices")
    
    response = page.goto(f"{base_url}/about-us/legal-notices", wait_until="domcontentloaded")
    assert response.status < 400


@pytest.mark.readonly
def test_e2e_39_privacy_page(page: Page, base_url: str) -> None:
    """E2E-39: Privacy Notices page loads with privacy policy."""
    page.goto(f"{base_url}/about-us/privacy-notices")
    
    response = page.goto(f"{base_url}/about-us/privacy-notices", wait_until="domcontentloaded")
    assert response.status < 400


@pytest.mark.readonly
def test_e2e_40_terms_of_use_page(page: Page, base_url: str) -> None:
    """E2E-40: Terms of Use page loads with service terms."""
    page.goto(f"{base_url}/about-us/terms-of-use")
    
    expect(page).to_have_title(re.compile(r"[Tt]erms"))
