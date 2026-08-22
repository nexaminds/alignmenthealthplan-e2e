"""Regression tests for Alignment Health Plan Terms of Use page."""

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def browser_sync():
    """Create a sync browser instance."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()


@pytest.fixture
def page_sync(browser_sync, base_url):
    """Create a page with TLS error tolerance."""
    context = browser_sync.new_context(ignore_https_errors=True)
    page = context.new_page()
    yield page
    page.close()
    context.close()


class TestTermsOfUsePageStructure:
    """Verify structure and content of the Terms of Use page."""

    def test_terms_of_use_page_loads_with_correct_title(self, page_sync, base_url):
        """Terms of Use page loads and displays correct title."""
        page_sync.goto(f"{base_url}/about-us/terms-of-use", wait_until="networkidle")
        assert page_sync.title() == "Terms of Use | Alignment Health Plan"

    def test_terms_of_use_page_has_main_heading_exact(self, page_sync, base_url):
        """Terms of Use page displays 'Terms of Use' heading."""
        page_sync.goto(f"{base_url}/about-us/terms-of-use", wait_until="networkidle")
        h1 = page_sync.locator("h1").first
        assert h1.is_visible()
        assert "Terms of Use" in h1.text_content()

    def test_terms_of_use_page_has_intro_text(self, page_sync, base_url):
        """Terms of Use page has introductory text."""
        page_sync.goto(f"{base_url}/about-us/terms-of-use", wait_until="networkidle")
        intro = page_sync.locator("h2").filter(has_text="Please read these terms")
        assert intro.is_visible()

    def test_terms_of_use_page_has_full_terms_section(self, page_sync, base_url):
        """Terms of Use page has 'Full terms of use' section."""
        page_sync.goto(f"{base_url}/about-us/terms-of-use", wait_until="networkidle")
        section = page_sync.get_by_role("heading", name="Full terms of use")
        assert section.is_visible()

    def test_terms_of_use_page_has_privacy_policy_section(self, page_sync, base_url):
        """Terms of Use page has 'Privacy Policy' section."""
        page_sync.goto(f"{base_url}/about-us/terms-of-use", wait_until="networkidle")
        section = page_sync.get_by_role("heading", name="Privacy Policy")
        assert section.is_visible()

    def test_terms_of_use_page_has_nondiscrimination_section(self, page_sync, base_url):
        """Terms of Use page has 'Nondiscrimination Policy' section."""
        page_sync.goto(f"{base_url}/about-us/terms-of-use", wait_until="networkidle")
        section = page_sync.get_by_role("heading", name="Nondiscrimination Policy")
        assert section.is_visible()

    def test_terms_of_use_page_has_social_media_section(self, page_sync, base_url):
        """Terms of Use page has 'Social Media Policy' section."""
        page_sync.goto(f"{base_url}/about-us/terms-of-use", wait_until="networkidle")
        section = page_sync.get_by_role("heading", name="Social Media Policy")
        assert section.is_visible()

    def test_terms_of_use_page_has_sms_terms_section(self, page_sync, base_url):
        """Terms of Use page has 'SMS Terms and Conditions' section."""
        page_sync.goto(f"{base_url}/about-us/terms-of-use", wait_until="networkidle")
        section = page_sync.get_by_role("heading", name="SMS Terms and Conditions")
        assert section.is_visible()

    def test_terms_of_use_page_has_read_more_buttons(self, page_sync, base_url):
        """Terms of Use page has multiple 'Read More' buttons/links."""
        page_sync.goto(f"{base_url}/about-us/terms-of-use", wait_until="networkidle")
        read_more = page_sync.get_by_role("link", name="Read More")
        assert read_more.count() > 0
        assert read_more.first.is_visible()

    def test_terms_of_use_page_has_shop_online_link(self, page_sync, base_url):
        """Terms of Use page navigation includes 'Shop Online' link."""
        page_sync.goto(f"{base_url}/about-us/terms-of-use", wait_until="networkidle")
        shop_link = page_sync.get_by_role("link", name="Shop Online")
        assert shop_link.is_visible()
        href = shop_link.get_attribute("href")
        assert "/find-a-plan" in href

    def test_terms_of_use_page_has_ways_to_enroll_link(self, page_sync, base_url):
        """Terms of Use page navigation includes 'Ways to Enroll'."""
        page_sync.goto(f"{base_url}/about-us/terms-of-use", wait_until="networkidle")
        link = page_sync.get_by_role("link", name="Ways to Enroll")
        assert link.is_visible()

    def test_terms_of_use_page_has_enroll_link(self, page_sync, base_url):
        """Terms of Use page has 'Enroll Now' link."""
        page_sync.goto(f"{base_url}/about-us/terms-of-use", wait_until="networkidle")
        enroll_link = page_sync.get_by_role("link", name="Enroll Now").first
        assert enroll_link.is_visible()

    def test_terms_of_use_page_has_attend_seminar_link(self, page_sync, base_url):
        """Terms of Use page navigation includes 'Attend A Seminar'."""
        page_sync.goto(f"{base_url}/about-us/terms-of-use", wait_until="networkidle")
        link = page_sync.get_by_role("link", name="Attend A Seminar")
        assert link.is_visible()

    def test_terms_of_use_page_has_visit_us_link(self, page_sync, base_url):
        """Terms of Use page navigation includes 'Visit Us'."""
        page_sync.goto(f"{base_url}/about-us/terms-of-use", wait_until="networkidle")
        link = page_sync.get_by_role("link", name="Visit Us")
        assert link.is_visible()
