"""Contact Us page cases — E2E-09..E2E-10."""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_09_contact_us_phone_channels_render(page: Page, base_url: str) -> None:
    """E2E-09: the Contact Us page renders and exposes multiple phone channels."""
    response = page.goto(f"{base_url}/about-us/contact-us", wait_until="domcontentloaded")

    assert response is not None, "no response from /about-us/contact-us"
    assert response.status < 400, f"/about-us/contact-us returned HTTP {response.status}"

    heading = page.get_by_role("heading", name=re.compile(r"contact us", re.I)).first
    expect(heading).to_be_visible()

    tel_links = page.locator("a[href^='tel:']")
    assert tel_links.count() >= 3, f"expected at least 3 tel: links on Contact Us, found {tel_links.count()}"


@pytest.mark.readonly
def test_e2e_10_contact_us_message_audience_links_present(page: Page, base_url: str) -> None:
    """E2E-10: the 'Send Us a Message' audience links are present."""
    page.goto(f"{base_url}/about-us/contact-us", wait_until="domcontentloaded")

    expect(page.get_by_text(re.compile(r"send us a message", re.I)).first).to_be_visible()

    for audience in ("I am a Member", "I am a Provider", "I am a Broker", "Other Inquiries"):
        link = page.get_by_role("link", name=re.compile(re.escape(audience), re.I)).first
        expect(link).to_be_visible()
