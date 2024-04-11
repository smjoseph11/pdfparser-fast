from pathlib import Path
from unittest.mock import MagicMock

import pytest

from pdfparser import config
from pdfparser.flask_app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    with app.test_client() as client:
        yield client


TEST_DATA = Path(__file__).parent.parent / "test_data"


def test_parse_pdf_success(client, session, monkeypatch):
    """Test parsing a PDF successfully."""
    # Create a sample request data
    data = {"file_path": str(TEST_DATA / "Test_PDF_2p.pdf")}
    mock_sessionmaker = MagicMock(return_value=session)
    monkeypatch.setattr("pdfparser.flask_app.sessionmaker", mock_sessionmaker)
    # Send a POST request to the endpoint with sample data
    monkeypatch.setattr(config, "get_postgres_uri", lambda: "sqlite://")
    response = client.post("/parse_pdf", json=data)

    # Check that the response status code is 201 (created)
    assert response.status_code == 201

    # Check the response message
    assert response.json["message"] == "2 pages parsed successfully"  # Assuming 2 pages in the PDF


def test_parse_pdf_missing_file_path(client):
    """Test parsing a PDF with missing file path."""
    # Send a POST request without providing the file_path
    response = client.post("/parse_pdf", json={})

    # Check that the response status code is 400 (bad request)
    assert response.status_code == 400

    # Check the response message
    assert response.json["message"] == "File path and PDF ID are required"


# Add more test cases as needed
