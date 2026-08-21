"""Cross-page navigation and crawl-boundary cases — E2E-11..E2E-13."""

import re
from urllib.parse import urlparse

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_11_footer_legal_links_present(page: Page, base_url: str) -> None:
    """E2E-11: footer legal/compliance links are visible and stay on-domain."""
    page.goto(base_url, wait_until="domcontentloaded")

    expected = {
        "Legal Notices": "/about-us/legal-notices",
        "Privacy Notices": "/about-us/privacy-notices",
        "Terms of Use": "/about-us/terms-of-use",
    }

    for label, expected_path in expected.items():
        link = page.get_by_role("link", name=re.compile(re.escape(label), re.I)).first
        expect(link).to_be_visible()
        href = link.get_attribute("href") or ""
        assert expected_path in href, f"expected {label!r} href to contain {expected_path!r}, got {href!r}"


@pytest.mark.readonly
def test_e2e_12_shop_online_nav_link_targets_find_a_plan(page: Page, base_url: str) -> None:
    """E2E-12: the 'Shop Online' nav link resolves to the Find a Plan page."""
    page.goto(base_url, wait_until="domcontentloaded")

    link = page.get_by_role("link", name=re.compile(r"shop online", re.I)).first
    href = link.get_attribute("href") or ""
    assert "/find-a-plan" in href, f"expected Shop Online href to contain /find-a-plan, got {href!r}"

    response = page.goto(f"{base_url}/find-a-plan", wait_until="domcontentloaded")
    assert response is not None, "no response navigating to /find-a-plan"
    assert response.status < 400, f"/find-a-plan returned HTTP {response.status}"


@pytest.mark.readonly
def test_e2e_13_gated_login_links_stay_outside_crawl_scope(page: Page, base_url: str) -> None:
    """E2E-13: Member/Provider login links point off-host, confirming crawl exclusion."""
    page.goto(base_url, wait_until="domcontentloaded")
    base_host = urlparse(base_url).netloc

    for label in ("Member Login", "Provider Login"):
        link = page.get_by_role("link", name=re.compile(re.escape(label), re.I)).first
        href = link.get_attribute("href") or ""
        assert href, f"expected an href for {label!r}"
        host = urlparse(href).netloc
        assert host and host != base_host, (
            f"{label} unexpectedly resolves within crawl scope ({href!r}); "
            "gated login flows must stay excluded from this read-only public suite"
        )
