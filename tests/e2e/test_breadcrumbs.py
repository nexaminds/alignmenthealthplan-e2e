"""Breadcrumb integrity — E2E-45."""

import re

import pytest
from playwright.sync_api import Page


@pytest.mark.readonly
def test_e2e_45_ways_to_enroll_home_breadcrumb_resolves(page: Page, base_url: str) -> None:
    """E2E-45: the 'Home' breadcrumb on a sub-page resolves to a live page."""
    page.goto(f"{base_url}/find-plans/ways-to-enroll", wait_until="domcontentloaded")

    breadcrumb_home = page.get_by_role("link", name=re.compile(r"^home$", re.I)).first
    href = breadcrumb_home.get_attribute("href") or ""
    assert href, "expected an href on the Home breadcrumb link"

    target = href if href.startswith("http") else f"{base_url}{href}"
    response = page.goto(target, wait_until="domcontentloaded")
    assert response is not None, f"no response navigating to breadcrumb Home href {href!r}"
    assert response.status < 400, f"breadcrumb Home href {href!r} returned HTTP {response.status}"
