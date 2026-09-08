import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from app import app
from database.db import init_db, get_connection


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        connection = get_connection()

        connection.execute("DELETE FROM users")
        connection.commit()
        connection.close()

        yield client


def test_add_unique_user(client):
    response = client.post(
        "/",
        data={
            "name": "Youssef",
            "email": "youssef@test.com"
        }
    )

    assert b"Unique data added successfully." in response.data


def test_reject_duplicate_email(client):
    client.post(
        "/",
        data={
            "name": "Youssef",
            "email": "youssef@test.com"
        }
    )

    response = client.post(
        "/",
        data={
            "name": "Ahmed",
            "email": "youssef@test.com"
        }
    )

    assert b"Duplicate data! This email already exists." in response.data


def test_reject_invalid_email(client):
    response = client.post(
        "/",
        data={
            "name": "Youssef",
            "email": "invalid-email"
        }
    )

    assert b"Please enter a valid email address." in response.data


def test_reject_empty_fields(client):
    response = client.post(
        "/",
        data={
            "name": "",
            "email": ""
        }
    )

    assert b"Name and email are required." in response.data