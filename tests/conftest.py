"""
Pytest configuration and shared fixtures for Revenium Ollama middleware tests.
"""

import os
import pytest


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """
    Configure environment variables for all tests.

    This fixture runs once per test session and validates that required
    environment variables are set. It sets default values for optional
    variables if they are not already configured.

    Required environment variables:
        - REVENIUM_METERING_API_KEY: Your Revenium API key (REQUIRED)

    Optional environment variables (with defaults):
        - REVENIUM_METERING_BASE_URL: Uses package default (https://api.revenium.ai)
        - REVENIUM_LOG_LEVEL: Defaults to INFO
    """
    # Validate required environment variables
    if not os.environ.get('REVENIUM_METERING_API_KEY'):
        raise ValueError(
            "REVENIUM_METERING_API_KEY environment variable is required for tests. "
            "Please set it in your environment or .env file. "
            "See tests/README.md for setup instructions."
        )

    # Set default log level if not already set
    if not os.environ.get('REVENIUM_LOG_LEVEL'):
        os.environ['REVENIUM_LOG_LEVEL'] = 'INFO'

    # Note: REVENIUM_METERING_BASE_URL will use package default (https://api.revenium.ai) if not set

    yield

    # Cleanup after all tests (optional)
    # Could reset environment variables here if needed


@pytest.fixture(scope="session")
def model_name():
    """
    Return the Ollama model name to use for testing.
    
    Using a small, fast model for testing to minimize resource usage
    and test execution time.
    """
    return 'qwen2.5:0.5b'


@pytest.fixture(scope="session")
def test_metadata():
    """
    Return sample metadata for testing metadata propagation.
    
    This metadata can be used in tests that verify metadata is properly
    passed through to the Revenium metering service.
    """
    return {
        "trace_id": "pytest-trace-001",
        "task_type": "automated-testing",
        "subscriber": {
            "id": "pytest-user-123",
            "email": "pytest@example.com"
        },
        "organization_id": "pytest-test-org",
        "subscription_id": "pytest-subscription",
        "product_id": "ollama-middleware-pytest",
        "agent": "pytest-agent"
    }


def pytest_configure(config):
    """
    Configure pytest with custom markers.
    """
    config.addinivalue_line(
        "markers", "integration: mark test as an integration test"
    )
    config.addinivalue_line(
        "markers", "unit: mark test as a unit test"
    )

