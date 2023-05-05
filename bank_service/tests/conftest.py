import pytest


IP_ADDRESS = "127.0.0.1"
PORT_ADDRESS = "8000"


@pytest.fixture(scope="session")
def root_url():
    """Return the root url of the server
    """

    return f"http://{IP_ADDRESS}:{PORT_ADDRESS}"
