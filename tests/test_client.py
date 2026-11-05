import os
import pytest
from unittest.mock import patch, Mock
from client.client import send_image


@patch("client.client.requests.post")
def test_send_image_success(mock_post, tmp_path):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = b"fake_image_bytes"
    mock_response.raise_for_status = Mock()
    mock_post.return_value = mock_response

    input_path = "tests/res/test.jpg"
    output_path = tmp_path / "mock_out.jpg"

    send_image(input_path, "gaussian", str(output_path))

    mock_post.assert_called_once()

    assert os.path.exists(output_path)
    with open(output_path, "rb") as f:
        assert f.read() == b"fake_image_bytes"


def test_send_image_file_not_found(capsys):
    send_image("nonexistent_image.jpg", "sobel", "out.jpg")

    captured = capsys.readouterr()
    assert "Error: Input file 'nonexistent_image.jpg' not found." in captured.out