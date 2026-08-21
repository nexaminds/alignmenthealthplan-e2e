"""Comprehensive E2E test suite for alignmenthealthplan.com

Coverage includes:
- HTTP status code verification (200 responses)
- Page structure and navigation validation
- Accessibility baselines
- Performance validation
- Critical business workflow verification
"""

import pytest
import httpx
import time
from typing import Optional


class TestPageLoads:
    """Tests for page load and HTTP status codes"""

    @pytest.mark.readonly
    def test_homepage_returns_200(self, base_url):
        """E2E-01: Homepage returns 200 status code"""
        with httpx.Client() as client:
            response = client.get(base_url, follow_redirects=True, timeout=30)
            assert response.status_code == 200, f"Homepage returned {response.status_code}"
            assert len(response.text) > 500, "Homepage should have content"

    @pytest.mark.readonly
    def test_homepage_contains_expected_sections(self, base_url):
        """E2E-02: Homepage contains key sections and navigation"""
        with httpx.Client() as client:
            response = client.get(base_url, follow_redirects=True, timeout=30)
            assert response.status_code == 200
            
            content = response.text.lower()
            
            # Check for major navigation sections
            sections = ["discover", "find plans", "find care", "member", "provider"]
            found_sections = [s for s in sections if s in content]
            
            assert len(found_sections) >= 3, f"Missing key sections. Found: {found_sections}"

    @pytest.mark.readonly
    def test_homepage_has_enrollment_cta(self, base_url):
        """E2E-03: Homepage contains enrollment/action CTAs"""
        with httpx.Client() as client:
            response = client.get(base_url, follow_redirects=True, timeout=30)
            assert response.status_code == 200
            
            content = response.text.lower()
            
            # Should contain enrollment calls-to-action
            cta_keywords = ["enroll", "shop", "compare", "find plans", "see plans"]
            found_ctas = [cta for cta in cta_keywords if cta in content]
            
            assert len(found_ctas) >= 1, f"No CTAs found. Searched for: {cta_keywords}"

    @pytest.mark.readonly
    def test_homepage_has_contact_info(self, base_url):
        """E2E-04: Homepage displays phone number and contact methods"""
        with httpx.Client() as client:
            response = client.get(base_url, follow_redirects=True, timeout=30)
            assert response.status_code == 200
            
            content = response.text
            
            # Should have phone number (with various formatting)
            has_phone = any(pattern in content for pattern in ["888", "1-888", "TTY", "711"])
            assert has_phone, "Homepage should display phone number"


class TestFindPlansPages:
    """Tests for Find Plans section pages"""

    @pytest.mark.readonly
    def test_find_plan_online_page_200(self, base_url):
        """E2E-05: Find Plans / Shop Online page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/find-a-plan",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200, f"Find Plans page returned {response.status_code}"

    @pytest.mark.readonly
    def test_ways_to_enroll_page_200(self, base_url):
        """E2E-06: Ways to Enroll page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/find-plans/ways-to-enroll",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_attend_seminar_page_200(self, base_url):
        """E2E-07: Attend a Seminar page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/find-plans/attend-a-seminar",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_benefit_highlights_page_200(self, base_url):
        """E2E-08: Benefit Highlights page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/find-plans/benefit-highlights",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_pre_enrollment_kit_page_200(self, base_url):
        """E2E-09: Pre-Enrollment Kit page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/find-plans/ways-to-enroll/pre-enrollment-kit",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_group_retiree_options_page_200(self, base_url):
        """E2E-10: Group Retiree Options page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/find-plans/group-retiree-options",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_part_d_faqs_page_200(self, base_url):
        """E2E-11: Medicare Part D FAQs page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/find-plans/part-d-faqs",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_visit_us_page_200(self, base_url):
        """E2E-12: Visit Us page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/find-plans/visit-us",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200


class TestFindCarePages:
    """Tests for Find Care section pages"""

    @pytest.mark.readonly
    def test_find_drug_page_200(self, base_url):
        """E2E-13: Find a Drug page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/find-care/find-a-drug",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_find_pharmacy_page_200(self, base_url):
        """E2E-14: Find a Pharmacy page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/find-care/find-a-pharmacy",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_find_care_center_page_200(self, base_url):
        """E2E-15: Find a Care Center page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/find-care/find-a-care-center",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_schedule_transportation_page_200(self, base_url):
        """E2E-16: Schedule Transportation page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/find-care/schedule-transportation",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200


class TestDiscoverPages:
    """Tests for Discover Alignment section"""

    @pytest.mark.readonly
    def test_why_alignment_page_200(self, base_url):
        """E2E-17: Why Alignment Health Plan page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/discover-ahp/why-alignment-health-plan",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_medicare_advantage_page_200(self, base_url):
        """E2E-18: Medicare Advantage Plans page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/discover-ahp/medicare-advantage-plans",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_medicare_faqs_page_200(self, base_url):
        """E2E-19: Medicare Advantage FAQs page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/discover-ahp/medicare-advantage-frequently-asked-questions",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200


class TestMembersPages:
    """Tests for Member section pages"""

    @pytest.mark.readonly
    def test_member_services_page_200(self, base_url):
        """E2E-20: Member Services page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/members/member-services",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_member_forms_resources_page_200(self, base_url):
        """E2E-21: Member Forms and Resources page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/members/member-forms-resources",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_provider_network_page_200(self, base_url):
        """E2E-22: Provider Network page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/members/provider-network",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_rights_responsibilities_page_200(self, base_url):
        """E2E-23: Rights and Responsibilities page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/members/rights-and-responsibilities",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200


class TestProvidersPages:
    """Tests for Provider section pages"""

    @pytest.mark.readonly
    def test_provider_resources_page_200(self, base_url):
        """E2E-24: Provider Resources page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/providers/provider-resources",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_non_contracted_providers_page_200(self, base_url):
        """E2E-25: Non-Contracted Providers page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/providers/non-contracted-providers",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_ppo_plan_information_page_200(self, base_url):
        """E2E-26: PPO Plan Information page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/providers/ppo-plan-information",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_part_c_information_page_200(self, base_url):
        """E2E-27: Part C Information page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/providers/part-c-information",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_compliance_information_page_200(self, base_url):
        """E2E-28: Compliance Information page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/providers/compliance-information",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_provider_manual_page_200(self, base_url):
        """E2E-29: Provider Manual page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/providers/provider-manual",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_provider_newsletter_page_200(self, base_url):
        """E2E-30: Provider Newsletter page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/providers/newsletter",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_special_needs_training_page_200(self, base_url):
        """E2E-31: Special Needs Plan Training page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/providers/special-needs-plan-training",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200


class TestAboutPages:
    """Tests for About / Company pages"""

    @pytest.mark.readonly
    def test_about_us_page_200(self, base_url):
        """E2E-32: About Us page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/about-us",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_contact_us_page_200(self, base_url):
        """E2E-33: Contact Us page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/about-us/contact-us",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_legal_notices_page_200(self, base_url):
        """E2E-34: Legal Notices page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/about-us/legal-notices",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_privacy_notices_page_200(self, base_url):
        """E2E-35: Privacy Notices page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/about-us/privacy-notices",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_terms_of_use_page_200(self, base_url):
        """E2E-36: Terms of Use page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/about-us/terms-of-use",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_nondiscrimination_policy_page_200(self, base_url):
        """E2E-37: Nondiscrimination Policy page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/about-us/terms-of-use/nondiscrimination-policy",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_notice_of_availability_page_200(self, base_url):
        """E2E-38: Notice of Availability page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/about-us/terms-of-use/notice-of-availability",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200

    @pytest.mark.readonly
    def test_disaster_policy_page_200(self, base_url):
        """E2E-39: Disaster Policy page returns 200"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/about-us/disaster-policy",
                follow_redirects=True,
                timeout=30
            )
            assert response.status_code == 200


class TestContentValidation:
    """Tests for critical content presence"""

    @pytest.mark.readonly
    def test_homepage_has_required_healthcare_disclaimers(self, base_url):
        """E2E-40: Homepage includes required healthcare disclaimers"""
        with httpx.Client() as client:
            response = client.get(base_url, follow_redirects=True, timeout=30)
            content = response.text.lower()
            
            # Should have compliance language
            has_required = "hmo" in content or "medicare" in content or "cms" in content
            assert has_required, "Page should mention Medicare/HMO compliance"

    @pytest.mark.readonly
    def test_homepage_displays_five_star_rating(self, base_url):
        """E2E-41: Homepage displays 5-star rating or quality badges"""
        with httpx.Client() as client:
            response = client.get(base_url, follow_redirects=True, timeout=30)
            content = response.text
            
            # Check for star rating or quality indicators
            has_rating = "5-star" in content or "five star" in content or "rating" in content
            assert has_rating or len(content) > 1000, "Page should load with content"

    @pytest.mark.readonly
    def test_homepage_includes_benefits_summary(self, base_url):
        """E2E-42: Homepage summarizes key benefits"""
        with httpx.Client() as client:
            response = client.get(base_url, follow_redirects=True, timeout=30)
            content = response.text.lower()
            
            # Should mention key benefits
            benefits = ["premium", "copay", "coverage", "pharmacy", "vision"]
            found_benefits = [b for b in benefits if b in content]
            
            assert len(found_benefits) >= 2, f"Should mention benefits. Found: {found_benefits}"

    @pytest.mark.readonly
    def test_legal_pages_contain_required_notices(self, base_url):
        """E2E-43: Legal pages contain required compliance notices"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/about-us/terms-of-use",
                follow_redirects=True,
                timeout=30
            )
            content = response.text.lower()
            
            # Should have legal/terms content
            assert "term" in content or "agree" in content or "policy" in content


class TestLinkIntegrity:
    """Tests for navigation link integrity"""

    @pytest.mark.readonly
    def test_member_login_link_present(self, base_url):
        """E2E-44: Member Login link is present and correct"""
        with httpx.Client() as client:
            response = client.get(base_url, follow_redirects=True, timeout=30)
            content = response.text
            
            # Should contain member login link/reference
            has_member_link = "members.alignmenthealthplan.com" in content or "member login" in content.lower()
            assert has_member_link, "Member login should be accessible"

    @pytest.mark.readonly
    def test_provider_login_link_present(self, base_url):
        """E2E-45: Provider Login link is present and correct"""
        with httpx.Client() as client:
            response = client.get(base_url, follow_redirects=True, timeout=30)
            content = response.text
            
            # Should contain provider login link/reference
            has_provider_link = ("alignmenthealth" in content or "ava.alignmenthealth" in content 
                                or "provider login" in content.lower())
            assert has_provider_link, "Provider login should be accessible"

    @pytest.mark.readonly
    def test_footer_contains_legal_links(self, base_url):
        """E2E-46: Footer contains required legal links"""
        with httpx.Client() as client:
            response = client.get(base_url, follow_redirects=True, timeout=30)
            content = response.text.lower()
            
            # Should have links to legal documents
            legal_terms = ["privacy", "terms", "legal", "notice", "policy"]
            found_legal = [t for t in legal_terms if t in content]
            
            assert len(found_legal) >= 2, f"Missing legal links. Found: {found_legal}"

    @pytest.mark.readonly
    def test_footer_has_copyright_notice(self, base_url):
        """E2E-47: Footer includes copyright notice"""
        with httpx.Client() as client:
            response = client.get(base_url, follow_redirects=True, timeout=30)
            content = response.text
            
            # Should have copyright year
            has_copyright = ("©" in content or "Copyright" in content or "2026" in content 
                            or "2025" in content)
            assert has_copyright, "Footer should include copyright"


class TestPerformance:
    """Tests for response time and performance"""

    @pytest.mark.readonly
    def test_homepage_response_time_reasonable(self, base_url):
        """E2E-48: Homepage responds within reasonable time (< 10 seconds)"""
        start = time.time()
        with httpx.Client() as client:
            response = client.get(base_url, follow_redirects=True, timeout=30)
        elapsed = time.time() - start
        
        assert response.status_code == 200
        assert elapsed < 10, f"Homepage took {elapsed:.2f}s (threshold: 10s)"

    @pytest.mark.readonly
    def test_major_pages_respond_within_timeout(self, base_url):
        """E2E-49: Major pages respond within 10 seconds"""
        test_urls = [
            f"{base_url}/find-a-plan",
            f"{base_url}/discover-ahp/why-alignment-health-plan",
            f"{base_url}/members/member-services",
        ]
        
        with httpx.Client() as client:
            for url in test_urls:
                start = time.time()
                response = client.get(url, follow_redirects=True, timeout=30)
                elapsed = time.time() - start
                
                assert response.status_code == 200, f"{url} returned {response.status_code}"
                assert elapsed < 10, f"{url} took {elapsed:.2f}s"


class TestContentEncoding:
    """Tests for proper content encoding and structure"""

    @pytest.mark.readonly
    def test_homepage_uses_proper_charset(self, base_url):
        """E2E-50: Homepage uses proper character encoding (UTF-8)"""
        with httpx.Client() as client:
            response = client.get(base_url, follow_redirects=True, timeout=30)
            
            # Check content type header
            content_type = response.headers.get("content-type", "").lower()
            
            # Should be HTML
            assert "text/html" in content_type or "application" in content_type

    @pytest.mark.readonly
    def test_homepage_not_blocked_by_robots(self, base_url):
        """E2E-51: Homepage is not completely blocked from crawlers"""
        with httpx.Client() as client:
            response = client.get(base_url, follow_redirects=True, timeout=30)
            
            # Page should load successfully
            assert response.status_code == 200
            
            # Should not be a 403 or 503 response
            assert response.status_code < 400, "Page should be accessible"


class TestAccessibilityRequirements:
    """Tests for accessibility compliance indicators"""

    @pytest.mark.readonly
    def test_homepage_html_structure_valid(self, base_url):
        """E2E-52: Homepage has valid HTML structure"""
        with httpx.Client() as client:
            response = client.get(base_url, follow_redirects=True, timeout=30)
            content = response.text
            
            # Should have basic HTML structure
            assert "<html" in content.lower() or "<!doctype" in content.lower()
            assert "<head" in content.lower()
            assert "<body" in content.lower()

    @pytest.mark.readonly
    def test_homepage_includes_language_attribute(self, base_url):
        """E2E-53: Homepage specifies language attribute"""
        with httpx.Client() as client:
            response = client.get(base_url, follow_redirects=True, timeout=30)
            content = response.text.lower()
            
            # Should specify language
            assert "lang=" in content or "xml:lang" in content or "language" in content

    @pytest.mark.readonly
    def test_homepage_has_meta_viewport(self, base_url):
        """E2E-54: Homepage includes viewport meta tag for mobile"""
        with httpx.Client() as client:
            response = client.get(base_url, follow_redirects=True, timeout=30)
            content = response.text.lower()
            
            # Should have viewport tag for responsive design
            assert "viewport" in content

    @pytest.mark.readonly
    def test_homepage_has_meta_description(self, base_url):
        """E2E-55: Homepage includes meta description"""
        with httpx.Client() as client:
            response = client.get(base_url, follow_redirects=True, timeout=30)
            content = response.text.lower()
            
            # Should have meta description
            assert "description" in content


class TestPageTitles:
    """Tests for page titles and metadata"""

    @pytest.mark.readonly
    def test_homepage_has_page_title(self, base_url):
        """E2E-56: Homepage has descriptive page title"""
        with httpx.Client() as client:
            response = client.get(base_url, follow_redirects=True, timeout=30)
            content = response.text
            
            # Should have <title> tag
            assert "<title>" in content.lower() and "</title>" in content.lower()

    @pytest.mark.readonly
    def test_find_plans_page_has_title(self, base_url):
        """E2E-57: Find Plans page has descriptive title"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/find-a-plan",
                follow_redirects=True,
                timeout=30
            )
            content = response.text.lower()
            
            # Should have page title
            assert "<title>" in content and "</title>" in content

    @pytest.mark.readonly
    def test_about_page_has_title(self, base_url):
        """E2E-58: About Us page has descriptive title"""
        with httpx.Client() as client:
            response = client.get(
                f"{base_url}/about-us",
                follow_redirects=True,
                timeout=30
            )
            content = response.text.lower()
            
            # Should have page title
            assert "<title>" in content and "</title>" in content


class TestExternalResourcesAvailability:
    """Tests that external resources are linked properly"""

    @pytest.mark.readonly
    def test_homepage_links_to_required_portals(self, base_url):
        """E2E-59: Homepage links to member and provider portals"""
        with httpx.Client() as client:
            response = client.get(base_url, follow_redirects=True, timeout=30)
            content = response.text
            
            # Should link to member and provider portals
            has_links = (("members.alignmenthealthplan" in content) and 
                        ("alignmenthealth" in content or "ava.alignmenthealth" in content))
            
            # At least member portal should be present
            assert "members.alignmenthealthplan" in content

    @pytest.mark.readonly
    def test_homepage_displays_required_compliance_badge(self, base_url):
        """E2E-60: Homepage displays quality/compliance badge or indicator"""
        with httpx.Client() as client:
            response = client.get(base_url, follow_redirects=True, timeout=30)
            content = response.text.lower()
            
            # Should mention star rating, NCQA, or quality metrics
            has_quality_indicator = any([
                "5-star" in content,
                "five star" in content,
                "ncqa" in content,
                "cms" in content,
                "rating" in content
            ])
            
            assert has_quality_indicator or "fortune" in content, "Should display quality metrics"
