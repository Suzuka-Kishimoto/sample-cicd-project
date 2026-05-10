from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    """ルートエンドポイントのテスト"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, CI/CD World!"}

def test_read_item():
    """アイテムエンドポイントのテスト"""
    response = client.get("/items/5")
    assert response.status_code == 200
    assert response.json() == {"item_id": 5, "q": None}

def test_read_item_with_query():
    """クエリパラメータ付きアイテムエンドポイントのテスト"""
    response = client.get("/items/5?q=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 5, "q": "test"}

def test_health_check():
    """ヘルスチェックエンドポイントのテスト"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
