"""Footer / legal pages — E2E-28..E2E-32."""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_28_privacy_notices_page_renders(page: Page, base_url: str) -> None:
    """E2E-28: Privacy Notices page loads and renders its heading."""
    response = page.goto(f"{base_url}/about-us/privacy-notices", wait_until="domcontentloaded")

    assert response is not None, "no response from /about-us/privacy-notices"
    assert response.status < 400, f"/about-us/privacy-notices returned HTTP {response.status}"
    expect(page).to_have_title(re.compile(r"privacy notices", re.I))
    expect(page.get_by_role("heading", name=re.compile(r"privacy notices", re.I)).first).to_be_visible()


@pytest.mark.readonly
def test_e2e_29_terms_of_use_page_lists_subpolicies(page: Page, base_url: str) -> None:
    """E2E-29: Terms of Use hub page lists its sub-policy 'Read More' links."""
    response = page.goto(f"{base_url}/about-us/terms-of-use", wait_until="domcontentloaded")

    assert response is not None, "no response from /about-us/terms-of-use"
    assert response.status < 400, f"/about-us/terms-of-use returned HTTP {response.status}"
    expect(page).to_have_title(re.compile(r"terms of use", re.I))

    read_more_count = page.get_by_role("link", name=re.compile(r"read more", re.I)).count()
    assert read_more_count >= 4, f"expected at least 4 'Read More' sub-policy links, found {read_more_count}"


@pytest.mark.readonly
def test_e2e_30_nondiscrimination_policy_page_renders(page: Page, base_url: str) -> None:
    """E2E-30: Nondiscrimination Policy page loads and exposes the grievance phone line."""
    response = page.goto(
        f"{base_url}/about-us/terms-of-use/nondiscrimination-policy", wait_until="domcontentloaded"
    )

    assert response is not None, "no response from /about-us/terms-of-use/nondiscrimination-policy"
    assert response.status < 400, f"nondiscrimination-policy returned HTTP {response.status}"
    expect(page).to_have_title(re.compile(r"nondiscrimination policy", re.I))
    expect(page.locator("a[href^='tel:1-844-297-5948']").first).to_be_visible()


@pytest.mark.readonly
def test_e2e_31_notice_of_availability_page_renders(page: Page, base_url: str) -> None:
    """E2E-31: Notice of Availability page loads and describes free interpreter services."""
    response = page.goto(
        f"{base_url}/about-us/terms-of-use/notice-of-availability", wait_until="domcontentloaded"
    )

    assert response is not None, "no response from /about-us/terms-of-use/notice-of-availability"
    assert response.status < 400, f"notice-of-availability returned HTTP {response.status}"
    expect(page).to_have_title(re.compile(r"notice of availability", re.I))
    expect(page.get_by_text(re.compile(r"free interpreter services", re.I)).first).to_be_visible()


@pytest.mark.readonly
def test_e2e_32_disaster_policy_page_renders(page: Page, base_url: str) -> None:
    """E2E-32: Disaster Policy page loads and renders its heading."""
    response = page.goto(f"{base_url}/about-us/disaster-policy", wait_until="domcontentloaded")

    assert response is not None, "no response from /about-us/disaster-policy"
    assert response.status < 400, f"/about-us/disaster-policy returned HTTP {response.status}"
    expect(page).to_have_title(re.compile(r"disaster policy", re.I))
    heading = page.get_by_text(
        re.compile(r"how alignment health plan supports medicare advantage members during disasters", re.I)
    ).first
    expect(heading).to_be_visible()
