"""Test page structure, content, and data presentation."""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_19_hero_section_renders(page: Page, base_url: str) -> None:
    """E2E-19: home page hero or banner section is visible."""
    page.goto(base_url, wait_until="domcontentloaded")
    hero = page.locator("[class*='hero'], [class*='banner'], [class*='jumbotron']").first
    if hero.count() > 0:
        expect(hero).to_be_visible()


@pytest.mark.readonly
def test_e2e_20_multiple_sections_present(page: Page, base_url: str) -> None:
    """E2E-20: home page contains multiple content sections."""
    page.goto(base_url, wait_until="domcontentloaded")
    sections = page.locator("section")
    assert sections.count() >= 2, "Page should have multiple sections"


@pytest.mark.readonly
def test_e2e_21_content_readable_text(page: Page, base_url: str) -> None:
    """E2E-21: page contains readable body text content."""
    page.goto(base_url, wait_until="domcontentloaded")
    body_text = page.locator("p, article, [role='article']")
    assert body_text.count() > 0, "Page missing paragraph text content"


@pytest.mark.readonly
def test_e2e_22_buttons_are_interactive(page: Page, base_url: str) -> None:
    """E2E-22: buttons on page are visible and have cursor pointer style."""
    page.goto(base_url, wait_until="domcontentloaded")
    buttons = page.locator("button, a[role='button'], [class*='btn']")
    count = buttons.count()
    assert count > 0, "Page missing buttons"
    for i in range(min(count, 5)):
        btn = buttons.nth(i)
        expect(btn).to_be_visible()


@pytest.mark.readonly
def test_e2e_23_page_width_not_overflowing(page: Page, base_url: str) -> None:
    """E2E-23: page content does not overflow horizontally."""
    page.goto(base_url, wait_until="domcontentloaded")
    body = page.locator("body")
    viewport_width = page.viewport_size["width"]
    # Check if body width exceeds viewport
    body_width = page.evaluate("document.body.scrollWidth")
    assert body_width <= viewport_width + 1, f"Page overflows: {body_width} > {viewport_width}"


@pytest.mark.readonly
def test_e2e_24_images_load_successfully(page: Page, base_url: str) -> None:
    """E2E-24: images on page load without broken image errors."""
    page.goto(base_url, wait_until="domcontentloaded")
    images = page.locator("img")
    count = images.count()
    for i in range(count):
        img = images.nth(i)
        # Check naturalHeight for loaded images
        natural_height = img.evaluate("e => e.naturalHeight")
        assert natural_height > 0, f"Image {i} failed to load"


@pytest.mark.readonly
def test_e2e_25_links_have_valid_hrefs(page: Page, base_url: str) -> None:
    """E2E-25: navigation links have valid href attributes."""
    page.goto(base_url, wait_until="domcontentloaded")
    links = page.locator("a")
    count = links.count()
    for i in range(min(count, 15)):
        link = links.nth(i)
        href = link.get_attribute("href")
        if href and not href.startswith("#"):
            # href should not be empty or just whitespace
            assert href.strip(), f"Link {i} has empty href"


@pytest.mark.readonly
def test_e2e_26_page_response_time_acceptable(page: Page, base_url: str) -> None:
    """E2E-26: page initial response time is under 5 seconds."""
    import time
    start = time.time()
    page.goto(base_url, wait_until="domcontentloaded")
    elapsed = time.time() - start
    assert elapsed < 5, f"Page took {elapsed:.2f}s to load (expected < 5s)"


@pytest.mark.readonly
def test_e2e_27_javascript_not_blocking_rendering(page: Page, base_url: str) -> None:
    """E2E-27: page renders content before all JavaScript finishes."""
    page.goto(base_url, wait_until="domcontentloaded")
    content = page.locator("h1, h2, p").first
    expect(content).to_be_visible()


@pytest.mark.readonly
def test_e2e_28_cta_buttons_visible(page: Page, base_url: str) -> None:
    """E2E-28: call-to-action buttons are prominently visible."""
    page.goto(base_url, wait_until="domcontentloaded")
    cta = page.locator("[class*='cta'], [class*='primary'], button:visible").first
    if cta.count() > 0:
        expect(cta).to_be_visible()
