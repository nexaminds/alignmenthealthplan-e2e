"""Comprehensive regression test suite for alignmenthealthplan.com.

Covers core user journeys and page structure across:
- Homepage (hero, navigation, CTAs)
- Find a Plan (plan discovery workflow)
- Contact Us (contact information and form)
- Legal and privacy pages (footer/compliance)

Naming convention: test_e2e_NN_<behavior>
Each test is a single assertion target with a descriptive name.
Read-only by default (@pytest.mark.readonly).
"""

import re

import pytest
from playwright.sync_api import Page, expect


class TestHomepage:
    """Homepage load, structure, and key elements."""

    @pytest.mark.readonly
    def test_e2e_02_homepage_title_contains_alignment_brand(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-02: Homepage title includes 'Alignment' brand name."""
        response = page.goto(base_url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400
        expect(page).to_have_title(re.compile(r"Alignment", re.IGNORECASE))

    @pytest.mark.readonly
    def test_e2e_03_homepage_h1_visible_and_contains_medicare_advantage(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-03: Homepage h1 is visible and mentions Medicare Advantage."""
        page.goto(base_url)
        h1 = page.locator("h1").first
        expect(h1).to_be_visible()
        text = h1.text_content()
        assert "medicare" in text.lower(), f"h1 text: {text}"
        assert "advantage" in text.lower(), f"h1 text: {text}"

    @pytest.mark.readonly
    def test_e2e_04_homepage_has_header_element(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-04: Homepage header element is present."""
        page.goto(base_url)
        header = page.locator("header")
        expect(header).to_be_visible()

    @pytest.mark.readonly
    def test_e2e_05_homepage_enroll_now_button_exists(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-05: Homepage has 'Enroll Now' CTA button."""
        page.goto(base_url)
        enroll_btn = page.get_by_text("Enroll Now")
        assert enroll_btn.count() > 0, "Should have Enroll Now button"

    @pytest.mark.readonly
    def test_e2e_06_homepage_footer_present_with_links(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-06: Homepage footer is rendered and contains navigation links."""
        page.goto(base_url)
        footer = page.locator("footer")
        expect(footer).to_be_visible()
        footer_links = footer.locator("a")
        link_count = footer_links.count()
        assert link_count > 0, "Footer should have navigation links"

    @pytest.mark.readonly
    def test_e2e_07_homepage_footer_has_legal_links(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-07: Homepage footer includes legal/compliance links."""
        page.goto(base_url)
        footer = page.locator("footer")
        # Look for common legal/privacy link texts using proper regex syntax
        legal_privacy_links = footer.get_by_text(re.compile(r"Legal|Privacy", re.IGNORECASE))
        assert (
            legal_privacy_links.count() > 0
        ), "Footer should have legal/privacy links"


class TestFindAPlanPage:
    """Find a Plan page structure and user flow."""

    @pytest.mark.readonly
    def test_e2e_08_find_plan_page_loads_with_200_status(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-08: Find a Plan page loads successfully."""
        url = f"{base_url}/find-a-plan"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400, f"GET {url} returned HTTP {response.status}"

    @pytest.mark.readonly
    def test_e2e_09_find_plan_page_title_correct(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-09: Find a Plan page title includes 'Plan'."""
        page.goto(f"{base_url}/find-a-plan")
        expect(page).to_have_title(re.compile(r"Plan", re.IGNORECASE))

    @pytest.mark.readonly
    def test_e2e_10_find_plan_page_has_main_heading(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-10: Find a Plan page has visible main heading."""
        page.goto(f"{base_url}/find-a-plan")
        # Find any heading (h2, h3, h4 since there may not be h1)
        heading = page.locator("h2, h3, h4").first
        expect(heading).to_be_visible()

    @pytest.mark.readonly
    def test_e2e_11_find_plan_page_form_visible(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-11: Find a Plan page contains a form element."""
        page.goto(f"{base_url}/find-a-plan")
        form = page.locator("form").first
        expect(form).to_be_visible()

    @pytest.mark.readonly
    def test_e2e_12_find_plan_page_header_accessible(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-12: Find a Plan page retains header element."""
        page.goto(f"{base_url}/find-a-plan")
        header = page.locator("header")
        expect(header).to_be_visible()

    @pytest.mark.readonly
    def test_e2e_13_find_plan_footer_contains_contact_link(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-13: Find a Plan page footer includes Contact Us link."""
        page.goto(f"{base_url}/find-a-plan")
        footer = page.locator("footer")
        contact_link = footer.get_by_text(re.compile(r"Contact Us", re.IGNORECASE))
        assert contact_link.count() > 0, "Footer should have Contact Us link"


class TestContactUsPage:
    """Contact Us page structure and content."""

    @pytest.mark.readonly
    def test_e2e_14_contact_page_loads_successfully(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-14: Contact Us page loads with 200 status."""
        url = f"{base_url}/about-us/contact-us"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400, f"GET {url} returned HTTP {response.status}"

    @pytest.mark.readonly
    def test_e2e_15_contact_page_title_contains_contact(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-15: Contact Us page title includes 'Contact'."""
        page.goto(f"{base_url}/about-us/contact-us")
        expect(page).to_have_title(re.compile(r"Contact", re.IGNORECASE))

    @pytest.mark.readonly
    def test_e2e_16_contact_page_h1_visible(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-16: Contact Us page h1 is visible."""
        page.goto(f"{base_url}/about-us/contact-us")
        h1 = page.locator("h1").first
        expect(h1).to_be_visible()
        assert "contact" in h1.text_content().lower()

    @pytest.mark.readonly
    def test_e2e_17_contact_page_contains_phone_information(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-17: Contact Us page displays phone contact method."""
        page.goto(f"{base_url}/about-us/contact-us")
        # Look for phone-related text (phone number or "Phone" label)
        phone_content = page.get_by_text(re.compile(r"\d{3}.*\d{4}|phone", re.IGNORECASE))
        assert phone_content.count() > 0, "Contact page should have phone information"

    @pytest.mark.readonly
    def test_e2e_18_contact_page_header_visible(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-18: Contact Us page retains main header."""
        page.goto(f"{base_url}/about-us/contact-us")
        header = page.locator("header")
        expect(header).to_be_visible()

    @pytest.mark.readonly
    def test_e2e_19_contact_page_has_form(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-19: Contact Us page contains at least one form."""
        page.goto(f"{base_url}/about-us/contact-us")
        forms = page.locator("form")
        assert forms.count() > 0, "Contact page should have a form"


class TestLegalPages:
    """Legal and privacy compliance pages."""

    @pytest.mark.readonly
    def test_e2e_20_legal_notices_page_loads_successfully(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-20: Legal Notices page loads with 200 status."""
        url = f"{base_url}/about-us/legal-notices"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400, f"GET {url} returned HTTP {response.status}"

    @pytest.mark.readonly
    def test_e2e_21_legal_notices_page_title_correct(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-21: Legal Notices page title includes 'Legal'."""
        page.goto(f"{base_url}/about-us/legal-notices")
        expect(page).to_have_title(re.compile(r"Legal", re.IGNORECASE))

    @pytest.mark.readonly
    def test_e2e_22_legal_notices_h1_visible(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-22: Legal Notices page h1 is visible."""
        page.goto(f"{base_url}/about-us/legal-notices")
        h1 = page.locator("h1").first
        expect(h1).to_be_visible()
        assert "legal" in h1.text_content().lower()

    @pytest.mark.readonly
    def test_e2e_23_privacy_notices_page_loads_successfully(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-23: Privacy Notices page loads with 200 status."""
        url = f"{base_url}/about-us/privacy-notices"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None
        assert response.status < 400, f"GET {url} returned HTTP {response.status}"

    @pytest.mark.readonly
    def test_e2e_24_privacy_notices_page_title_correct(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-24: Privacy Notices page title includes 'Privacy'."""
        page.goto(f"{base_url}/about-us/privacy-notices")
        expect(page).to_have_title(re.compile(r"Privacy", re.IGNORECASE))

    @pytest.mark.readonly
    def test_e2e_25_privacy_notices_h1_visible(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-25: Privacy Notices page h1 is visible."""
        page.goto(f"{base_url}/about-us/privacy-notices")
        h1 = page.locator("h1").first
        expect(h1).to_be_visible()
        assert "privacy" in h1.text_content().lower()

    @pytest.mark.readonly
    def test_e2e_26_legal_pages_retain_header(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-26: Legal/privacy pages retain visible header."""
        page.goto(f"{base_url}/about-us/legal-notices")
        header = page.locator("header")
        expect(header).to_be_visible()

    @pytest.mark.readonly
    def test_e2e_27_legal_pages_footer_accessible(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-27: Legal pages include footer with links."""
        page.goto(f"{base_url}/about-us/legal-notices")
        footer = page.locator("footer")
        expect(footer).to_be_visible()
        footer_links = footer.locator("a")
        assert footer_links.count() > 0, "Legal page footer should have navigation"


class TestPageConsistency:
    """Cross-page consistency and shared patterns."""

    @pytest.mark.readonly
    def test_e2e_28_homepage_and_find_plan_share_header(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-28: Homepage and Find a Plan use consistent header structure."""
        page.goto(base_url)
        home_header = page.locator("header").first
        home_header_visible = home_header.is_visible()

        page.goto(f"{base_url}/find-a-plan")
        plan_header = page.locator("header").first
        plan_header_visible = plan_header.is_visible()

        assert (
            home_header_visible == plan_header_visible
        ), "Header visibility should be consistent"

    @pytest.mark.readonly
    def test_e2e_29_all_pages_have_footer(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-29: All key pages include a footer element."""
        urls = [
            base_url,
            f"{base_url}/find-a-plan",
            f"{base_url}/about-us/contact-us",
            f"{base_url}/about-us/legal-notices",
        ]
        for url in urls:
            page.goto(url)
            footer = page.locator("footer")
            expect(footer).to_be_visible(timeout=5000)

    @pytest.mark.readonly
    def test_e2e_30_all_pages_return_http_200(
        self, page: Page, base_url: str
    ) -> None:
        """E2E-30: All key pages return HTTP 2xx status code."""
        urls = [
            base_url,
            f"{base_url}/find-a-plan",
            f"{base_url}/about-us/contact-us",
            f"{base_url}/about-us/legal-notices",
            f"{base_url}/about-us/privacy-notices",
        ]
        for url in urls:
            response = page.goto(url, wait_until="domcontentloaded")
            assert response is not None, f"No response from {url}"
            assert (
                response.status < 400
            ), f"GET {url} returned HTTP {response.status}"
