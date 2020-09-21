#!/src/api
import pytest
import api

from db import db
from flask import json

@pytest.fixture
def client():
    client = api.app.test_client()
    api.app.config['TESTING'] = True
    api.app.config['SQALCHEMY_TRACK_MODIFICATIONS'] = False 
    db.init_app(api.app)
    rv = client.post('/register', json={"username": "TestUser", "password": "TestPass"})
    rv = client.post('/login', json={"username": "TestUser", "password": "TestPass"})
    json = rv.get_json()
    setup_token = json["access_token"]
    rv = client.delete('/user', headers={"Authorization" : f"Bearer {setup_token}"}, json={"target": -1})
    rv = client.post('/register', json={"username": "TestUser1", "password": "TestPass"})
    rv = client.post('/login', json={"username": "TestUser1", "password": "TestPass"})
    json = rv.get_json()
    setup_token2 = json["access_token"]
    rv = client.delete('/user', headers={"Authorization" : f"Bearer {setup_token2}"}, json={"target": -1})
    yield client
 

def test_register(client):
    #http://localhost:5000/register
    rv = client.post('/register', json={"username": "TestUser1", "password": "TestPass"})
    json = rv.get_json()
    assert(json["message"] == "User 'TestUser1' created successfully.")
    assert(rv.status_code == 201)

    rv = client.post('/register', json={"username": "TestUser1", "password": "TestPass"})
    json = rv.get_json()
    assert(json["message"] == "A user with that username already exists.")
    assert(rv.status_code == 404)
    

def test_login(client):
    #http://localhost:5000/login
    rv = client.post('/register', json={"username": "TestUser", "password": "TestPass"})

    rv = client.post('/login', json={"username": "TestUser", "password": "TestPass"})
    json = rv.get_json()
    assert("access_token" in json)
    assert("refresh_token" in json)
    assert(rv.status_code == 200)

    setup_token = json["access_token"]

    rv = client.post('/login', json={"username": "WrongTestUser", "password": "TestPass"})
    json = rv.get_json()
    assert(rv.status_code == 401)

    rv = client.post('/login', json={"username": "TestUser", "password": "WrongTestPass68JwIotpIXNa"})
    json = rv.get_json()
    assert(rv.status_code == 401)


def test_delete(client):
    rv = client.post('/register', json={"username": "TestUser", "password": "TestPass"})
    rv = client.post('/login', json={"username": "TestUser", "password": "TestPass"})
    json = rv.get_json()    
    token = json["access_token"]

    rv = client.delete('/user', json={"target": -1})
    assert(rv.status_code == 401)

    rv = client.delete('/user', headers={"Authorization" : f"Bearer {token}"}, json={"target": -2})
    json = rv.get_json()
    assert(json['message'] == "User not found.")
    assert(rv.status_code == 404)

    rv = client.delete('/user', headers={"Authorization" : f"Bearer {token}"}, json={"target": -1})
    json = rv.get_json()
    assert(json["message"] == "User deleted successfully.")
    assert(rv.status_code == 200)

def test_get(client):
    rv = client.post('/register', json={"username": "TestUser1", "password": "TestPass"})
    rv = client.post('/login', json={"username": "TestUser1", "password": "TestPass"})
    json = rv.get_json()    
    token = json["access_token"]

    rv = client.get('/user', json={"username": "TestUser1", "password": "TestPass"})
    assert(rv.status_code == 401)
    
    rv = client.get('/user', headers={"Authorization" : f"Bearer {token}"}, json={"target": -1})
    json = rv.get_json()
    assert(json['username'] == 'TestUser1')
    assert(rv.status_code == 200)

    rv = client.delete('/user', headers={"Authorization" : f"Bearer {token}"}, json={"target": -1})
    
    rv = client.get('/user', headers={"Authorization" : f"Bearer {token}"}, json={"target": -1})
    assert(rv.status_code == 404)







