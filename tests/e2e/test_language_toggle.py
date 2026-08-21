"""Language toggle — E2E-33..E2E-34.

Execution note: real click-driven navigation this authoring session could not
pre-verify against a live browser (see case-matrix.md 'Execution note on
interactive cases'). CI is the first real run.
"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_33_language_toggle_switches_nav_to_spanish(page: Page, base_url: str) -> None:
    """E2E-33: clicking Español translates the primary nav."""
    page.goto(base_url, wait_until="domcontentloaded")

    page.get_by_role("link", name=re.compile(r"^español$", re.I)).first.click()

    expect(page.get_by_role("link", name=re.compile(r"contáctenos", re.I)).first).to_be_visible()


@pytest.mark.readonly
def test_e2e_34_language_toggle_switches_back_to_english(page: Page, base_url: str) -> None:
    """E2E-34: from the Spanish page, clicking English restores the English nav."""
    page.goto(f"{base_url}/?lang=es-mx", wait_until="domcontentloaded")

    page.get_by_role("link", name=re.compile(r"^english$", re.I)).first.click()

    expect(page.get_by_role("link", name=re.compile(r"^contact us$", re.I)).first).to_be_visible()
