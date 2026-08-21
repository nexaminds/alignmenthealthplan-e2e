"""Plan and discovery content page cases — E2E-05..E2E-08."""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_05_find_a_plan_page_renders(page: Page, base_url: str) -> None:
    """E2E-05: the Find a Plan page loads and renders its title."""
    response = page.goto(f"{base_url}/find-a-plan", wait_until="domcontentloaded")

    assert response is not None, "no response from /find-a-plan"
    assert response.status < 400, f"/find-a-plan returned HTTP {response.status}"
    expect(page).to_have_title(re.compile(r"find a plan", re.I))


@pytest.mark.readonly
def test_e2e_06_find_a_plan_lead_form_fields_present(page: Page, base_url: str) -> None:
    """E2E-06: the lead-capture form's fields are present. Never submitted."""
    page.goto(f"{base_url}/find-a-plan", wait_until="domcontentloaded")

    for label in ("First Name", "Last Name", "Email", "Phone Number", "U.S. ZIP Code"):
        expect(page.get_by_text(re.compile(re.escape(label), re.I)).first).to_be_visible()

    control_count = page.locator("input, select").count()
    assert control_count >= 5, f"expected at least 5 form controls on Find a Plan, found {control_count}"


@pytest.mark.readonly
def test_e2e_07_why_alignment_page_renders(page: Page, base_url: str) -> None:
    """E2E-07: the Why Alignment Health Plan page loads and renders its heading."""
    response = page.goto(
        f"{base_url}/discover-ahp/why-alignment-health-plan", wait_until="domcontentloaded"
    )

    assert response is not None, "no response from /discover-ahp/why-alignment-health-plan"
    assert response.status < 400, f"why-alignment-health-plan returned HTTP {response.status}"
    heading = page.get_by_role("heading", name=re.compile(r"why alignment health plan", re.I)).first
    expect(heading).to_be_visible()


@pytest.mark.readonly
def test_e2e_08_medicare_advantage_guide_page_renders(page: Page, base_url: str) -> None:
    """E2E-08: the Medicare Advantage guide page loads and renders its heading."""
    response = page.goto(
        f"{base_url}/discover-ahp/medicare-advantage-plans", wait_until="domcontentloaded"
    )

    assert response is not None, "no response from /discover-ahp/medicare-advantage-plans"
    assert response.status < 400, f"medicare-advantage-plans returned HTTP {response.status}"
    heading = page.get_by_role("heading", name=re.compile(r"medicare advantage", re.I)).first
    expect(heading).to_be_visible()
