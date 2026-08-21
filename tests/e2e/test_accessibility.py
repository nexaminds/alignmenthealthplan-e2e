"""Basic accessibility checks — E2E-40..E2E-43."""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_40_homepage_has_exactly_one_h1(page: Page, base_url: str) -> None:
    """E2E-40: the homepage exposes exactly one top-level heading."""
    page.goto(base_url, wait_until="domcontentloaded")

    h1_count = page.get_by_role("heading", level=1).count()
    assert h1_count == 1, f"expected exactly one <h1> on the homepage, found {h1_count}"


@pytest.mark.readonly
def test_e2e_41_homepage_has_navigation_landmark(page: Page, base_url: str) -> None:
    """E2E-41: the homepage exposes at least one navigation landmark."""
    page.goto(base_url, wait_until="domcontentloaded")

    nav_count = page.get_by_role("navigation").count()
    assert nav_count >= 1, f"expected at least one navigation landmark, found {nav_count}"


@pytest.mark.readonly
def test_e2e_42_homepage_has_contentinfo_landmark(page: Page, base_url: str) -> None:
    """E2E-42: the homepage exposes a footer (contentinfo) landmark."""
    page.goto(base_url, wait_until="domcontentloaded")

    footer_count = page.get_by_role("contentinfo").count()
    assert footer_count >= 1, f"expected at least one contentinfo landmark, found {footer_count}"


@pytest.mark.readonly
def test_e2e_43_find_a_plan_zip_code_field_has_accessible_label(page: Page, base_url: str) -> None:
    """E2E-43: the Zip code field on Find a Plan is programmatically labeled."""
    page.goto(f"{base_url}/find-a-plan", wait_until="domcontentloaded")

    zip_field = page.get_by_label(re.compile(r"zip code", re.I)).first
    expect(zip_field).to_be_visible()
