import os
import sys

# Fix import path BEFORE importing app
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.insert(0, PARENT_DIR)

from app import app  # noqa: E402


def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
