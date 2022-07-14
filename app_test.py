import pytest
from app import app


def test_home():
    tester = app.test_client()
    response = tester.get("/", content_type="text/html; charset=utf-8")
    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"


def test_topwords():
    tester = app.test_client()
    response = tester.get("/topwords", content_type="application/json")
    assert response.status_code == 200
    assert response.content_type == "application/json"


def test_popular_users():
    tester = app.test_client()
    response = tester.get("/popular/users", content_type="application/json")
    assert response.status_code == 200
    assert response.content_type == "application/json"


def test_popular_mentions():
    tester = app.test_client()
    response = tester.get("/popular/mentions", content_type="application/json")
    assert response.status_code == 200
    assert response.content_type == "application/json"


def test_hourly():
    tester = app.test_client()
    response = tester.get("/hourly", content_type="application/json")
    assert response.status_code == 200
    assert response.content_type == "application/json"
