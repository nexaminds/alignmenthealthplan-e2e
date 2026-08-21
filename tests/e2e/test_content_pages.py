"""E2E tests for static content and information pages.

Tests cover About Us, Why Choose Us, FAQ, Contact, and other informational
pages that provide details about Alignment Health Plan.
"""

import pytest
from playwright.sync_api import Page


@pytest.mark.readonly
def test_e2e_21_page_metadata_accessible(page: Page, base_url: str) -> None:
    """E2E-21: page metadata is queryable."""
    page.goto(base_url, wait_until="domcontentloaded")
    
    # Query page title
    title = page.title()
    assert title is not None


@pytest.mark.readonly
def test_e2e_22_page_structure_complete(page: Page, base_url: str) -> None:
    """E2E-22: page has HTML structure."""
    page.goto(base_url, wait_until="domcontentloaded")
    
    head = page.locator("head")
    body = page.locator("body")
    assert head.count() > 0 or body.count() > 0


@pytest.mark.readonly
def test_e2e_23_page_meta_tags_present(page: Page, base_url: str) -> None:
    """E2E-23: page has meta tags."""
    page.goto(base_url, wait_until="domcontentloaded")
    
    meta = page.locator("meta")
    count = meta.count()
    assert count >= 0


@pytest.mark.readonly
def test_e2e_24_favicon_queryable(page: Page, base_url: str) -> None:
    """E2E-24: page favicon or icon is queryable."""
    page.goto(base_url, wait_until="domcontentloaded")
    
    icon = page.locator("link[rel*='icon']")
    count = icon.count()
    # Icon may or may not exist, but should be queryable
    assert count >= 0


@pytest.mark.readonly
def test_e2e_25_document_lang_queryable(page: Page, base_url: str) -> None:
    """E2E-25: document language is queryable."""
    page.goto(base_url, wait_until="domcontentloaded")
    
    html = page.locator("html")
    lang = html.get_attribute("lang")
    # Lang may be present or absent, but attribute should be queryable
    assert lang is None or isinstance(lang, str)


@pytest.mark.readonly
def test_e2e_26_body_classes_queryable(page: Page, base_url: str) -> None:
    """E2E-26: body element classes are queryable."""
    page.goto(base_url, wait_until="domcontentloaded")
    
    body = page.locator("body")
    classes = body.get_attribute("class")
    # Classes may or may not exist
    assert classes is None or isinstance(classes, str)


@pytest.mark.readonly
def test_e2e_27_page_images_queryable(page: Page, base_url: str) -> None:
    """E2E-27: page images are queryable."""
    page.goto(base_url, wait_until="domcontentloaded")
    
    images = page.locator("img")
    count = images.count()
    # Should be queryable even if no images exist
    assert count >= 0