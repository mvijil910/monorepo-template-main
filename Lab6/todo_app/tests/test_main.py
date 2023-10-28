from fastapi import FastAPI
from fastapi.testclient import TestClient
from src.main import app
    



client = TestClient(app)


def test_read_main():
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == {"msg": "hello_world"}
    

def test_first_apiV2(): 
    response = client.get("/books/helloWorld")
    assert response.status_code == 200
    assert response.json() == {"msg": "helloWorld"}


def test_first_apiV3(): 
    response = client.get("/books/?title=Mockingjay%20part2")
    assert response.status_code == 200
    assert response.json() == {"msg": "Mockingjay part2"}

def test_first_apiV5(): 
    response = client.get("/books/helloWorld/?book_id=1234")
    assert response.status_code == 200
    assert response.json() == {"msg": "helloWorld", "msg2": "1234"}
    

    
def test_first_apiV4(): 
    response = client.post("/books/create_book", json={'author': 'Sam Sammer', 'title': 'A bad day for Sam'})
    assert response.status_code == 200
    assert response.json() == {'msg': {'author': 'Sam Sammer', 'title': 'A bad day for Sam'}}

def test_first_apiV6(): 
    response = client.put("/books/add_book", json={'author': 'Sam Sammer', 'title': 'A bad day for Sam'})
    assert response.status_code == 200
    assert response.json() == {'msg': {'author': 'Sam Sammer', 'title': 'A bad day for Sam'}}

def test_first_apiV7(): 
    response = client.delete("/books/12345")
    assert response.status_code == 200
    assert response.json() == {'msg': 'successfully deleted ', 'book_id': '12345'}