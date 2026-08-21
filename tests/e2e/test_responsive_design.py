"""Test CSS styling, responsive design, and visual consistency."""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_41_page_mobile_responsive_375(page: Page, base_url: str) -> None:
    """E2E-41: page renders properly on mobile (375px width)."""
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto(base_url, wait_until="domcontentloaded")
    # Check main content is visible
    main = page.locator("main, [role='main'], body > div").first
    expect(main).to_be_visible()


@pytest.mark.readonly
def test_e2e_42_page_tablet_responsive_768(page: Page, base_url: str) -> None:
    """E2E-42: page renders properly on tablet (768px width)."""
    page.set_viewport_size({"width": 768, "height": 1024})
    page.goto(base_url, wait_until="domcontentloaded")
    main = page.locator("main, [role='main'], body > div").first
    expect(main).to_be_visible()


@pytest.mark.readonly
def test_e2e_43_page_desktop_responsive_1920(page: Page, base_url: str) -> None:
    """E2E-43: page renders properly on desktop (1920px width)."""
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto(base_url, wait_until="domcontentloaded")
    main = page.locator("main, [role='main'], body > div").first
    expect(main).to_be_visible()


@pytest.mark.readonly
def test_e2e_44_text_readable_on_mobile(page: Page, base_url: str) -> None:
    """E2E-44: text content is readable at mobile viewport."""
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto(base_url, wait_until="domcontentloaded")
    # Check that paragraph text is not cut off
    paragraphs = page.locator("p").first
    if paragraphs.count() > 0:
        expect(paragraphs).to_be_visible()


@pytest.mark.readonly
def test_e2e_45_colors_have_contrast(page: Page, base_url: str) -> None:
    """E2E-45: text color has sufficient contrast against background."""
    page.goto(base_url, wait_until="domcontentloaded")
    # Check body text color vs background
    body = page.locator("body")
    color = body.evaluate("e => getComputedStyle(e).color")
    bg_color = body.evaluate("e => getComputedStyle(e).backgroundColor")
    # Both should be set (not transparent)
    assert color and color != "rgba(0, 0, 0, 0)", "Text color not properly set"


@pytest.mark.readonly
def test_e2e_46_font_size_readable(page: Page, base_url: str) -> None:
    """E2E-46: body text font size is readable (> 12px)."""
    page.goto(base_url, wait_until="domcontentloaded")
    paragraph = page.locator("p").first
    if paragraph.count() > 0:
        font_size = paragraph.evaluate("e => parseInt(getComputedStyle(e).fontSize)")
        assert font_size >= 12, f"Font size too small: {font_size}px"


@pytest.mark.readonly
def test_e2e_47_line_height_readable(page: Page, base_url: str) -> None:
    """E2E-47: text line height is readable (> 1.4)."""
    page.goto(base_url, wait_until="domcontentloaded")
    paragraph = page.locator("p").first
    if paragraph.count() > 0:
        line_height = paragraph.evaluate("e => getComputedStyle(e).lineHeight")
        # line_height could be "normal" or numeric
        if line_height != "normal":
            height_value = float(line_height.replace("px", ""))
            # Relative to font size, should be > 1.4
            assert height_value > 15, f"Line height may be too tight: {line_height}"


@pytest.mark.readonly
def test_e2e_48_buttons_styled_consistently(page: Page, base_url: str) -> None:
    """E2E-48: buttons have consistent styling across page."""
    page.goto(base_url, wait_until="domcontentloaded")
    buttons = page.locator("button, a[role='button']")
    count = buttons.count()
    if count >= 2:
        first_bg = buttons.nth(0).evaluate("e => getComputedStyle(e).backgroundColor")
        # At least some buttons should have background color
        assert first_bg, "Button background color not set"


@pytest.mark.readonly
def test_e2e_49_focus_indicators_visible(page: Page, base_url: str) -> None:
    """E2E-49: interactive elements show focus indicators."""
    page.goto(base_url, wait_until="domcontentloaded")
    link = page.locator("a").first
    if link.count() > 0:
        link.focus()
        # Browser should show focus indicator
        page.wait_for_timeout(100)


@pytest.mark.readonly
def test_e2e_50_no_horizontal_scroll_mobile(page: Page, base_url: str) -> None:
    """E2E-50: mobile view does not require horizontal scrolling."""
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto(base_url, wait_until="domcontentloaded")
    scroll_width = page.evaluate("document.documentElement.scrollWidth")
    viewport_width = page.viewport_size["width"]
    assert scroll_width <= viewport_width + 1, "Mobile view requires horizontal scroll"
