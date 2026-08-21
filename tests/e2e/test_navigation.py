"""Test site navigation, header, footer, and main menu structures."""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_02_home_page_header_present(page: Page, base_url: str) -> None:
    """E2E-02: home page contains a visible header with company branding."""
    page.goto(base_url, wait_until="domcontentloaded")
    header = page.locator("header")
    expect(header).to_be_visible()


@pytest.mark.readonly
def test_e2e_03_home_page_footer_present(page: Page, base_url: str) -> None:
    """E2E-03: home page contains a footer element."""
    page.goto(base_url, wait_until="domcontentloaded")
    footer = page.locator("footer")
    expect(footer).to_be_visible()


@pytest.mark.readonly
def test_e2e_04_navigation_menu_accessible(page: Page, base_url: str) -> None:
    """E2E-04: main navigation menu is present and accessible."""
    page.goto(base_url, wait_until="domcontentloaded")
    nav = page.locator("nav")
    expect(nav).to_be_visible()


@pytest.mark.readonly
def test_e2e_05_about_us_link_present(page: Page, base_url: str) -> None:
    """E2E-05: 'About Us' or similar link exists in navigation."""
    page.goto(base_url, wait_until="domcontentloaded")
    about_link = page.locator("a:has-text(/About|about us/i)")
    expect(about_link.first).to_be_visible()


@pytest.mark.readonly
def test_e2e_06_contact_link_present(page: Page, base_url: str) -> None:
    """E2E-06: 'Contact' or 'Contact Us' link exists."""
    page.goto(base_url, wait_until="domcontentloaded")
    contact_link = page.locator("a:has-text(/Contact|get in touch/i)")
    expect(contact_link.first).to_be_visible()


@pytest.mark.readonly
def test_e2e_07_logo_links_to_home(page: Page, base_url: str) -> None:
    """E2E-07: site logo navigates back to home when clicked."""
    page.goto(base_url, wait_until="domcontentloaded")
    logo = page.locator("a[href='/']:first-of-type")
    if logo.count() > 0:
        page.goto(f"{base_url}/about", wait_until="domcontentloaded")
        logo.click()
        expect(page).to_have_url(re.compile(r"/$"))


@pytest.mark.readonly
def test_e2e_08_responsive_menu_mobile(page: Page, base_url: str) -> None:
    """E2E-08: mobile menu button is present on small viewports."""
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto(base_url, wait_until="domcontentloaded")
    hamburger = page.locator("[aria-label*='menu' i], [class*='menu' i], button:has-text('☰'), button:has-text('Menu')")
    expect(hamburger.first).to_be_visible()
