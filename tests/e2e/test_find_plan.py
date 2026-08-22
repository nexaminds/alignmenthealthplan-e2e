"""Regression tests for Alignment Health Plan Find a Plan page."""

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


class TestFindAPlanPageStructure:
    """Verify structure and content of the Find a Plan page."""

    def test_find_plan_page_loads_with_correct_title(self, page_sync, base_url):
        """Find a Plan page loads and displays correct title."""
        page_sync.goto(f"{base_url}/find-a-plan/", wait_until="networkidle")
        assert page_sync.title() == "Find a Plan | Alignment Health Plan"

    def test_find_plan_page_displays_explore_plans_heading(self, page_sync, base_url):
        """Find a Plan page displays 'Explore Our Plans' section."""
        page_sync.goto(f"{base_url}/find-a-plan/", wait_until="networkidle")
        heading = page_sync.get_by_role("heading", name="Explore Our Plans")
        assert heading.is_visible()

    def test_find_plan_page_displays_help_contact_heading(self, page_sync, base_url):
        """Find a Plan page displays 'Need Help? Contact Us Today.' heading."""
        page_sync.goto(f"{base_url}/find-a-plan/", wait_until="networkidle")
        heading = page_sync.get_by_role("heading", name="Need Help? Contact Us Today.")
        assert heading.is_visible()

    def test_find_plan_page_displays_phone_link(self, page_sync, base_url):
        """Find a Plan page displays phone link in CTAbody."""
        page_sync.goto(f"{base_url}/find-a-plan/", wait_until="networkidle")
        phone = page_sync.get_by_role("link", name="1-888-293-8272").filter(has_text="TTY").first
        assert phone.is_visible()

    def test_find_plan_page_get_started_button(self, page_sync, base_url):
        """Find a Plan page has visible 'Get Started' button."""
        page_sync.goto(f"{base_url}/find-a-plan/", wait_until="networkidle")
        button = page_sync.get_by_role("button", name="Get Started")
        assert button.is_visible()

    def test_find_plan_page_navigation_has_shop_online(self, page_sync, base_url):
        """Find a Plan page navigation includes 'Shop Online' link to find-a-plan."""
        page_sync.goto(f"{base_url}/find-a-plan/", wait_until="networkidle")
        shop_link = page_sync.get_by_role("link", name="Shop Online")
        assert shop_link.is_visible()
        href = shop_link.get_attribute("href")
        assert "/find-a-plan" in href

    def test_find_plan_page_has_attend_seminar_link(self, page_sync, base_url):
        """Find a Plan page navigation includes 'Attend A Seminar' link."""
        page_sync.goto(f"{base_url}/find-a-plan/", wait_until="networkidle")
        seminar_link = page_sync.get_by_role("link", name="Attend A Seminar")
        assert seminar_link.is_visible()
        assert "attend-a-seminar" in seminar_link.get_attribute("href")

    def test_find_plan_page_navigation_has_ways_to_enroll(self, page_sync, base_url):
        """Find a Plan page navigation includes 'Ways to Enroll' link."""
        page_sync.goto(f"{base_url}/find-a-plan/", wait_until="networkidle")
        link = page_sync.get_by_role("link", name="Ways to Enroll")
        assert link.is_visible()
        assert "ways-to-enroll" in link.get_attribute("href")

    def test_find_plan_page_has_ways_to_enroll_link(self, page_sync, base_url):
        """Find a Plan page navigation includes 'Ways to Enroll' link."""
        page_sync.goto(f"{base_url}/find-a-plan/", wait_until="networkidle")
        link = page_sync.get_by_role("link", name="Ways to Enroll")
        assert link.is_visible()
        assert "ways-to-enroll" in link.get_attribute("href")
