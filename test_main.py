from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestRootRoute:
    def test_root_route(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello FastAPI"}
