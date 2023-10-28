from fastapi import FastAPI
from fastapi.testclient import TestClient
from ..src import main
    


client = TestClient(main)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
    
    