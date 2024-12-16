import pytest   
from loan import app # type: ignore


#proxy to live server
@pytest.fixture
def client():
    return app.test_client()


def test_home(client):
    resp = client.get("/")
    assert resp.status_code == 200
