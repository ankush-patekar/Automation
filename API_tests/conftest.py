import pytest
from API_utils.api_client import APIClient


@pytest.fixture(scope="session")
def api_client():
    client = APIClient()
    token = client.get_token()         # Fetch token only once for entire test session
    print(f"Token: {token}")           # For debugging
    return client
