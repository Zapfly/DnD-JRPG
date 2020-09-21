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
    rv = client.post('/register', json={"username": "TestUser", "password": "TestPass"})
    rv = client.post('/login', json={"username": "TestUser", "password": "TestPass"})
    json = rv.get_json()
    global token
    token = json["access_token"]
    rv = client.delete('/level', headers={"Authorization" : f"Bearer {token}"}, json={"levelname": "Hades"})
    rv = client.delete('/level', headers={"Authorization" : f"Bearer {token}"}, json={"levelname": "Mount Olympus"})
    rv = client.post('/level', headers={"Authorization" : f"Bearer {token}"}, json={"levelname": "Mount Olympus"})
    #create level
    #create hero
    yield client
    rv = client.delete('/level', headers={"Authorization" : f"Bearer {token}"}, json={"levelname": "Mount Olympus"})
    rv = client.delete('/level', headers={"Authorization" : f"Bearer {token}"}, json={"levelname": "Hades"})
    rv = client.delete('/user', headers={"Authorization" : f"Bearer {token}"}, json={"target": -1})
    #delete level
    #delete hero


def test_postlevel(client):
    rv = client.post('/level', json={
        "levelname": "Hades",
        }
    )        
    assert(rv.status_code == 401)

    rv = client.post('/level', headers={"Authorization" : f"Bearer {token}"}, json={
        "levelname": "Hades",
        }
    )
    json = rv.get_json()        
    assert(rv.status_code == 201)
    assert(json['levelname'] == 'Hades')

    rv = client.post('/level', headers={"Authorization" : f"Bearer {token}"}, json={
        "levelname": "Hades",
        }
    )
    json = rv.get_json()        
    assert(rv.status_code == 404)
    assert(json['message'] == "A level with name 'Hades' already exists.")


def test_getlevel(client):

    rv = client.get('/level', json={
        "levelname": "Random Level Name"
        }
    )
    assert(rv.status_code == 401)

    rv = client.get('/level', headers={"Authorization" : f"Bearer {token}"}, json={
        "levelname": "Random Level Name"
        }
    )
    json = rv.get_json()
    assert(rv.status_code == 404)
    assert(json['message'] == "Level not found")

    rv = client.get('/level', headers={"Authorization" : f"Bearer {token}"}, json={
        "levelname": "Mount Olympus"
        }
    )
    json = rv.get_json()
    assert(rv.status_code == 200)
    assert(json['levelname'] == 'Mount Olympus')


def test_putlevel(client):
    rv = client.put('/level', json={
        "levelname": "Hades"})
    assert(rv.status_code == 401)
    
    rv = client.put('/level', headers={"Authorization" : f"Bearer {token}"}, json={
        "levelname": "Hades"})
    json = rv.get_json()
    assert(rv.status_code == 201)
    assert(json['message'] == "Level 'Hades' created successfully.")

    rv = client.put('/level', headers={"Authorization" : f"Bearer {token}"}, json={
        "levelname": "Hades",
        "old_levelname": "Random Test Level"
        }
    )
    json = rv.get_json()
    assert(rv.status_code == 404)
    assert(json['message'] == "A level with name 'Hades' already exists.")

    rv = client.put('/level', headers={"Authorization" : f"Bearer {token}"}, json={
        "levelname": "New Mount Olympus",
        "old_levelname": "Hades"
        }
    )
    json = rv.get_json()
    assert(rv.status_code == 200)
    assert(json['message'] == "Level updated successfully.")

    rv = client.put('/level', headers={"Authorization" : f"Bearer {token}"}, json={
        "levelname": "Hades"})
    json = rv.get_json()
    assert(rv.status_code == 201)
    assert(json['message'] == "Level 'Hades' created successfully.")

    rv = client.put('/level', headers={"Authorization" : f"Bearer {token}"}, json={
        "levelname": "New Mount Olympus",
        "old_levelname": "Hades"
        }
    )
    json = rv.get_json()
    assert(rv.status_code == 404)
    assert(json['message'] == "A level with name 'New Mount Olympus' already exists.")

    rv = client.delete('/level', headers={"Authorization" : f"Bearer {token}"}, json={"levelname": "New Mount Olympus"})


def test_deletelevel(client):  
    rv = client.delete('/level', json={
        "levelname": "New Mount Olympus"
        }
    )
    assert(rv.status_code == 401)

    rv = client.delete('/level', headers={"Authorization" : f"Bearer {token}"}, json={
        "levelname": "New Mount Olympus"
        }
    )
    json = rv.get_json()
    assert(rv.status_code == 404)
    assert(json['message'] == 'That level does not exist.')

    rv = client.delete('/level', headers={"Authorization" : f"Bearer {token}"}, json={
        "levelname": "Mount Olympus"
        }
    )
    json = rv.get_json()
    assert(rv.status_code == 200)
    assert(json['message'] == "Level 'Mount Olympus' deleted.")


def test_getalllevels(client):
    rv = client.post('/level', headers={"Authorization" : f"Bearer {token}"}, json={"levelname": "Mount Olympus"})
    
    rv = client.get('/levels')
    assert(rv.status_code == 401)

    rv = client.get('/levels', headers={"Authorization" : f"Bearer {token}"})
    json = rv.get_json()
    assert(len(json["levels"]) > 0)