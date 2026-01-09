import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.database import get_db

@pytest.fixture
def client():
    with TestClient(app) as c: 
        yield c
        
        