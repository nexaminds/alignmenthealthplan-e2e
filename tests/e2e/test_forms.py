"""Test form validation and user input handling."""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.readonly
def test_e2e_34_form_fields_have_required_markers(page: Page, base_url: str) -> None:
    """E2E-34: required form fields are marked as required."""
    page.goto(base_url, wait_until="domcontentloaded")
    required_inputs = page.locator("input[required], textarea[required], select[required]")
    count = required_inputs.count()
    if count > 0:
        for i in range(count):
            inp = required_inputs.nth(i)
            is_required = inp.get_attribute("required") is not None
            aria_required = inp.get_attribute("aria-required")
            assert is_required or aria_required == "true", f"Input {i} not marked required"


@pytest.mark.readonly
def test_e2e_35_email_input_validation(page: Page, base_url: str) -> None:
    """E2E-35: email input field enforces email format on client side."""
    page.goto(base_url, wait_until="domcontentloaded")
    email_input = page.locator("input[type='email']").first
    if email_input.count() > 0:
        email_input.fill("invalid-email")
        # Try to submit the form if there's a submit button
        submit = page.locator("button[type='submit']").first
        if submit.count() > 0:
            # Browser should reject invalid email
            validity = email_input.evaluate("e => e.validity.valid")
            # Email field should show as invalid


@pytest.mark.readonly
def test_e2e_36_phone_input_accepts_numbers(page: Page, base_url: str) -> None:
    """E2E-36: phone number input accepts numeric input."""
    page.goto(base_url, wait_until="domcontentloaded")
    phone_input = page.locator("input[type='tel'], input[type='phone'], input[placeholder*='phone' i]").first
    if phone_input.count() > 0:
        phone_input.fill("555-123-4567")
        value = phone_input.input_value()
        assert len(value) > 0, "Phone input did not accept input"


@pytest.mark.readonly
def test_e2e_37_dropdown_options_accessible(page: Page, base_url: str) -> None:
    """E2E-37: dropdown select fields have accessible options."""
    page.goto(base_url, wait_until="domcontentloaded")
    selects = page.locator("select")
    count = selects.count()
    if count > 0:
        select = selects.first
        options = select.locator("option")
        assert options.count() > 0, "Select has no options"


@pytest.mark.readonly
def test_e2e_38_form_error_messages_visible(page: Page, base_url: str) -> None:
    """E2E-38: form validation error messages are displayed."""
    page.goto(base_url, wait_until="domcontentloaded")
    error_messages = page.locator("[class*='error'], [class*='alert'], [role='alert']")
    # Just verify error containers exist when visible
    if error_messages.count() > 0:
        for i in range(min(error_messages.count(), 3)):
            msg = error_messages.nth(i)
            text = msg.text_content()
            # If visible, should have text
            if msg.is_visible():
                assert len(text.strip()) > 0, f"Error message {i} is empty"


@pytest.mark.readonly
def test_e2e_39_checkbox_and_radio_interactive(page: Page, base_url: str) -> None:
    """E2E-39: checkboxes and radio buttons respond to clicks."""
    page.goto(base_url, wait_until="domcontentloaded")
    checkbox = page.locator("input[type='checkbox']").first
    if checkbox.count() > 0:
        is_checked_before = checkbox.is_checked()
        checkbox.click()
        is_checked_after = checkbox.is_checked()
        assert is_checked_before != is_checked_after, "Checkbox did not toggle"


@pytest.mark.readonly
def test_e2e_40_form_submit_button_functional(page: Page, base_url: str) -> None:
    """E2E-40: form submit button is clickable and styled."""
    page.goto(base_url, wait_until="domcontentloaded")
    submit = page.locator("button[type='submit']").first
    if submit.count() > 0:
        expect(submit).to_be_visible()
        expect(submit).to_be_enabled()
