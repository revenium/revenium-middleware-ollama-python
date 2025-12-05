"""
Pytest configuration and shared fixtures for Revenium Ollama middleware tests.
"""

import os
import pytest


@pytest.fixture(scope="function")
def setup_integration_test():
    """
    Configure environment variables for integration tests.

    This fixture validates that required environment variables are set
    for integration tests that need to connect to real services.

    Required environment variables:
        - REVENIUM_METERING_API_KEY: Your Revenium API key (REQUIRED)

    Optional environment variables (with defaults):
        - REVENIUM_METERING_BASE_URL: Uses package default
        - REVENIUM_LOG_LEVEL: Defaults to INFO
    """
    # Validate required environment variables for integration tests
    if not os.environ.get('REVENIUM_METERING_API_KEY'):
        pytest.skip(
            "REVENIUM_METERING_API_KEY environment variable is required "
            "for integration tests. Please set it in your environment "
            "or .env file. See tests/README.md for setup instructions."
        )

    # Set default log level if not already set
    if not os.environ.get('REVENIUM_LOG_LEVEL'):
        os.environ['REVENIUM_LOG_LEVEL'] = 'INFO'

    yield


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

