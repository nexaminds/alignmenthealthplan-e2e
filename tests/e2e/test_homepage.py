"""Homepage cases — E2E-02..E2E-04.

E2E-01 (title renders) lives in test_smoke.py, the repo's seed case.
"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_02_homepage_hero_heading_renders(page: Page, base_url: str) -> None:
    """E2E-02: the hero section renders a heading about Medicare Advantage."""
    page.goto(base_url, wait_until="domcontentloaded")

    heading = page.get_by_role("heading", name=re.compile(r"medicare advantage", re.I)).first
    expect(heading).to_be_visible()


@pytest.mark.readonly
def test_e2e_03_homepage_primary_navigation_present(page: Page, base_url: str) -> None:
    """E2E-03: the primary navigation exposes the top-level sections."""
    page.goto(base_url, wait_until="domcontentloaded")

    for label in ("Discover Alignment", "Find Plans", "Find Care", "For Members", "For Providers"):
        expect(page.get_by_text(re.compile(re.escape(label), re.I)).first).to_be_visible()

    expect(page.get_by_role("link", name=re.compile(r"contact us", re.I)).first).to_be_visible()


@pytest.mark.readonly
def test_e2e_04_homepage_plan_finder_widget_present(page: Page, base_url: str) -> None:
    """E2E-04: the zip/county plan-finder widget is present. Not submitted."""
    page.goto(base_url, wait_until="domcontentloaded")

    expect(page.get_by_text(re.compile(r"zip code", re.I)).first).to_be_visible()
    expect(page.get_by_text(re.compile(r"county", re.I)).first).to_be_visible()
    expect(page.get_by_role("link", name=re.compile(r"see plans", re.I)).first).to_be_visible()

    select_count = page.locator("select").count()
    assert select_count >= 1, f"expected at least one <select> control in the plan-finder widget, found {select_count}"
