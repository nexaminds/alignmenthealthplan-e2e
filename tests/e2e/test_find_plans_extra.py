"""Remaining Find Plans section pages — E2E-14..E2E-20."""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_14_ways_to_enroll_page_renders(page: Page, base_url: str) -> None:
    """E2E-14: Ways to Enroll page loads and exposes the sales phone line."""
    response = page.goto(f"{base_url}/find-plans/ways-to-enroll", wait_until="domcontentloaded")

    assert response is not None, "no response from /find-plans/ways-to-enroll"
    assert response.status < 400, f"/find-plans/ways-to-enroll returned HTTP {response.status}"
    expect(page).to_have_title(re.compile(r"ways to enroll", re.I))
    expect(page.locator("a[href^='tel:1-888-293-8272']").first).to_be_visible()


@pytest.mark.readonly
def test_e2e_15_attend_a_seminar_page_renders(page: Page, base_url: str) -> None:
    """E2E-15: Attend a Seminar page loads and renders its heading (case-insensitive)."""
    response = page.goto(f"{base_url}/find-plans/attend-a-seminar", wait_until="domcontentloaded")

    assert response is not None, "no response from /find-plans/attend-a-seminar"
    assert response.status < 400, f"/find-plans/attend-a-seminar returned HTTP {response.status}"
    expect(page).to_have_title(re.compile(r"attend a seminar", re.I))
    heading = page.get_by_text(re.compile(r"upcoming seminars near you", re.I)).first
    expect(heading).to_be_visible()


@pytest.mark.readonly
def test_e2e_16_benefit_highlights_page_renders(page: Page, base_url: str) -> None:
    """E2E-16: Benefit Highlights page loads and renders its heading."""
    response = page.goto(f"{base_url}/find-plans/benefit-highlights", wait_until="domcontentloaded")

    assert response is not None, "no response from /find-plans/benefit-highlights"
    assert response.status < 400, f"/find-plans/benefit-highlights returned HTTP {response.status}"
    expect(page).to_have_title(re.compile(r"benefit highlights", re.I))
    expect(page.get_by_role("heading", name=re.compile(r"benefit highlights", re.I)).first).to_be_visible()


@pytest.mark.readonly
def test_e2e_17_pre_enrollment_kit_breadcrumb_targets_ways_to_enroll(page: Page, base_url: str) -> None:
    """E2E-17: Pre-Enrollment Kit page loads with a working parent breadcrumb."""
    response = page.goto(
        f"{base_url}/find-plans/ways-to-enroll/pre-enrollment-kit", wait_until="domcontentloaded"
    )

    assert response is not None, "no response from /find-plans/ways-to-enroll/pre-enrollment-kit"
    assert response.status < 400, f"pre-enrollment-kit returned HTTP {response.status}"
    expect(page).to_have_title(re.compile(r"pre-enrollment kit", re.I))

    breadcrumb = page.get_by_role("link", name=re.compile(r"ways to enroll", re.I)).first
    expect(breadcrumb).to_be_visible()
    href = breadcrumb.get_attribute("href") or ""
    assert "/find-plans/ways-to-enroll" in href, (
        f"expected breadcrumb href to contain /find-plans/ways-to-enroll, got {href!r}"
    )


@pytest.mark.readonly
def test_e2e_18_group_retiree_options_page_renders(page: Page, base_url: str) -> None:
    """E2E-18: Group Retiree Options page loads and renders its heading (case-insensitive)."""
    response = page.goto(f"{base_url}/find-plans/group-retiree-options", wait_until="domcontentloaded")

    assert response is not None, "no response from /find-plans/group-retiree-options"
    assert response.status < 400, f"/find-plans/group-retiree-options returned HTTP {response.status}"
    expect(page).to_have_title(re.compile(r"group retiree options", re.I))
    heading = page.get_by_text(re.compile(r"helping you serve your retirees", re.I)).first
    expect(heading).to_be_visible()


@pytest.mark.readonly
def test_e2e_19_medicare_part_d_faqs_page_renders(page: Page, base_url: str) -> None:
    """E2E-19: Medicare Part D FAQs page loads with at least 10 question entries."""
    response = page.goto(f"{base_url}/find-plans/part-d-faqs", wait_until="domcontentloaded")

    assert response is not None, "no response from /find-plans/part-d-faqs"
    assert response.status < 400, f"/find-plans/part-d-faqs returned HTTP {response.status}"
    expect(page).to_have_title(re.compile(r"medicare part d faqs", re.I))

    question_count = page.get_by_role("link", name=re.compile(r"^Q\.", re.I)).count()
    assert question_count >= 10, f"expected at least 10 Part D FAQ questions, found {question_count}"


@pytest.mark.readonly
def test_e2e_20_visit_us_page_renders(page: Page, base_url: str) -> None:
    """E2E-20: Visit Us page loads and lists at least one plan center with directions."""
    response = page.goto(f"{base_url}/find-plans/visit-us", wait_until="domcontentloaded")

    assert response is not None, "no response from /find-plans/visit-us"
    assert response.status < 400, f"/find-plans/visit-us returned HTTP {response.status}"
    expect(page).to_have_title(re.compile(r"visit", re.I))
    expect(page.get_by_role("link", name=re.compile(r"get directions", re.I)).first).to_be_visible()
