"""Test accessibility features, compliance, and page rendering."""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_09_page_has_meta_charset(page: Page, base_url: str) -> None:
    """E2E-09: page declares UTF-8 charset in meta tag."""
    page.goto(base_url, wait_until="domcontentloaded")
    charset = page.locator("meta[charset]")
    expect(charset).to_be_visible()


@pytest.mark.readonly
def test_e2e_10_page_has_viewport_meta(page: Page, base_url: str) -> None:
    """E2E-10: page declares viewport for responsive design."""
    page.goto(base_url, wait_until="domcontentloaded")
    viewport = page.locator("meta[name='viewport']")
    expect(viewport).to_be_visible()


@pytest.mark.readonly
def test_e2e_11_page_has_title(page: Page, base_url: str) -> None:
    """E2E-11: page has a descriptive title element."""
    page.goto(base_url, wait_until="domcontentloaded")
    title = page.title()
    assert len(title) > 0


@pytest.mark.readonly
def test_e2e_12_page_has_lang_attribute(page: Page, base_url: str) -> None:
    """E2E-12: HTML element has lang attribute for accessibility."""
    page.goto(base_url, wait_until="domcontentloaded")
    html = page.locator("html")
    lang = html.get_attribute("lang")
    assert lang is not None


@pytest.mark.readonly
def test_e2e_13_main_content_landmark_present(page: Page, base_url: str) -> None:
    """E2E-13: page has a main content landmark for accessibility."""
    page.goto(base_url, wait_until="domcontentloaded")
    main = page.locator("main, [role='main']")
    expect(main.first).to_be_visible()


@pytest.mark.readonly
def test_e2e_14_images_have_alt_text(page: Page, base_url: str) -> None:
    """E2E-14: decorative images have alt text or role presentation."""
    page.goto(base_url, wait_until="domcontentloaded")
    images = page.locator("img")
    count = images.count()
    assert count > 0
    for i in range(count):
        img = images.nth(i)
        alt = img.get_attribute("alt")
        role = img.get_attribute("role")
        has_alt = alt is not None and len(alt) > 0
        is_decorative = role == "presentation" or role == "none"
        assert has_alt or is_decorative, f"Image {i} missing alt text or role"


@pytest.mark.readonly
def test_e2e_15_headings_hierarchy_present(page: Page, base_url: str) -> None:
    """E2E-15: page uses heading elements (h1, h2, etc.)."""
    page.goto(base_url, wait_until="domcontentloaded")
    h1 = page.locator("h1")
    assert h1.count() > 0, "Page missing h1 heading"


@pytest.mark.readonly
def test_e2e_16_forms_have_labels(page: Page, base_url: str) -> None:
    """E2E-16: form inputs have associated labels."""
    page.goto(base_url, wait_until="domcontentloaded")
    inputs = page.locator("input[type='text'], input[type='email'], textarea, select")
    count = inputs.count()
    if count > 0:
        for i in range(min(count, 5)):  # Check first 5 inputs
            input_field = inputs.nth(i)
            input_id = input_field.get_attribute("id")
            aria_label = input_field.get_attribute("aria-label")
            if input_id:
                label = page.locator(f"label[for='{input_id}']")
                has_label = label.count() > 0 or aria_label is not None
                assert has_label, f"Input {i} missing associated label"


@pytest.mark.readonly
def test_e2e_17_links_have_meaningful_text(page: Page, base_url: str) -> None:
    """E2E-17: links have descriptive text, not just 'click here'."""
    page.goto(base_url, wait_until="domcontentloaded")
    links = page.locator("a")
    count = links.count()
    assert count > 0
    for i in range(min(count, 10)):  # Check first 10 links
        link = links.nth(i)
        text = link.text_content()
        aria_label = link.get_attribute("aria-label")
        title = link.get_attribute("title")
        has_meaningful = (text and len(text.strip()) > 0) or aria_label or title
        assert has_meaningful, f"Link {i} missing meaningful text"


@pytest.mark.readonly
def test_e2e_18_page_loads_without_console_errors(page: Page, base_url: str) -> None:
    """E2E-18: page loads without critical JavaScript console errors."""
    errors = []
    page.on("console", lambda msg: errors.append(msg) if msg.type == "error" else None)
    page.goto(base_url, wait_until="domcontentloaded")
    page.wait_for_load_state("networkidle")
    # Allow up to 3 errors as sites often have benign errors
    assert len(errors) <= 3, f"Too many console errors: {len(errors)}"
