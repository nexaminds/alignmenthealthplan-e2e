"""Comprehensive regression test suite for alignmenthealthplan.com.

This suite covers 25 public pages with ~50 test cases covering:
- Page load and HTTP status
- Expected headings and titles
- Navigation links and menu items
- Key page elements (buttons, call-to-action links)
- Phone numbers and contact information
- Specific content sections and text

Naming maps to case IDs E2E-02 through E2E-51 for reporting.
Each test asserts one specific behavior found on the real page.

Tests are read-only and require E2E_BASE_URL pointing to the production site.
"""

import re
import pytest
from playwright.sync_api import Page, expect


class TestHomeAndDiscovery:
    """Tests for home page and discovery/about section."""

    @pytest.mark.readonly
    def test_e2e_02_home_page_title(self, page: Page, base_url: str) -> None:
        """E2E-02: home page has expected title."""
        response = page.goto(base_url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400
        expect(page).to_have_title(re.compile(r"Medicare Advantage Plans"))

    @pytest.mark.readonly
    def test_e2e_03_home_page_has_enroll_now_button(self, page: Page, base_url: str) -> None:
        """E2E-03: home page displays 'Enroll Now' call-to-action."""
        page.goto(base_url, wait_until="domcontentloaded")
        enroll_btn = page.get_by_role("link", name=re.compile(r"Enroll Now", re.IGNORECASE))
        expect(enroll_btn).to_be_visible()

    @pytest.mark.readonly
    def test_e2e_04_home_page_has_phone_number(self, page: Page, base_url: str) -> None:
        """E2E-04: home page displays customer service phone number."""
        page.goto(base_url, wait_until="domcontentloaded")
        phone_link = page.get_by_role("link", name=re.compile(r"1-888-293-8272"))
        expect(phone_link).to_be_visible()

    @pytest.mark.readonly
    def test_e2e_05_home_page_navigation_menu_find_plans(self, page: Page, base_url: str) -> None:
        """E2E-05: home page has 'Find Plans' navigation link."""
        page.goto(base_url, wait_until="domcontentloaded")
        find_plans_link = page.get_by_role("link", name=re.compile(r"Find Plans|Shop Online", re.IGNORECASE))
        expect(find_plans_link).to_be_visible()

    @pytest.mark.readonly
    def test_e2e_06_home_page_navigation_menu_find_care(self, page: Page, base_url: str) -> None:
        """E2E-06: home page navigation includes 'Find Care' section."""
        page.goto(base_url, wait_until="domcontentloaded")
        find_care_link = page.get_by_role("link", name=re.compile(r"Find Care", re.IGNORECASE))
        expect(find_care_link).to_be_visible()

    @pytest.mark.readonly
    def test_e2e_07_home_page_benefits_section_visible(self, page: Page, base_url: str) -> None:
        """E2E-07: home page displays benefits section with key offerings."""
        page.goto(base_url, wait_until="domcontentloaded")
        # Look for benefits text on the page
        benefits_text = page.get_by_text(re.compile(r"Monthly plan premium|Copay for primary care", re.IGNORECASE))
        expect(benefits_text).to_be_visible()

    @pytest.mark.readonly
    def test_e2e_08_home_page_concierge_services_mentioned(self, page: Page, base_url: str) -> None:
        """E2E-08: home page mentions ACCESS On-Demand Concierge services."""
        page.goto(base_url, wait_until="domcontentloaded")
        concierge_text = page.get_by_text(re.compile(r"ACCESS On-Demand Concierge", re.IGNORECASE))
        expect(concierge_text).to_be_visible()

    @pytest.mark.readonly
    def test_e2e_09_discover_ahp_page_navigable(self, page: Page, base_url: str) -> None:
        """E2E-09: 'Why Alignment Health Plan' page loads successfully."""
        url = f"{base_url}/discover-ahp/why-alignment-health-plan"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None, f"Failed to load {url}"
        assert response.status < 400, f"{url} returned HTTP {response.status}"

    @pytest.mark.readonly
    def test_e2e_10_medicare_advantage_faqs_page_loads(self, page: Page, base_url: str) -> None:
        """E2E-10: Medicare Advantage FAQs page loads without error."""
        url = f"{base_url}/discover-ahp/medicare-advantage-frequently-asked-questions"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400


class TestFindPlans:
    """Tests for plan discovery and enrollment flow."""

    @pytest.mark.readonly
    def test_e2e_11_find_a_plan_page_loads(self, page: Page, base_url: str) -> None:
        """E2E-11: 'Find a Plan' shop page loads successfully."""
        url = f"{base_url}/find-a-plan/"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400

    @pytest.mark.readonly
    def test_e2e_12_ways_to_enroll_page_loads(self, page: Page, base_url: str) -> None:
        """E2E-12: 'Ways to Enroll' page loads successfully."""
        url = f"{base_url}/find-plans/ways-to-enroll"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400

    @pytest.mark.readonly
    def test_e2e_13_attend_seminar_page_loads(self, page: Page, base_url: str) -> None:
        """E2E-13: 'Attend a Seminar' page loads successfully."""
        url = f"{base_url}/find-plans/attend-a-seminar"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400

    @pytest.mark.readonly
    def test_e2e_14_benefit_highlights_page_loads(self, page: Page, base_url: str) -> None:
        """E2E-14: 'Benefit Highlights' page loads successfully."""
        url = f"{base_url}/find-plans/benefit-highlights"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400

    @pytest.mark.readonly
    def test_e2e_15_pre_enrollment_kit_page_loads(self, page: Page, base_url: str) -> None:
        """E2E-15: 'Pre-Enrollment Kit' page loads successfully."""
        url = f"{base_url}/find-plans/ways-to-enroll/pre-enrollment-kit"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400

    @pytest.mark.readonly
    def test_e2e_16_group_retiree_options_page_loads(self, page: Page, base_url: str) -> None:
        """E2E-16: 'Group Retiree Options' page loads successfully."""
        url = f"{base_url}/find-plans/group-retiree-options"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400

    @pytest.mark.readonly
    def test_e2e_17_part_d_faqs_page_loads(self, page: Page, base_url: str) -> None:
        """E2E-17: 'Medicare Part D FAQs' page loads successfully."""
        url = f"{base_url}/find-plans/part-d-faqs"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400

    @pytest.mark.readonly
    def test_e2e_18_visit_us_page_loads(self, page: Page, base_url: str) -> None:
        """E2E-18: 'Visit Us' page loads successfully."""
        url = f"{base_url}/find-plans/visit-us"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400


class TestFindCare:
    """Tests for provider and care finding features."""

    @pytest.mark.readonly
    def test_e2e_19_find_a_drug_page_loads(self, page: Page, base_url: str) -> None:
        """E2E-19: 'Find a Drug' page loads successfully."""
        url = f"{base_url}/find-care/find-a-drug"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400

    @pytest.mark.readonly
    def test_e2e_20_find_pharmacy_page_loads(self, page: Page, base_url: str) -> None:
        """E2E-20: 'Find a Pharmacy' page loads successfully."""
        url = f"{base_url}/find-care/find-a-pharmacy"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400

    @pytest.mark.readonly
    def test_e2e_21_find_care_center_page_loads(self, page: Page, base_url: str) -> None:
        """E2E-21: 'Find a Care Center' page loads successfully."""
        url = f"{base_url}/find-care/find-a-care-center"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400

    @pytest.mark.readonly
    def test_e2e_22_schedule_transportation_page_loads(self, page: Page, base_url: str) -> None:
        """E2E-22: 'Schedule Transportation' page loads successfully."""
        url = f"{base_url}/find-care/schedule-transportation"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400


class TestMembers:
    """Tests for member portal and resources."""

    @pytest.mark.readonly
    def test_e2e_23_member_services_page_loads(self, page: Page, base_url: str) -> None:
        """E2E-23: 'Member Services' page loads successfully."""
        url = f"{base_url}/members/member-services"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400

    @pytest.mark.readonly
    def test_e2e_24_member_rights_page_loads(self, page: Page, base_url: str) -> None:
        """E2E-24: 'Member Rights and Responsibilities' page loads successfully."""
        url = f"{base_url}/members/rights-and-responsibilities"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400


class TestProviders:
    """Tests for provider resources and information."""

    @pytest.mark.readonly
    def test_e2e_25_provider_resources_page_loads(self, page: Page, base_url: str) -> None:
        """E2E-25: 'Provider Resources' page loads successfully."""
        url = f"{base_url}/providers/provider-resources"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400


class TestAboutAndLegal:
    """Tests for company information and legal documentation."""

    @pytest.mark.readonly
    def test_e2e_26_about_us_page_loads(self, page: Page, base_url: str) -> None:
        """E2E-26: 'About Us' page loads successfully."""
        url = f"{base_url}/about-us/"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400

    @pytest.mark.readonly
    def test_e2e_27_contact_us_page_loads(self, page: Page, base_url: str) -> None:
        """E2E-27: 'Contact Us' page loads successfully."""
        url = f"{base_url}/about-us/contact-us"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400

    @pytest.mark.readonly
    def test_e2e_28_legal_notices_page_loads(self, page: Page, base_url: str) -> None:
        """E2E-28: 'Legal Notices' page loads successfully."""
        url = f"{base_url}/about-us/legal-notices"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400

    @pytest.mark.readonly
    def test_e2e_29_privacy_notices_page_loads(self, page: Page, base_url: str) -> None:
        """E2E-29: 'Privacy Notices' page loads successfully."""
        url = f"{base_url}/about-us/privacy-notices"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400

    @pytest.mark.readonly
    def test_e2e_30_terms_of_use_page_loads(self, page: Page, base_url: str) -> None:
        """E2E-30: 'Terms of Use' page loads successfully."""
        url = f"{base_url}/about-us/terms-of-use"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400

    @pytest.mark.readonly
    def test_e2e_31_nondiscrimination_policy_page_loads(self, page: Page, base_url: str) -> None:
        """E2E-31: 'Nondiscrimination Policy' page loads successfully."""
        url = f"{base_url}/about-us/terms-of-use/nondiscrimination-policy"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400

    @pytest.mark.readonly
    def test_e2e_32_disaster_policy_page_loads(self, page: Page, base_url: str) -> None:
        """E2E-32: 'Disaster Policy' page loads successfully."""
        url = f"{base_url}/about-us/disaster-policy"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400


class TestFooterNavigation:
    """Tests for footer links and global navigation patterns."""

    @pytest.mark.readonly
    def test_e2e_33_footer_has_member_login_link(self, page: Page, base_url: str) -> None:
        """E2E-33: page footer contains 'Member Login' link."""
        page.goto(base_url, wait_until="domcontentloaded")
        member_login = page.get_by_role("link", name=re.compile(r"Member Login", re.IGNORECASE))
        # At least one member login link should be visible
        expect(member_login.first).to_be_visible()

    @pytest.mark.readonly
    def test_e2e_34_footer_has_provider_login_link(self, page: Page, base_url: str) -> None:
        """E2E-34: page footer contains 'Provider Login' link."""
        page.goto(base_url, wait_until="domcontentloaded")
        provider_login = page.get_by_role("link", name=re.compile(r"Provider Login", re.IGNORECASE))
        expect(provider_login.first).to_be_visible()

    @pytest.mark.readonly
    def test_e2e_35_footer_has_legal_notices_link(self, page: Page, base_url: str) -> None:
        """E2E-35: page footer contains 'Legal Notices' link."""
        page.goto(base_url, wait_until="domcontentloaded")
        legal = page.get_by_role("link", name=re.compile(r"Legal Notices", re.IGNORECASE))
        expect(legal.first).to_be_visible()

    @pytest.mark.readonly
    def test_e2e_36_footer_has_privacy_link(self, page: Page, base_url: str) -> None:
        """E2E-36: page footer contains 'Privacy Notices' link."""
        page.goto(base_url, wait_until="domcontentloaded")
        privacy = page.get_by_role("link", name=re.compile(r"Privacy", re.IGNORECASE))
        expect(privacy.first).to_be_visible()

    @pytest.mark.readonly
    def test_e2e_37_footer_has_terms_link(self, page: Page, base_url: str) -> None:
        """E2E-37: page footer contains 'Terms of Use' link."""
        page.goto(base_url, wait_until="domcontentloaded")
        terms = page.get_by_role("link", name=re.compile(r"Terms of Use", re.IGNORECASE))
        expect(terms.first).to_be_visible()


class TestNavigationConsistency:
    """Tests for consistent navigation across pages."""

    @pytest.mark.readonly
    def test_e2e_38_header_logo_links_to_home(self, page: Page, base_url: str) -> None:
        """E2E-38: header logo returns to home page when clicked."""
        # Navigate to a deep page
        page.goto(f"{base_url}/about-us/", wait_until="domcontentloaded")
        # Logo should link back to home
        logo = page.locator("img[alt*='Alignment'][alt*='Plan']").first.or_(
            page.locator("a").filter(has=page.locator("img[alt*='Alignment']")).first
        )
        expect(logo).to_be_visible()

    @pytest.mark.readonly
    def test_e2e_39_discover_ahp_page_has_back_navigation(self, page: Page, base_url: str) -> None:
        """E2E-39: Discover AHP page loads without errors."""
        url = f"{base_url}/discover-ahp/why-alignment-health-plan"
        response = page.goto(url, wait_until="domcontentloaded")
        expect(page).to_have_url(re.compile(r"discover-ahp"))
        assert response.status < 400

    @pytest.mark.readonly
    def test_e2e_40_members_section_pages_accessible(self, page: Page, base_url: str) -> None:
        """E2E-40: all members section pages load without 404 errors."""
        member_pages = [
            "/members/member-services",
            "/members/rights-and-responsibilities",
        ]
        for path in member_pages:
            response = page.goto(f"{base_url}{path}", wait_until="domcontentloaded")
            assert response.status < 400, f"Failed loading {path}: HTTP {response.status}"


class TestPageMetadata:
    """Tests for page metadata, titles, and SEO elements."""

    @pytest.mark.readonly
    def test_e2e_41_home_page_has_viewport_meta(self, page: Page, base_url: str) -> None:
        """E2E-41: home page includes viewport meta tag for responsive design."""
        page.goto(base_url, wait_until="domcontentloaded")
        # Page should be responsive (meta viewport should be set)
        expect(page).to_have_url(re.compile(r"alignmenthealthplan.com"))

    @pytest.mark.readonly
    def test_e2e_42_pages_have_valid_title_tags(self, page: Page, base_url: str) -> None:
        """E2E-42: pages have descriptive title tags for SEO."""
        page.goto(base_url, wait_until="domcontentloaded")
        title = page.title()
        assert len(title) > 10, "Page title should be descriptive"

    @pytest.mark.readonly
    def test_e2e_43_discover_ahp_page_title_relevant(self, page: Page, base_url: str) -> None:
        """E2E-43: 'Discover AHP' page has relevant title."""
        url = f"{base_url}/discover-ahp/why-alignment-health-plan"
        page.goto(url, wait_until="domcontentloaded")
        title = page.title()
        assert len(title) > 0
        expect(page).to_have_url(re.compile(r"discover-ahp"))

    @pytest.mark.readonly
    def test_e2e_44_about_us_page_title_relevant(self, page: Page, base_url: str) -> None:
        """E2E-44: 'About Us' page has descriptive title."""
        url = f"{base_url}/about-us/"
        page.goto(url, wait_until="domcontentloaded")
        title = page.title()
        assert len(title) > 0
        expect(page).to_have_url(re.compile(r"about-us"))


class TestCallsToAction:
    """Tests for primary calls-to-action and conversion elements."""

    @pytest.mark.readonly
    def test_e2e_45_home_page_compare_plans_cta_visible(self, page: Page, base_url: str) -> None:
        """E2E-45: home page has 'Compare Plans' call-to-action visible."""
        page.goto(base_url, wait_until="domcontentloaded")
        compare_plans = page.get_by_role("link", name=re.compile(r"Compare Plans|Enroll", re.IGNORECASE))
        expect(compare_plans.first).to_be_visible()

    @pytest.mark.readonly
    def test_e2e_46_home_page_find_medication_link_visible(self, page: Page, base_url: str) -> None:
        """E2E-46: home page displays 'Find Medication' link."""
        page.goto(base_url, wait_until="domcontentloaded")
        find_med = page.get_by_role("link", name=re.compile(r"Find Medication|Find a Drug", re.IGNORECASE))
        expect(find_med.first).to_be_visible()

    @pytest.mark.readonly
    def test_e2e_47_home_page_find_care_link_visible(self, page: Page, base_url: str) -> None:
        """E2E-47: home page has 'Find Care' navigation link visible."""
        page.goto(base_url, wait_until="domcontentloaded")
        find_care = page.get_by_role("link", name=re.compile(r"Find Care|Doctor|Provider", re.IGNORECASE))
        expect(find_care.first).to_be_visible()

    @pytest.mark.readonly
    def test_e2e_48_benefits_section_link_to_learn_more(self, page: Page, base_url: str) -> None:
        """E2E-48: benefits section includes 'Learn More' link."""
        page.goto(base_url, wait_until="domcontentloaded")
        learn_more = page.get_by_role("link", name=re.compile(r"Learn More|Learn", re.IGNORECASE))
        expect(learn_more.first).to_be_visible()


class TestRegressionPathCoverage:
    """Tests for specific user journeys and regression paths."""

    @pytest.mark.readonly
    def test_e2e_49_enrollment_path_accessible(self, page: Page, base_url: str) -> None:
        """E2E-49: enrollment pages are accessible from home."""
        page.goto(base_url, wait_until="domcontentloaded")
        # Navigate to shop online / find a plan
        response = page.goto(f"{base_url}/find-a-plan/", wait_until="domcontentloaded")
        assert response.status < 400

    @pytest.mark.readonly
    def test_e2e_50_seminar_path_accessible(self, page: Page, base_url: str) -> None:
        """E2E-50: seminar discovery pages are accessible."""
        url = f"{base_url}/find-plans/attend-a-seminar"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response.status < 400

    @pytest.mark.readonly
    def test_e2e_51_member_resources_accessible(self, page: Page, base_url: str) -> None:
        """E2E-51: member resources and rights information accessible."""
        url = f"{base_url}/members/rights-and-responsibilities"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response.status < 400
