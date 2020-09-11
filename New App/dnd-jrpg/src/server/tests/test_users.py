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
    yield client
 

def test_postuser(client):
    #http://localhost:5000/user
    rv = client.delete('/user', json={"username": "TestUser1", "password": "TestPass"})

    rv = client.post('/user', json={"username": "TestUser1", "password": "TestPass"})
    json = rv.get_json()
    assert("message" in json)
    assert(rv.status_code == 201)

    rv = client.post('/user', json={"username": "TestUser1", "password": "TestPass"})
    json = rv.get_json()
    assert("message" in json)
    assert(rv.status_code == 404)

    rv = client.delete('/user', json={"username": "TestUser1", "password": "TestPass"})
    json = rv.get_json()
    assert("message" in json)
    assert(rv.status_code == 200)
    

def test_auth(client):
    #http://localhost:5000/auth
    rv = client.delete('/user', json={"username": "TestUser1", "password": "TestPass"})
    rv = client.post('/user', json={"username": "TestUser", "password": "TestPass"})

    rv = client.post('/auth', json={"username": "TestUser", "password": "TestPass"})
    json = rv.get_json()
    assert("access_token" in json)
    assert(rv.status_code == 200)

    rv = client.post('/auth', json={"username": "WrongTestUser", "password": "TestPass"})
    json = rv.get_json()
    assert(rv.status_code == 401)

    rv = client.post('/auth', json={"username": "TestUser", "password": "WrongTestPass68JwIotpIXNa"})
    json = rv.get_json()
    assert(rv.status_code == 401)

    rv = client.delete('/user', json={"username": "TestUser1", "password": "TestPass"})
    rv = client.delete('/user', json={"username": "TestUser", "password": "TestPass"})


def test_get(client):
    rv = client.delete('/user', json={"username": "TestUser1", "password": "TestPass"})
    rv = client.post('/user', json={"username": "TestUser1", "password": "TestPass"})
    rv = client.post('/auth', json={"username": "TestUser1", "password": "TestPass"})
    json = rv.get_json()    
    token = json["access_token"]

    rv = client.get('/user', headers={"Authorization" : f"JWT {token}"}, json={"username": "TestUser1", "password": "TestPass"})
    json = rv.get_json()
    assert(json['username'] == 'TestUser1')
    assert(rv.status_code == 200)

    rv = client.delete('/user', json={"username": "TestUser1", "password": "TestPass"})
    
    rv = client.get('/user', headers={"Authorization" : f"JWT {token}"}, json={"username": "TestUser1", "password": "TestPass"})
    assert(rv.status_code == 401)







