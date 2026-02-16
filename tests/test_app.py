import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert any("participants" in v for v in data.values())

def test_signup_and_unregister():
    # Use a test activity and email
    activity = next(iter(client.get("/activities").json().keys()))
    email = "testuser@mergington.edu"
    # Sign up
    signup = client.post(f"/activities/{activity}/signup?email={email}")
    assert signup.status_code in (200, 400)  # 400 if already signed up
    # Unregister
    unregister = client.post(f"/activities/{activity}/unregister?email={email}")
    assert unregister.status_code in (200, 400)  # 400 if not signed up
