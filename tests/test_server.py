import pytest
from fastapi.testclient import TestClient
from server.main import app
import os

client = TestClient(app)


def test_process_image_success():
    img_path = "tests/res/test.jpg"

    # Send a multipart/form-data request mimicking the client
    with open(img_path, "rb") as f:
        response = client.post(
            "/process",
            files={"file": ("test.jpg", f, "image/jpeg")},
            data={"filter_type": "laplace"}
        )

    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    # Ensure the returned buffer contains data
    assert len(response.content) > 0


def test_process_image_invalid_filter():
    img_path = "tests/res/test.jpg"

    with open(img_path, "rb") as f:
        response = client.post(
            "/process",
            files={"file": ("test.jpg", f, "image/jpeg")},
            data={"filter_type": "invalid_filter"}
        )

    assert response.status_code == 400
    assert response.text == "Invalid filter"