"""Regression tests for Alignment Health Plan Contact Us page."""

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


class TestContactUsPageStructure:
    """Verify structure and content of the Contact Us page."""

    def test_contact_us_page_loads_with_correct_title(self, page_sync, base_url):
        """Contact Us page loads and displays correct title."""
        page_sync.goto(f"{base_url}/about-us/contact-us", wait_until="networkidle")
        assert page_sync.title() == "Contact Us | Alignment Health Plan"

    def test_contact_us_page_has_contact_us_heading_exact(self, page_sync, base_url):
        """Contact Us page displays 'Contact Us' heading."""
        page_sync.goto(f"{base_url}/about-us/contact-us", wait_until="networkidle")
        h1 = page_sync.locator("h1").first
        assert h1.is_visible()
        assert "Contact Us" in h1.text_content()

    def test_contact_us_page_has_subheading(self, page_sync, base_url):
        """Contact Us page displays descriptive subheading."""
        page_sync.goto(f"{base_url}/about-us/contact-us", wait_until="networkidle")
        # Using locator that matches the h4 element
        subheading = page_sync.locator("h4").filter(has_text="ready to answer")
        assert subheading.is_visible()

    def test_contact_us_page_has_send_message_section(self, page_sync, base_url):
        """Contact Us page displays 'Send Us a Message' section."""
        page_sync.goto(f"{base_url}/about-us/contact-us", wait_until="networkidle")
        section = page_sync.get_by_role("heading", name="Send Us a Message")
        assert section.is_visible()

    def test_contact_us_page_member_category_exists(self, page_sync, base_url):
        """Contact Us page has 'Member' inquiry option."""
        page_sync.goto(f"{base_url}/about-us/contact-us", wait_until="networkidle")
        # Use text containing approach instead of exact role match
        member_section = page_sync.locator("text=I am a Member").first
        assert member_section.is_visible()

    def test_contact_us_page_provider_category_exists(self, page_sync, base_url):
        """Contact Us page has 'Provider' inquiry option."""
        page_sync.goto(f"{base_url}/about-us/contact-us", wait_until="networkidle")
        provider_section = page_sync.locator("text=I am a Provider").first
        assert provider_section.is_visible()

    def test_contact_us_page_broker_category_exists(self, page_sync, base_url):
        """Contact Us page has 'Broker' inquiry option."""
        page_sync.goto(f"{base_url}/about-us/contact-us", wait_until="networkidle")
        broker_section = page_sync.locator("text=I am a Broker").first
        assert broker_section.is_visible()

    def test_contact_us_page_other_inquiries_exists(self, page_sync, base_url):
        """Contact Us page has 'Other Inquiries' option."""
        page_sync.goto(f"{base_url}/about-us/contact-us", wait_until="networkidle")
        other_section = page_sync.locator("text=Other Inquiries").first
        assert other_section.is_visible()

    def test_contact_us_page_enroll_link(self, page_sync, base_url):
        """Contact Us page has 'Enroll Now' link in navigation."""
        page_sync.goto(f"{base_url}/about-us/contact-us", wait_until="networkidle")
        enroll_link = page_sync.get_by_role("link", name="Enroll Now").first
        assert enroll_link.is_visible()

    def test_contact_us_page_has_ways_to_enroll_link(self, page_sync, base_url):
        """Contact Us page navigation includes 'Ways to Enroll'."""
        page_sync.goto(f"{base_url}/about-us/contact-us", wait_until="networkidle")
        link = page_sync.get_by_role("link", name="Ways to Enroll")
        assert link.is_visible()
        assert "ways-to-enroll" in link.get_attribute("href")

    def test_contact_us_page_has_attend_seminar_link(self, page_sync, base_url):
        """Contact Us page navigation includes 'Attend A Seminar'."""
        page_sync.goto(f"{base_url}/about-us/contact-us", wait_until="networkidle")
        link = page_sync.get_by_role("link", name="Attend A Seminar")
        assert link.is_visible()
