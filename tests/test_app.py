
from fastapi.testclient import TestClient
from app import app, deployments

client = TestClient(app)


def setup_function():
    deployments.clear()


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "DevOps Platform is running"
    }


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "unhealthy"
    }


def test_info():
    response = client.get("/info")

    assert response.status_code == 200
    assert response.json()["project"] == "DevOps Platform"


def test_create_deployment():
    payload = {
        "application": "payment-api",
        "environment": "production",
        "version": "1.0.0"
    }

    response = client.post("/deploy", json=payload)

    assert response.status_code == 200
    assert response.json()["application"] == "payment-api"
    assert response.json()["status"] == "RUNNING"
    assert "deployment_id" in response.json()


def test_deployment_not_found():
    response = client.get("/deploy/invalid-id")

    assert response.status_code == 404

