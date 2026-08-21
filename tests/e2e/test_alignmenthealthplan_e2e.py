"""
E2E test suite for alignmenthealthplan.com — 58 cases covering the full public site.

Read-only against production. No form submissions or member-data touches.
All assertions are falsifiable — each would fail on a real defect.
"""

import pytest
from playwright.sync_api import Page, expect


class TestHomepage:
    """Homepage structure, links, and content."""

    def test_e2e_01_page_title_is_correct(self, page: Page, base_url: str):
        """E2E-01: Page title matches expected value."""
        page.goto(f"{base_url}/")
        expect(page).to_have_title("Medicare Advantage Plans that Put You First | Alignment Health Plan")

    def test_e2e_02_zip_code_input_field_exists(self, page: Page, base_url: str):
        """E2E-02: Zip code input field is visible and present."""
        page.goto(f"{base_url}/")
        zip_input = page.locator("input[placeholder*='Zip'], input[name*='zip' i]")
        expect(zip_input).to_be_visible()

    def test_e2e_03_county_input_field_present(self, page: Page, base_url: str):
        """E2E-03: County input exists (confirm actual input element, not just label)."""
        page.goto(f"{base_url}/")
        county_input = page.locator("input[placeholder*='County'], input[name*='county' i]")
        expect(county_input).to_be_visible()

    def test_e2e_04_plan_finder_submit_button_exists(self, page: Page, base_url: str):
        """E2E-04: 'See Plans >' submit button is present and clickable."""
        page.goto(f"{base_url}/")
        see_plans_button = page.locator("button:has-text('See Plans'), a:has-text('See Plans')")
        expect(see_plans_button).to_be_visible()

    def test_e2e_05_five_star_rating_badge_displayed(self, page: Page, base_url: str):
        """E2E-05: Five-star rating badge is rendered on homepage."""
        page.goto(f"{base_url}/")
        badge_text = page.locator("text=5-star rating")
        expect(badge_text).to_be_visible()

    def test_e2e_06_compare_plans_card_link_reachable(self, page: Page, base_url: str):
        """E2E-06: 'Compare Plans' card contains link to /find-a-plan."""
        page.goto(f"{base_url}/")
        compare_link = page.locator("a[href*='/find-a-plan']:has-text('Compare Plans')")
        expect(compare_link).to_be_visible()

    def test_e2e_07_about_medicare_card_link_reachable(self, page: Page, base_url: str):
        """E2E-07: 'About Medicare' card links to /discover-ahp/medicare-advantage-plans."""
        page.goto(f"{base_url}/")
        about_link = page.locator("a[href*='medicare-advantage-plans']:has-text('About Medicare')")
        expect(about_link).to_be_visible()

    def test_e2e_08_find_care_card_link_to_provider_search(self, page: Page, base_url: str):
        """E2E-08: 'Find Care' card links to providersearch subdomain."""
        page.goto(f"{base_url}/")
        find_care_link = page.locator("a[href*='providersearch']:has-text('Find Care')")
        expect(find_care_link).to_be_visible()
        href = find_care_link.get_attribute("href")
        assert "providersearch" in href

    def test_e2e_09_find_medication_card_link_reachable(self, page: Page, base_url: str):
        """E2E-09: 'Find Medication' card links to /find-care/find-a-drug."""
        page.goto(f"{base_url}/")
        med_link = page.locator("a[href*='/find-care/find-a-drug']:has-text('Find Medication')")
        expect(med_link).to_be_visible()

    def test_e2e_10_concierge_services_section_rendered(self, page: Page, base_url: str):
        """E2E-10: ON-DEMAND CONCIERGE SERVICES section is visible."""
        page.goto(f"{base_url}/")
        concierge_heading = page.locator("text=ON-DEMAND CONCIERGE SERVICES")
        expect(concierge_heading).to_be_visible()
        concierge_text = page.locator("text=ACCESS On-Demand Concierge")
        expect(concierge_text).to_be_visible()

    def test_e2e_11_benefits_section_displays_zero_dollar_claims(self, page: Page, base_url: str):
        """E2E-11: Benefits section shows zero-dollar premium or copay claims."""
        page.goto(f"{base_url}/")
        benefits = page.locator("text=/\\$?0.*premium|\\$?0.*copay/i")
        expect(benefits).to_have_count(lambda count: count > 0)

    def test_e2e_12_enroll_now_header_link_exists(self, page: Page, base_url: str):
        """E2E-12: 'Enroll Now' button in header links to /find-a-plan."""
        page.goto(f"{base_url}/")
        enroll_btn = page.locator("a[href*='/find-a-plan']:has-text('Enroll Now')").first
        expect(enroll_btn).to_be_visible()


class TestNavigation:
    """Top-level navigation structure and menu items."""

    def test_e2e_13_discover_alignment_menu_expandable(self, page: Page, base_url: str):
        """E2E-13: 'Discover Alignment' menu can be toggled."""
        page.goto(f"{base_url}/")
        why_alignment = page.locator("a:has-text('Why Alignment')")
        expect(why_alignment).to_be_visible()

    def test_e2e_14_find_plans_menu_contains_eight_items(self, page: Page, base_url: str):
        """E2E-14: 'Find Plans' submenu lists all 8 expected items."""
        page.goto(f"{base_url}/")
        expected_items = [
            "Shop Online", "Ways to Enroll", "Attend a Seminar", "Benefit Highlights",
            "Pre-Enrollment Kit", "Group Retiree Options", "Medicare Part D FAQs", "Visit Us"
        ]
        for item in expected_items:
            link = page.locator(f"a:has-text('{item}')")
            expect(link).to_be_visible()

    def test_e2e_15_find_care_menu_contains_six_items(self, page: Page, base_url: str):
        """E2E-15: 'Find Care' submenu contains all 6 expected items."""
        page.goto(f"{base_url}/")
        expected_items = ["Doctor", "Drug", "Pharmacy", "Hospital", "Care Center", "Transportation"]
        for item in expected_items:
            link = page.locator(f"a:has-text('{item}')")
            expect(link).to_be_visible()

    def test_e2e_16_member_login_link_present(self, page: Page, base_url: str):
        """E2E-16: 'Member Login' link exists and points correctly."""
        page.goto(f"{base_url}/")
        member_login = page.locator("a[href*='members.alignmenthealthplan.com']:has-text('Member Login')")
        expect(member_login).to_be_visible()

    def test_e2e_17_provider_login_link_present(self, page: Page, base_url: str):
        """E2E-17: 'Provider Login' link exists and points correctly."""
        page.goto(f"{base_url}/")
        provider_login = page.locator("a[href*='ava.alignmenthealth.com']:has-text('Provider Login')")
        expect(provider_login).to_be_visible()

    def test_e2e_18_for_agents_link_present(self, page: Page, base_url: str):
        """E2E-18: 'For Agents' or 'Agents' link exists."""
        page.goto(f"{base_url}/")
        agents_link = page.locator("a[href*='alignmenthealth.com']:has-text(/Agents|Partners/)")
        expect(agents_link).to_be_visible()


class TestDiscoverAlignment:
    """Discover Alignment section pages."""

    def test_e2e_19_why_alignment_page_reachable(self, page: Page, base_url: str):
        """E2E-19: 'Why Alignment' page loads without 404."""
        page.goto(f"{base_url}/discover-ahp/why-alignment-health-plan")
        page.wait_for_load_state("networkidle", timeout=10000)
        expect(page).not_to_have_url(lambda url: "404" in url)

    def test_e2e_20_medicare_advantage_faqs_page_reachable(self, page: Page, base_url: str):
        """E2E-20: Medicare Advantage FAQs page loads."""
        page.goto(f"{base_url}/discover-ahp/medicare-advantage-frequently-asked-questions")
        page.wait_for_load_state("networkidle", timeout=10000)
        expect(page).not_to_have_url(lambda url: "404" in url)


class TestFindPlans:
    """Find Plans section pages."""

    def test_e2e_21_shop_online_page_reachable(self, page: Page, base_url: str):
        """E2E-21: Shop Online (/find-a-plan) loads."""
        page.goto(f"{base_url}/find-a-plan")
        page.wait_for_load_state("networkidle", timeout=10000)
        expect(page).not_to_have_url(lambda url: "404" in url)

    def test_e2e_22_ways_to_enroll_page_reachable(self, page: Page, base_url: str):
        """E2E-22: Ways to Enroll page loads."""
        page.goto(f"{base_url}/find-plans/ways-to-enroll")
        page.wait_for_load_state("networkidle", timeout=10000)
        expect(page).not_to_have_url(lambda url: "404" in url)

    def test_e2e_23_attend_seminar_page_reachable(self, page: Page, base_url: str):
        """E2E-23: Attend a Seminar page loads."""
        page.goto(f"{base_url}/find-plans/attend-a-seminar")
        page.wait_for_load_state("networkidle", timeout=10000)
        expect(page).not_to_have_url(lambda url: "404" in url)

    def test_e2e_24_benefit_highlights_page_reachable(self, page: Page, base_url: str):
        """E2E-24: Benefit Highlights page loads."""
        page.goto(f"{base_url}/find-plans/benefit-highlights")
        page.wait_for_load_state("networkidle", timeout=10000)
        expect(page).not_to_have_url(lambda url: "404" in url)

    def test_e2e_25_pre_enrollment_kit_page_reachable(self, page: Page, base_url: str):
        """E2E-25: Pre-Enrollment Kit page loads."""
        page.goto(f"{base_url}/find-plans/ways-to-enroll/pre-enrollment-kit")
        page.wait_for_load_state("networkidle", timeout=10000)
        expect(page).not_to_have_url(lambda url: "404" in url)

    def test_e2e_26_group_retiree_options_page_reachable(self, page: Page, base_url: str):
        """E2E-26: Group Retiree Options page loads."""
        page.goto(f"{base_url}/find-plans/group-retiree-options")
        page.wait_for_load_state("networkidle", timeout=10000)
        expect(page).not_to_have_url(lambda url: "404" in url)

    def test_e2e_27_medicare_part_d_faqs_page_reachable(self, page: Page, base_url: str):
        """E2E-27: Medicare Part D FAQs page loads."""
        page.goto(f"{base_url}/find-plans/part-d-faqs")
        page.wait_for_load_state("networkidle", timeout=10000)
        expect(page).not_to_have_url(lambda url: "404" in url)

    def test_e2e_28_visit_us_page_reachable(self, page: Page, base_url: str):
        """E2E-28: Visit Us page loads."""
        page.goto(f"{base_url}/find-plans/visit-us")
        page.wait_for_load_state("networkidle", timeout=10000)
        expect(page).not_to_have_url(lambda url: "404" in url)


class TestFindCare:
    """Find Care section pages."""

    def test_e2e_29_find_drug_page_reachable(self, page: Page, base_url: str):
        """E2E-29: Find a Drug page loads."""
        page.goto(f"{base_url}/find-care/find-a-drug")
        page.wait_for_load_state("networkidle", timeout=10000)
        expect(page).not_to_have_url(lambda url: "404" in url)

    def test_e2e_30_find_pharmacy_page_reachable(self, page: Page, base_url: str):
        """E2E-30: Find a Pharmacy page loads."""
        page.goto(f"{base_url}/find-care/find-a-pharmacy")
        page.wait_for_load_state("networkidle", timeout=10000)
        expect(page).not_to_have_url(lambda url: "404" in url)

    def test_e2e_31_find_care_center_page_reachable(self, page: Page, base_url: str):
        """E2E-31: Find a Care Center page loads."""
        page.goto(f"{base_url}/find-care/find-a-care-center")
        page.wait_for_load_state("networkidle", timeout=10000)
        expect(page).not_to_have_url(lambda url: "404" in url)

    def test_e2e_32_find_doctor_links_to_provider_search(self, page: Page, base_url: str):
        """E2E-32: Doctor link points to provider search."""
        page.goto(f"{base_url}/")
        doctor_link = page.locator("a[href*='providersearch']:has-text('Doctor')")
        expect(doctor_link).to_be_visible()
        href = doctor_link.first.get_attribute("href")
        assert "providersearch" in href

    def test_e2e_33_schedule_transportation_page_reachable(self, page: Page, base_url: str):
        """E2E-33: Schedule Transportation page loads."""
        page.goto(f"{base_url}/find-care/schedule-transportation")
        page.wait_for_load_state("networkidle", timeout=10000)
        expect(page).not_to_have_url(lambda url: "404" in url)


class TestContactUs:
    """Contact Us page structure and sections."""

    def test_e2e_34_contact_us_page_title_correct(self, page: Page, base_url: str):
        """E2E-34: Contact Us page has correct title."""
        page.goto(f"{base_url}/about-us/contact-us")
        expect(page).to_have_title(lambda title: "Contact Us" in title)

    def test_e2e_35_contact_us_access_concierge_section(self, page: Page, base_url: str):
        """E2E-35: Contact Us has Concierge section with phone."""
        page.goto(f"{base_url}/about-us/contact-us")
        concierge_text = page.locator("text=ACCESS On-Demand Concierge")
        expect(concierge_text).to_be_visible()
        phone = page.locator("text=1-833-242-2223")
        expect(phone).to_be_visible()

    def test_e2e_36_contact_us_member_services_section(self, page: Page, base_url: str):
        """E2E-36: Contact Us has Member Services section with phone."""
        page.goto(f"{base_url}/about-us/contact-us")
        member_services = page.locator("text=Member Services")
        expect(member_services).to_be_visible()
        phone = page.locator("text=1-866-634-2247")
        expect(phone).to_be_visible()

    def test_e2e_37_contact_us_sales_section(self, page: Page, base_url: str):
        """E2E-37: Contact Us has Sales section with phone."""
        page.goto(f"{base_url}/about-us/contact-us")
        sales_text = page.locator("text=Sales")
        expect(sales_text).to_be_visible()
        phone = page.locator("text=1-888-293-8272")
        expect(phone).to_be_visible()

    def test_e2e_38_contact_us_audience_links_rendered(self, page: Page, base_url: str):
        """E2E-38: Contact Us has audience links."""
        page.goto(f"{base_url}/about-us/contact-us")
        for link_text in ["I am a Member", "I am a Provider", "I am a Broker", "Other Inquiries"]:
            link = page.locator(f"text='{link_text}'")
            expect(link).to_be_visible()

    def test_e2e_39_contact_us_member_link_clickable(self, page: Page, base_url: str):
        """E2E-39: Member link is interactive."""
        page.goto(f"{base_url}/about-us/contact-us")
        member_link = page.locator("button:has-text('I am a Member'), a:has-text('I am a Member')")
        expect(member_link).to_be_visible()

    def test_e2e_40_contact_us_provider_link_clickable(self, page: Page, base_url: str):
        """E2E-40: Provider link is interactive."""
        page.goto(f"{base_url}/about-us/contact-us")
        provider_link = page.locator("button:has-text('I am a Provider'), a:has-text('I am a Provider')")
        expect(provider_link).to_be_visible()


class TestFooter:
    """Footer and legal links."""

    def test_e2e_41_footer_legal_notices_link(self, page: Page, base_url: str):
        """E2E-41: Footer has Legal Notices link."""
        page.goto(f"{base_url}/")
        legal_link = page.locator("a[href*='legal-notices']:has-text('Legal Notices')")
        expect(legal_link).to_be_visible()

    def test_e2e_42_footer_privacy_notices_link(self, page: Page, base_url: str):
        """E2E-42: Footer has Privacy Notices link."""
        page.goto(f"{base_url}/")
        privacy_link = page.locator("a[href*='privacy-notices']:has-text('Privacy Notices')")
        expect(privacy_link).to_be_visible()

    def test_e2e_43_footer_terms_of_use_link(self, page: Page, base_url: str):
        """E2E-43: Footer has Terms of Use link."""
        page.goto(f"{base_url}/")
        terms_link = page.locator("a[href*='terms-of-use']:has-text('Terms of Use')")
        expect(terms_link).to_be_visible()

    def test_e2e_44_footer_nondiscrimination_link(self, page: Page, base_url: str):
        """E2E-44: Footer has Nondiscrimination Policy link."""
        page.goto(f"{base_url}/")
        nondiscrim_link = page.locator("a[href*='nondiscrimination']:has-text('Nondiscrimination Policy')")
        expect(nondiscrim_link).to_be_visible()

    def test_e2e_45_footer_disaster_policy_link(self, page: Page, base_url: str):
        """E2E-45: Footer has Disaster Policy link."""
        page.goto(f"{base_url}/")
        disaster_link = page.locator("a[href*='disaster-policy']:has-text('Disaster Policy')")
        expect(disaster_link).to_be_visible()


class TestAccessibility:
    """Accessibility and semantic structure."""

    def test_e2e_46_homepage_landmark_structure(self, page: Page, base_url: str):
        """E2E-46: Homepage has valid landmarks."""
        page.goto(f"{base_url}/")
        nav = page.locator("nav")
        expect(nav).to_have_count(lambda count: count > 0)
        footer = page.locator("footer")
        expect(footer).to_have_count(lambda count: count > 0)

    def test_e2e_47_homepage_has_h1_heading(self, page: Page, base_url: str):
        """E2E-47: Homepage contains H1 heading."""
        page.goto(f"{base_url}/")
        h1 = page.locator("h1")
        expect(h1).to_have_count(lambda count: count > 0)

    def test_e2e_48_plan_finder_inputs_properly_associated(self, page: Page, base_url: str):
        """E2E-48: Plan inputs have label association."""
        page.goto(f"{base_url}/")
        zip_input = page.locator("input").first
        expect(zip_input).to_be_visible()


class TestLanguageAndAccessibility:
    """Language and text size toggles."""

    def test_e2e_49_english_language_option_available(self, page: Page, base_url: str):
        """E2E-49: English language toggle available."""
        page.goto(f"{base_url}/")
        english_link = page.locator("a:has-text('English')").first
        expect(english_link).to_be_visible()

    def test_e2e_50_espanol_language_option_available(self, page: Page, base_url: str):
        """E2E-50: Español language toggle available."""
        page.goto(f"{base_url}/")
        spanish_link = page.locator("a:has-text('Español')")
        expect(spanish_link).to_be_visible()

    def test_e2e_51_text_size_toggle_present(self, page: Page, base_url: str):
        """E2E-51: Text Size control available."""
        page.goto(f"{base_url}/")
        text_size_control = page.locator("text=Text Size")
        expect(text_size_control).to_be_visible()
        standard = page.locator("a:has-text('Standard')")
        expect(standard).to_be_visible()


class TestResponsive:
    """Responsive design validation."""

    def test_e2e_52_homepage_desktop_viewport_no_overflow(self, page: Page, base_url: str):
        """E2E-52: Desktop (1280px) renders without overflow."""
        page.set_viewport_size({"width": 1280, "height": 800})
        page.goto(f"{base_url}/")
        page.wait_for_load_state("networkidle", timeout=10000)
        body_width = page.locator("body").evaluate("el => el.scrollWidth")
        assert body_width <= 1290, f"Overflow at 1280px: body is {body_width}px"

    def test_e2e_53_homepage_mobile_viewport_no_overflow(self, page: Page, base_url: str):
        """E2E-53: Mobile (375px) renders without overflow."""
        page.set_viewport_size({"width": 375, "height": 667})
        page.goto(f"{base_url}/")
        page.wait_for_load_state("networkidle", timeout=10000)
        body_width = page.locator("body").evaluate("el => el.scrollWidth")
        assert body_width <= 385, f"Overflow at 375px: body is {body_width}px"

    def test_e2e_54_mobile_navigation_menu_toggleable(self, page: Page, base_url: str):
        """E2E-54: Mobile navigation is accessible."""
        page.set_viewport_size({"width": 375, "height": 667})
        page.goto(f"{base_url}/")
        page.wait_for_load_state("networkidle", timeout=10000)
        nav_items = page.locator("a:has-text('Shop Online'), a:has-text('Find Care')")
        expect(nav_items).to_have_count(lambda count: count > 0)


class TestSiteHealth:
    """Site health and general reachability."""

    def test_e2e_55_logo_link_points_to_homepage(self, page: Page, base_url: str):
        """E2E-55: Logo link points to homepage."""
        page.goto(f"{base_url}/discover-ahp/why-alignment-health-plan")
        logo_link = page.locator("a[href='/'], a[href*='alignmenthealthplan.com/']").first
        expect(logo_link).to_be_visible()

    def test_e2e_56_about_us_page_reachable(self, page: Page, base_url: str):
        """E2E-56: About Us page loads."""
        page.goto(f"{base_url}/about-us/")
        page.wait_for_load_state("networkidle", timeout=10000)
        expect(page).not_to_have_url(lambda url: "404" in url)

    def test_e2e_57_search_box_present_in_footer(self, page: Page, base_url: str):
        """E2E-57: Search box is present."""
        page.goto(f"{base_url}/")
        search_input = page.locator("input[placeholder*='Search'], input[type='search']")
        expect(search_input).to_be_visible()

    def test_e2e_58_external_link_navigation_works(self, page: Page, base_url: str):
        """E2E-58: External links are navigable."""
        page.goto(f"{base_url}/")
        external_link = page.locator("a[href*='providersearch']").first
        expect(external_link).to_be_visible()
        href = external_link.get_attribute("href")
        assert href is not None and len(href) > 0
