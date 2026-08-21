"""Shared fixtures for the black-box E2E suite.

The target under test is external and production. Two rules are enforced here
rather than left to reviewer discipline:

1. There is no default base URL. An unset E2E_BASE_URL fails loudly instead of
   silently pointing the suite at localhost or a hardcoded host.
2. The suite is read-only by default. Tests that would write a record must be
   marked and are deselected unless E2E_ALLOW_WRITES is explicitly set.
"""

import os

import pytest


@pytest.fixture(scope="session")
def base_url() -> str:
    """Target base URL. Deliberately has no fallback."""
    url = os.environ.get("E2E_BASE_URL", "").strip()
    if not url:
        raise RuntimeError(
            "E2E_BASE_URL is not set. Point it at the target under test, e.g.\n"
            "  E2E_BASE_URL=https://www.alignmenthealthplan.com\n"
            "There is no default on purpose - a silent fallback makes a green "
            "run meaningless."
        )
    return url.rstrip("/")


@pytest.fixture(scope="session")
def writes_allowed() -> bool:
    """True only when the operator has opted into state-changing tests."""
    return os.environ.get("E2E_ALLOW_WRITES", "").strip().lower() in {"1", "true", "yes"}


@pytest.fixture(scope="session")
def browser_context_args():
    """Configure browser context to ignore HTTPS errors for production testing."""
    return {
        "ignore_https_errors": True,
    }


def pytest_collection_modifyitems(config, items):
    """Skip write-performing tests unless writes are explicitly enabled.

    Against a third-party production site, submitting a form creates a real
    record. Tests that do so carry @pytest.mark.writes and stay deselected by
    default; they report as SKIPPED, which the reporting contract treats as
    non-green rather than as coverage.
    """
    if os.environ.get("E2E_ALLOW_WRITES", "").strip().lower() in {"1", "true", "yes"}:
        return
    skip = pytest.mark.skip(
        reason="write-performing test: set E2E_ALLOW_WRITES=1 on an environment you own"
    )
    for item in items:
        if "writes" in item.keywords:
            item.add_marker(skip)


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "writes: performs a state-changing action; skipped unless E2E_ALLOW_WRITES=1"
    )
