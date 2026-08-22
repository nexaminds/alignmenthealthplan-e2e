"""Regression tests for Alignment Health Plan homepage."""

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


class TestHomepageStructure:
    """Verify core structure and content of the homepage."""

    def test_homepage_loads_with_correct_title(self, page_sync, base_url):
        """Homepage loads and displays correct page title."""
        page_sync.goto(f"{base_url}/", wait_until="networkidle")
        assert page_sync.title() == "Medicare Advantage Plans that Put You First | Alignment Health Plan"

    def test_homepage_has_main_heading(self, page_sync, base_url):
        """Homepage displays the main value proposition heading."""
        page_sync.goto(f"{base_url}/", wait_until="networkidle")
        h1 = page_sync.locator("h1").first
        assert h1.is_visible()
        h1_text = h1.text_content().strip()
        assert "MEDICARE ADVANTAGE" in h1_text
        assert "PUT" in h1_text and "YOU FIRST" in h1_text

    def test_homepage_has_help_section_heading(self, page_sync, base_url):
        """Homepage displays 'How Can We Help You Today?' section."""
        page_sync.goto(f"{base_url}/", wait_until="networkidle")
        heading = page_sync.get_by_role("heading", name="How Can We Help You Today?")
        assert heading.is_visible()

    def test_homepage_has_concierge_services_heading(self, page_sync, base_url):
        """Homepage displays on-demand concierge services section."""
        page_sync.goto(f"{base_url}/", wait_until="networkidle")
        heading = page_sync.get_by_role("heading", name="ON-DEMAND CONCIERGE SERVICES")
        assert heading.is_visible()

    def test_homepage_has_benefits_heading(self, page_sync, base_url):
        """Homepage displays benefits section heading."""
        page_sync.goto(f"{base_url}/", wait_until="networkidle")
        heading = page_sync.get_by_role("heading", name="benefits‡ we can all align on")
        assert heading.is_visible()

    def test_homepage_displays_phone_number(self, page_sync, base_url):
        """Homepage displays customer support phone number."""
        page_sync.goto(f"{base_url}/", wait_until="networkidle")
        phone = page_sync.get_by_text("1-888-293-8272 (TTY: 711)").first
        assert phone.is_visible()

    def test_homepage_enroll_button_exists(self, page_sync, base_url):
        """Homepage has visible 'Enroll Now' button."""
        page_sync.goto(f"{base_url}/", wait_until="networkidle")
        enroll_buttons = page_sync.get_by_role("link", name="Enroll Now")
        assert enroll_buttons.count() > 0
        assert enroll_buttons.first.is_visible()

    def test_homepage_see_plans_button_exists(self, page_sync, base_url):
        """Homepage has visible 'See Plans' button."""
        page_sync.goto(f"{base_url}/", wait_until="networkidle")
        button = page_sync.get_by_role("button", name="See Plans >")
        assert button.is_visible()

    def test_homepage_navigation_contains_shop_online(self, page_sync, base_url):
        """Homepage navigation includes 'Shop Online' link to find-a-plan."""
        page_sync.goto(f"{base_url}/", wait_until="networkidle")
        link = page_sync.get_by_role("link", name="Shop Online")
        assert link.is_visible()
        href = link.get_attribute("href")
        assert "/find-a-plan" in href

    def test_homepage_navigation_contains_ways_to_enroll(self, page_sync, base_url):
        """Homepage navigation includes 'Ways to Enroll' link."""
        page_sync.goto(f"{base_url}/", wait_until="networkidle")
        link = page_sync.get_by_role("link", name="Ways to Enroll")
        assert link.is_visible()
        assert "ways-to-enroll" in link.get_attribute("href")

    def test_homepage_seminars_section(self, page_sync, base_url):
        """Homepage displays 'Seminars' section."""
        page_sync.goto(f"{base_url}/", wait_until="networkidle")
        heading = page_sync.get_by_role("heading", name="Seminars")
        assert heading.is_visible()

    def test_homepage_enroll_online_section(self, page_sync, base_url):
        """Homepage displays 'Enroll Online' section."""
        page_sync.goto(f"{base_url}/", wait_until="networkidle")
        heading = page_sync.get_by_role("heading", name="Enroll Online")
        assert heading.is_visible()

    def test_homepage_enroll_buttons_in_nav(self, page_sync, base_url):
        """Homepage has 'Enroll Now' link in navigation."""
        page_sync.goto(f"{base_url}/", wait_until="networkidle")
        enroll_link = page_sync.get_by_role("link", name="Enroll Now").first
        assert enroll_link.is_visible()

    def test_homepage_attend_seminar_link(self, page_sync, base_url):
        """Homepage navigation includes 'Attend A Seminar' link."""
        page_sync.goto(f"{base_url}/", wait_until="networkidle")
        link = page_sync.get_by_role("link", name="Attend A Seminar")
        assert link.is_visible()
        assert "attend-a-seminar" in link.get_attribute("href")
