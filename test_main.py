from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestRootRoute:
    def test_root_route(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello FastAPI"}


class TestHiRoute:

    def test_string(self):
        name = "Jane"
        response = client.get("/hi/%s" % name)
        assert response.status_code == 200
        assert response.json() == {"message": ("Hi %s" % name)}

    def test_empty(self):
        name = ""
        response = client.get("/hi/%s" % name)
        assert response.status_code == 404

    def test_non_alpha(self):
        name = "123"
        response = client.get("/hi/%s" % name)
        assert response.status_code == 200
        assert response.json() == {"message": ("Hi %s" % name)}
