from coello.app.app import app

def test_index():
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert "coello" in r.get_data(as_text=True)

def test_ai_empty():
    client = app.test_client()
    r = client.post("/api/ai", json={})
    assert r.status_code == 200
    data = r.get_json()
    assert "reply" in data
    assert isinstance(data["reply"], str)

def test_ai_prompt():
    client = app.test_client()
    r = client.post("/api/ai", json={"prompt": "Hola"})
    data = r.get_json()
    assert "hola" in data["reply"].lower()
