
import pytest
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}

def test_chat_non_streaming():
    resp = client.post("/chat", json={"message": "hello", "stream": False})
    assert resp.status_code == 200
    data = resp.json()
    assert "answer" in data or "response" in data

def test_chat_streaming():
    resp = client.post("/chat", json={"message": "hello", "stream": True})
    assert resp.status_code == 200
    # SSE should have event line
    assert resp.headers["content-type"] == "text/event-stream"
