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

    rv = client.post('/user', json={"username": "TestUser", "password": "TestPass"})
    json = rv.get_json()
    test_user = json['user']
    global test_user_id
    test_user_id = test_user['user_id']
    #auth
    rv = client.post('/auth', json={"username": "TestUser", "password": "TestPass"})
    json = rv.get_json()
    global token
    token = json["access_token"]
    rv = client.delete('/hero/Odysseus', headers={"Authorization" : f"JWT {token}"}, json={"user_id": test_user_id})
    rv = client.post('/hero/Hercules', headers={"Authorization" : f"JWT {token}"}, json={
            "heroname": "Hercules",
            "atk": 30,
            "hp": 40,
            "max_hp": 40,
            "sprite": "string",
            "user_id": test_user_id
        }
    )
    #create hero
    yield client
    rv = client.delete('/user', json={"username": "TestUser", "password": "TestPass"})
    #delete level
    #delete hero
    rv = client.delete('/hero/Hercules', headers={"Authorization" : f"JWT {token}"}, json={"user_id": test_user_id})
    rv = client.delete('/hero/Odysseus', headers={"Authorization" : f"JWT {token}"}, json={"user_id": test_user_id})


#http://localhost:5000/hero/<string:heroname>
def test_posthero(client):
    rv = client.post('/hero/Odysseus', json={
            "heroname": "Odysseus",
            "atk": 30,
            "hp": 40,
            "sprite": "string",
            "user_id": test_user_id
        }
    )   
    assert(rv.status_code == 401)

    rv = client.post('/hero/Odysseus', headers={"Authorization" : f"JWT {token}"}, json={
            "heroname": "Odysseus",
            "atk": 30,
            "hp": 40,
            "sprite": "string",
            "user_id": test_user_id
        }
    )

    json = rv.get_json()
    assert(rv.status_code == 200)


def test_gethero(client):
    rv = client.get('/hero/Hercules', json={
        "user_id": test_user_id
    })
    assert(rv.status_code == 401)

    rv = client.get('/hero/Hercules', headers={"Authorization" : f"JWT {token}"}, json={
        "user_id": test_user_id
    })
    assert(rv.status_code == 200)
    json = rv.get_json()
    assert(json['message'] == "Hero Hercules found")
    gotten_hero = json['hero']
    assert(gotten_hero['heroname'] == "Hercules")

    rv = client.get('/hero/Odysseus', headers={"Authorization" : f"JWT {token}"}, json={
        "user_id": test_user_id
    })
    assert(rv.status_code == 404)
    json = rv.get_json()
    assert(json['message'] == "Hero not found")
    

def test_puthero(client):
    rv = client.put('/hero/Hercules', json={
            "heroname": "Odysseus",
            "atk": 30,
            "hp": 40,
            "sprite": "string",
            "user_id": test_user_id
        }
    )
    assert(rv.status_code == 401)

    rv = client.put('/hero/Hercules', headers={"Authorization" : f"JWT {token}"}, json={
            "heroname": "Odysseus",
            "atk": 30,
            "hp": 40,
            "sprite": "string",
            "user_id": test_user_id
        }
    )
    assert(rv.status_code == 200)

    rv = client.get('/hero/Hercules', headers={"Authorization" : f"JWT {token}"}, json={
        "user_id": test_user_id
    })
    assert(rv.status_code == 404)

    rv = client.get('/hero/Odysseus', headers={"Authorization" : f"JWT {token}"}, json={
        "user_id": test_user_id
    })
    assert(rv.status_code == 200)


def test_deletehero(client):
    rv = client.delete('/hero/Hercules', json={
            "heroname": "Hercules",
            "atk": 30,
            "hp": 40,
            "sprite": "string",
            "user_id": test_user_id
    })
    assert(rv.status_code == 401)

    rv = client.delete('/hero/Hercules', headers={"Authorization" : f"JWT {token}"}, json={
            "username": "TestUser",
            "heroname": "Hercules",
            "atk": 30,
            "hp": 40,
            "sprite": "string",
            "user_id": test_user_id
    })
    json = rv.get_json()
    assert("message" in json == {'message': 'Hero deleted'})
    assert(rv.status_code == 200)

    rv = client.delete('/hero/Hercules', headers={"Authorization" : f"JWT {token}"}, json={
            "username": "TestUser",
            "heroname": "Hercules",
            "atk": 30,
            "hp": 40,
            "sprite": "string",
            "user_id": test_user_id
    })
    json = rv.get_json()
    assert("message" in json == {'message': 'That hero does not exist'})
    assert(rv.status_code == 400)
