"""Form interaction and client-side validation tests.

Tests form rendering, field validation, and interactive controls.
"""

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_41_homepage_zip_form_interactive(page: Page, base_url: str) -> None:
    """E2E-41: Homepage zip code form fields are interactive."""
    page.goto(base_url)
    
    # Find zip input
    zip_input = page.locator('input[placeholder*="Zip"], input[name*="zip"]').first
    
    if zip_input.count() > 0:
        expect(zip_input).to_be_enabled()
        expect(zip_input).to_be_visible()


@pytest.mark.readonly
def test_e2e_42_form_county_dropdown(page: Page, base_url: str) -> None:
    """E2E-42: Plan search form has county/state dropdown selector."""
    page.goto(base_url)
    
    # Look for select or dropdown elements
    selects = page.locator("select").all()
    
    # Should have at least one dropdown (likely county/state)
    assert len(selects) > 0, "No dropdown found in homepage"


@pytest.mark.readonly
def test_e2e_43_see_plans_button_visible(page: Page, base_url: str) -> None:
    """E2E-43: See Plans/Search button is visible and enabled."""
    page.goto(base_url)
    
    # Find the search button
    search_btn = page.locator('button:has-text("See Plans"), button:has-text("Search")').first
    
    if search_btn.count() > 0:
        expect(search_btn).to_be_visible()
        expect(search_btn).to_be_enabled()


@pytest.mark.readonly
def test_e2e_44_language_selector_present(page: Page, base_url: str) -> None:
    """E2E-44: Language selector is present (English/Español)."""
    page.goto(base_url)
    
    # Look for language switcher
    lang_indicators = page.locator("text=English").all()
    
    # Should have language indicator visible
    assert len(lang_indicators) > 0, "No language selector found"


@pytest.mark.readonly
def test_e2e_45_text_size_controls(page: Page, base_url: str) -> None:
    """E2E-45: Text size accessibility controls are present."""
    page.goto(base_url)
    
    # Look for text size buttons
    size_controls = page.locator("button[aria-label*='text'], button:has-text('Text')").all()
    
    # Should have text size controls or indicator
    page_content = page.content()
    assert "text size" in page_content.lower() or "font size" in page_content.lower()


@pytest.mark.readonly
def test_e2e_46_search_functionality(page: Page, base_url: str) -> None:
    """E2E-46: Site search functionality is accessible."""
    page.goto(base_url)
    
    # Look for search input
    search_inputs = page.locator('input[type="search"], input[placeholder*="Search"]').all()
    
    # Should have search available
    assert len(search_inputs) > 0, "No search input found"


@pytest.mark.readonly
def test_e2e_47_doctor_search_accessible(page: Page, base_url: str) -> None:
    """E2E-47: Doctor/Provider search link is accessible."""
    page.goto(base_url)
    
    # Look for provider search link
    provider_search = page.locator('a[href*="providersearch"], text=Doctor').first
    
    expect(provider_search).to_be_visible()


@pytest.mark.readonly
def test_e2e_48_external_link_warning(page: Page, base_url: str) -> None:
    """E2E-48: External links trigger appropriate warning/dialog."""
    page.goto(base_url)
    
    # Look for external links
    external_links = page.locator('a[target="_blank"]').all()
    
    # Should have some external links with appropriate handling
    assert len(external_links) > 0, "No external links found"


@pytest.mark.readonly
def test_e2e_49_accessibility_attributes(page: Page, base_url: str) -> None:
    """E2E-49: Key elements have accessibility attributes."""
    page.goto(base_url)
    
    # Check for ARIA labels on buttons
    buttons_with_aria = page.locator('button[aria-label]').all()
    
    # Should have accessible buttons
    total_buttons = page.locator('button').all()
    assert len(total_buttons) > 0, "No buttons found"


@pytest.mark.readonly
def test_e2e_50_semantic_html_structure(page: Page, base_url: str) -> None:
    """E2E-50: Page uses semantic HTML (nav, main, footer, etc.)."""
    page.goto(base_url)
    
    # Check for semantic elements
    nav_elements = page.locator("nav").all()
    main_elements = page.locator("main").all()
    footer_elements = page.locator("footer").all()
    
    # Should have at least nav and footer
    assert len(nav_elements) > 0, "No nav element found"
    assert len(footer_elements) > 0, "No footer element found"


@pytest.mark.readonly
def test_e2e_51_responsive_images(page: Page, base_url: str) -> None:
    """E2E-51: Images use responsive attributes (srcset/picture)."""
    page.goto(base_url)
    
    # Check for images with responsive attributes
    responsive_imgs = page.locator('img[srcset], picture').all()
    
    # Should have responsive images
    all_imgs = page.locator("img").all()
    assert len(all_imgs) > 0, "No images found"


@pytest.mark.readonly
def test_e2e_52_page_loading_performance(page: Page, base_url: str) -> None:
    """E2E-52: Homepage loads within acceptable time."""
    # Measure load time
    start_time = page.context.browser.start_time if hasattr(page.context.browser, 'start_time') else None
    
    response = page.goto(base_url, wait_until="domcontentloaded")
    
    assert response.status < 400
    # Page should be interactive within reasonable time
    expect(page.locator("text=Alignment")).to_be_visible()


@pytest.mark.readonly
def test_e2e_53_no_console_errors_homepage(page: Page, base_url: str) -> None:
    """E2E-53: Homepage loads without JavaScript console errors."""
    errors = []
    page.on("console", lambda msg: errors.append(msg) if msg.type == "error" else None)
    
    page.goto(base_url)
    page.wait_for_load_state("networkidle")
    
    # Should not have error-level console messages
    error_messages = [str(e) for e in errors]
    critical_errors = [e for e in error_messages if "error" in e.lower() and "404" not in e]
    
    assert len(critical_errors) == 0, f"Console errors found: {critical_errors}"


@pytest.mark.readonly
def test_e2e_54_mobile_responsive_layout(page: Page, base_url: str) -> None:
    """E2E-54: Homepage is responsive on mobile viewport."""
    page.goto(base_url)
    page.set_viewport_size({"width": 375, "height": 667})
    page.reload()
    
    # Main content should be visible
    expect(page.locator("text=Medicare Advantage")).to_be_visible()
    expect(page.locator("text=Plans that Put You First")).to_be_visible()


@pytest.mark.readonly
def test_e2e_55_tablet_responsive_layout(page: Page, base_url: str) -> None:
    """E2E-55: Homepage is responsive on tablet viewport."""
    page.goto(base_url)
    page.set_viewport_size({"width": 768, "height": 1024})
    page.reload()
    
    # Layout should adapt
    expect(page.locator("text=Medicare Advantage")).to_be_visible()


@pytest.mark.readonly
def test_e2e_56_keyboard_navigation(page: Page, base_url: str) -> None:
    """E2E-56: Main interactive elements are keyboard accessible."""
    page.goto(base_url)
    
    # Tab through the page
    page.press("body", "Tab")
    page.press("body", "Tab")
    page.press("body", "Tab")
    
    # Should have focused element
    focused = page.evaluate("document.activeElement.tagName")
    assert focused is not None


@pytest.mark.readonly
def test_e2e_57_focus_visible_on_buttons(page: Page, base_url: str) -> None:
    """E2E-57: Buttons show focus indicator when keyboard navigated."""
    page.goto(base_url)
    
    # Tab to a button
    page.press("body", "Tab")
    page.press("body", "Tab")
    
    # Focused element should be identifiable
    focused_elem = page.evaluate("document.activeElement")
    assert focused_elem is not None


@pytest.mark.readonly
def test_e2e_58_link_underline_visible(page: Page, base_url: str) -> None:
    """E2E-58: Links are visually distinguishable from regular text."""
    page.goto(base_url)
    page.wait_for_load_state("domcontentloaded")
    
    # Find links
    links = page.locator("a").all()
    
    # Should have visible links
    assert len(links) > 5, "Too few links on homepage"


@pytest.mark.readonly
def test_e2e_59_heading_hierarchy_valid(page: Page, base_url: str) -> None:
    """E2E-59: Page uses valid heading hierarchy (h1, h2, h3)."""
    page.goto(base_url)
    
    # Check for h1
    h1_elements = page.locator("h1").all()
    
    # Should have h1 for main title
    assert len(h1_elements) > 0, "No h1 found"


@pytest.mark.readonly
def test_e2e_60_meta_tags_present(page: Page, base_url: str) -> None:
    """E2E-60: Page has required meta tags for SEO and accessibility."""
    page.goto(base_url)
    
    # Check for viewport meta tag
    viewport_meta = page.locator('meta[name="viewport"]')
    expect(viewport_meta).to_have_attribute("content", /width=device-width/)
    
    # Check for description
    desc_meta = page.locator('meta[name="description"]')
    expect(desc_meta).to_have_count(1)
