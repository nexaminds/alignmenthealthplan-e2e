"""Responsive behavior — E2E-38..E2E-39.

Execution note: viewport-driven layout behavior this authoring session could
not pre-verify against a live browser (see case-matrix.md 'Execution note on
interactive cases'). CI is the first real run.
"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_38_mobile_viewport_shows_menu_toggle(page: Page, base_url: str) -> None:
    """E2E-38: at a mobile viewport, the hamburger 'Menu' toggle is visible."""
    page.set_viewport_size({"width": 375, "height": 812})
    page.goto(base_url, wait_until="domcontentloaded")

    expect(page.get_by_text(re.compile(r"^menu$", re.I)).first).to_be_visible()


@pytest.mark.readonly
def test_e2e_39_desktop_viewport_shows_primary_nav_directly(page: Page, base_url: str) -> None:
    """E2E-39: at a desktop viewport, primary nav is visible without opening any toggle."""
    page.set_viewport_size({"width": 1440, "height": 900})
    page.goto(base_url, wait_until="domcontentloaded")

    expect(page.get_by_text(re.compile(r"discover alignment", re.I)).first).to_be_visible()
