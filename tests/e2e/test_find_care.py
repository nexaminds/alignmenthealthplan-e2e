"""Find Care section — E2E-22..E2E-27."""

import re
from urllib.parse import urlparse

import pytest
from playwright.sync_api import Page, expect

PROVIDER_SEARCH_HOST = "providersearch.alignmenthealthplan.com"


@pytest.mark.readonly
def test_e2e_22_find_a_drug_page_renders(page: Page, base_url: str) -> None:
    """E2E-22: Find a Drug page loads and shows the digital formulary option."""
    response = page.goto(f"{base_url}/find-care/find-a-drug", wait_until="domcontentloaded")

    assert response is not None, "no response from /find-care/find-a-drug"
    assert response.status < 400, f"/find-care/find-a-drug returned HTTP {response.status}"
    expect(page).to_have_title(re.compile(r"find a drug", re.I))
    expect(page.get_by_text(re.compile(r"digital drug formulary", re.I)).first).to_be_visible()


@pytest.mark.readonly
def test_e2e_23_find_a_pharmacy_page_renders(page: Page, base_url: str) -> None:
    """E2E-23: Find a Pharmacy page loads and shows the pharmacy search option."""
    response = page.goto(f"{base_url}/find-care/find-a-pharmacy", wait_until="domcontentloaded")

    assert response is not None, "no response from /find-care/find-a-pharmacy"
    assert response.status < 400, f"/find-care/find-a-pharmacy returned HTTP {response.status}"
    expect(page).to_have_title(re.compile(r"find a pharmacy", re.I))
    expect(page.get_by_text(re.compile(r"pharmacy search", re.I)).first).to_be_visible()


@pytest.mark.readonly
def test_e2e_24_find_a_care_center_page_renders(page: Page, base_url: str) -> None:
    """E2E-24: Find a Care Center page loads and lists a California region."""
    response = page.goto(f"{base_url}/find-care/find-a-care-center", wait_until="domcontentloaded")

    assert response is not None, "no response from /find-care/find-a-care-center"
    assert response.status < 400, f"/find-care/find-a-care-center returned HTTP {response.status}"
    expect(page).to_have_title(re.compile(r"find a care center", re.I))
    expect(page.get_by_text(re.compile(r"^California$", re.I)).first).to_be_visible()


@pytest.mark.readonly
def test_e2e_25_schedule_transportation_page_renders(page: Page, base_url: str) -> None:
    """E2E-25: Schedule Transportation page loads and renders its heading."""
    response = page.goto(f"{base_url}/find-care/schedule-transportation", wait_until="domcontentloaded")

    assert response is not None, "no response from /find-care/schedule-transportation"
    assert response.status < 400, f"/find-care/schedule-transportation returned HTTP {response.status}"
    expect(page).to_have_title(re.compile(r"schedule transportation", re.I))
    heading = page.get_by_text(re.compile(r"make the most of your transportation benefits", re.I)).first
    expect(heading).to_be_visible()


@pytest.mark.readonly
def test_e2e_26_find_care_doctor_link_targets_provider_search(page: Page, base_url: str) -> None:
    """E2E-26: the 'Doctor' nav link exists and targets the provider-search host."""
    page.goto(base_url, wait_until="domcontentloaded")

    link = page.get_by_role("link", name=re.compile(r"^doctor$", re.I)).first
    href = link.get_attribute("href") or ""
    assert href, "expected an href for the Doctor nav link"
    host = urlparse(href).netloc
    assert host == PROVIDER_SEARCH_HOST, f"expected Doctor link host {PROVIDER_SEARCH_HOST!r}, got {host!r}"


@pytest.mark.readonly
def test_e2e_27_find_care_hospital_link_targets_provider_search(page: Page, base_url: str) -> None:
    """E2E-27: the 'Hospital' nav link exists and targets the provider-search host."""
    page.goto(base_url, wait_until="domcontentloaded")

    link = page.get_by_role("link", name=re.compile(r"^hospital$", re.I)).first
    href = link.get_attribute("href") or ""
    assert href, "expected an href for the Hospital nav link"
    host = urlparse(href).netloc
    assert host == PROVIDER_SEARCH_HOST, f"expected Hospital link host {PROVIDER_SEARCH_HOST!r}, got {host!r}"
