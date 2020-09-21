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
    rv = client.delete('/monster', headers={"Authorization" : f"Bearer {token}"}, json={"levelname": "Mount Olympus", "monstername": "TestBoblin"})
    rv = client.delete('/monster', headers={"Authorization" : f"Bearer {token}"}, json={"levelname": "Mount Olympus", "monstername": "TestBoblin2"})
    rv = client.delete('/level', headers={"Authorization" : f"Bearer {token}"}, json={"levelname": "Mount Olympus"})
    rv = client.post('/level', headers={"Authorization" : f"Bearer {token}"}, json={"levelname": "Mount Olympus"})
    rv = client.post('/monster', headers={"Authorization" : f"Bearer {token}"}, json={
            "monstername": "TestBoblin",
            "atk": 10,
            "hp": 15,
            "max_hp": 15,
            "sprite": "string",
            "levelname": "Mount Olympus"
        }
    )
    yield client
    rv = client.delete('/monster', headers={"Authorization" : f"Bearer {token}"}, json={"levelname": "Mount Olympus", "monstername": "TestBoblin"})
    rv = client.delete('/monster', headers={"Authorization" : f"Bearer {token}"}, json={"levelname": "Mount Olympus", "monstername": "TestBoblin2"})
    rv = client.delete('/level', headers={"Authorization" : f"Bearer {token}"}, json={"levelname": "Mount Olympus"})
    rv = client.delete('/user', headers={"Authorization" : f"Bearer {setup_token}"}, json={"target": -1})


#http://localhost:5000/monster
def test_postmonster(client):
    rv = client.post('/monster', json={
            "monstername": "TestBoblin2",
            "atk": 11,
            "hp": 16,
            "max_hp": 16,
            "sprite": "string",
            "levelname": "Mount Olympus"
        }
    )   
    assert(rv.status_code == 401)

    rv = client.post('/monster', headers={"Authorization" : f"Bearer {token}"}, json={
            "monstername": "TestBoblin2",
            "atk": 11,
            "hp": 16,
            "max_hp": 16,
            "sprite": "string",
            "levelname": "Mount Olympus"
        }
    )

    json = rv.get_json()
    assert(rv.status_code == 201)
    assert(json['monstername'] == 'TestBoblin2')

    rv = client.post('/monster', headers={"Authorization" : f"Bearer {token}"}, json={
            "monstername": "TestBoblin2",
            "atk": 11,
            "hp": 16,
            "max_hp": 16,
            "sprite": "string",
            "levelname": "Mount Olympus"
        }
    )

    json = rv.get_json()
    assert(rv.status_code == 404)
    assert(json['message'] == "A monster with name 'TestBoblin2' already exists in level 'Mount Olympus'.")


def test_getmonster(client):
    rv = client.get('/monster', json={
        "levelname": "Mount Olympus",
        "monstername": "TestBoblin"
    })
    assert(rv.status_code == 401)

    rv = client.get('/monster', headers={"Authorization" : f"Bearer {token}"}, json={
        "levelname": "Mount Olympus",
        "monstername": "TestBoblin"
    })
    assert(rv.status_code == 200)
    json = rv.get_json()
    assert(json['monstername'] == "TestBoblin")

    rv = client.get('/monster', headers={"Authorization" : f"Bearer {token}"}, json={
        "levelname": "TestArena",
        "monstername": "TestBoblin"
    })
    assert(rv.status_code == 404)
    json = rv.get_json()
    assert(json['message'] == "Monster not found.")
    
    rv = client.get('/monster', headers={"Authorization" : f"Bearer {token}"}, json={
        "levelname": "Mount Olympus",
        "monstername": "TestBoblinOfDoom"
    })
    assert(rv.status_code == 404)
    json = rv.get_json()
    assert(json['message'] == "Monster not found.")

def test_putmonster(client):
    rv = client.put('/monster', json={
            "monstername": "TestBoblin2",
            "atk": 10,
            "hp": 15,
            "max_hp": 15,
            "sprite": "string",
            "old_monstername": "TestBoblin",
            "levelname": "Mount Olympus"
        }
    )
    #test required authorization
    assert(rv.status_code == 401)

    rv = client.put('/monster', headers={"Authorization" : f"Bearer {token}"}, json={
            "monstername": "TestBoblin2",
            "atk": 10,
            "hp": 15,
            "max_hp": 15,
            "sprite": "string",
            "old_monstername": "TestBoblin",
            "levelname": "Mount Olympus"
        }
    )
    #updating when data['old_monstername'] exists but data['monstername'] does not
    json = rv.get_json()
    assert(json['message'] == "Monster updated.")
    assert(rv.status_code == 200)

    rv = client.get('/monster', headers={"Authorization" : f"Bearer {token}"}, json={
        "levelname": "Mount Olympus",
        "monstername": "TestBoblin"
    })
    #previous test continued
    json = rv.get_json()
    assert(json['message'] == "Monster not found.")
    assert(rv.status_code == 404)

    rv = client.get('/monster', headers={"Authorization" : f"Bearer {token}"}, json={
        "levelname": "Mount Olympus",
        "monstername": "TestBoblin2"
    })
    #previous test continued
    assert(rv.status_code == 200)
    
    rv = client.put('/monster', headers={"Authorization" : f"Bearer {token}"}, json={
        "monstername": "TestBoblin2",
        "atk": 30,
        "hp": 40,
        "sprite": "string",
        "levelname": "Mount Olympus",
        "old_monstername": "UnknownBoblin"
        }
    )
    #testing when data['old_monstername'] doesn't exist but data["monstername"] does
    json = rv.get_json()
    assert(json['message'] == "A monster with name 'TestBoblin2' already exists in level 'Mount Olympus'.")
    assert(rv.status_code == 404)

    rv = client.put('/monster', headers={"Authorization" : f"Bearer {token}"}, json={
        "monstername": "TestBoblin",
        "atk": 30,
        "hp": 40,
        "sprite": "string",
        "levelname": "Mount Olympus",
        "old_monstername": "TestBoblin"
        }
    )
    json = rv.get_json()
    #test when neither monstername exists
    assert(json['message'] == "Monster 'TestBoblin' created successfully.")
    assert(rv.status_code == 201)

    rv = client.put('/monster', headers={"Authorization" : f"Bearer {token}"}, json={
        "monstername": "TestBoblin2",
        "atk": 30,
        "hp": 40,
        "sprite": "string",
        "levelname": "Mount Olympus",
        "old_monstername": "TestBoblin"
        }
    )
    json = rv.get_json()
    #test when both exist
    assert(json['message'] == "A monster with name 'TestBoblin2' already exists in level 'Mount Olympus'.")
    assert(rv.status_code == 404)


def test_deletemonster(client):
    rv = client.delete('/monster', json={
        "monstername": "TestBoblin",
        "levelname": "Mount Olympus"
        }
    )
    assert(rv.status_code == 401)

    rv = client.delete('/monster', headers={"Authorization" : f"Bearer {token}"}, json={
        "monstername": "TestBoblin",
        "levelname": "Mount Olympus"
        }
    )
    json = rv.get_json()
    assert("message" in json == {'message': 'Monster deleted.'})
    assert(rv.status_code == 200)

    rv = client.delete('/monster', headers={"Authorization" : f"Bearer {token}"}, json={
        "monstername": "TestBoblin",
        "levelname": "Mount Olympus"
        }
    )
    json = rv.get_json()
    assert("message" in json == {'message': 'That monster does not exist.'})
    assert(rv.status_code == 404)