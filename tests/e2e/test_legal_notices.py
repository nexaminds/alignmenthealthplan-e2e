"""Regression tests for Alignment Health Plan Legal Notices page."""

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


class TestLegalNoticesPageStructure:
    """Verify structure and content of the Legal Notices page."""

    def test_legal_notices_page_loads_with_correct_title(self, page_sync, base_url):
        """Legal Notices page loads and displays correct title."""
        page_sync.goto(f"{base_url}/about-us/legal-notices", wait_until="networkidle")
        assert page_sync.title() == "Legal Notices | Alignment Health Plan"

    def test_legal_notices_page_has_heading(self, page_sync, base_url):
        """Legal Notices page displays 'Legal Notices' heading."""
        page_sync.goto(f"{base_url}/about-us/legal-notices", wait_until="networkidle")
        h1 = page_sync.locator("h1").first
        assert h1.is_visible()
        assert "Legal Notices" in h1.text_content()

    def test_legal_notices_page_has_phone_number(self, page_sync, base_url):
        """Legal Notices page displays support phone number."""
        page_sync.goto(f"{base_url}/about-us/legal-notices", wait_until="networkidle")
        phone = page_sync.get_by_text("1-866-634-2247").first
        assert phone.is_visible()

    def test_legal_notices_page_has_enroll_link(self, page_sync, base_url):
        """Legal Notices page has 'Enroll Now' link."""
        page_sync.goto(f"{base_url}/about-us/legal-notices", wait_until="networkidle")
        enroll_link = page_sync.get_by_role("link", name="Enroll Now").first
        assert enroll_link.is_visible()

    def test_legal_notices_page_has_visit_us_link(self, page_sync, base_url):
        """Legal Notices page navigation includes 'Visit Us'."""
        page_sync.goto(f"{base_url}/about-us/legal-notices", wait_until="networkidle")
        link = page_sync.get_by_role("link", name="Visit Us")
        assert link.is_visible()

    def test_legal_notices_page_has_group_retiree_options_link(self, page_sync, base_url):
        """Legal Notices page navigation includes 'Group Retiree Options'."""
        page_sync.goto(f"{base_url}/about-us/legal-notices", wait_until="networkidle")
        link = page_sync.get_by_role("link", name="Group Retiree Options")
        assert link.is_visible()

    def test_legal_notices_page_has_shop_online_link(self, page_sync, base_url):
        """Legal Notices page navigation includes 'Shop Online' link."""
        page_sync.goto(f"{base_url}/about-us/legal-notices", wait_until="networkidle")
        shop_link = page_sync.get_by_role("link", name="Shop Online")
        assert shop_link.is_visible()
        href = shop_link.get_attribute("href")
        assert "/find-a-plan" in href

    def test_legal_notices_page_has_ways_to_enroll_link(self, page_sync, base_url):
        """Legal Notices page navigation includes 'Ways to Enroll'."""
        page_sync.goto(f"{base_url}/about-us/legal-notices", wait_until="networkidle")
        link = page_sync.get_by_role("link", name="Ways to Enroll")
        assert link.is_visible()
