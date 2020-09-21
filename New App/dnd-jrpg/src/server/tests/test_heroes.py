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
    rv = client.delete('/hero/Odysseus', headers={"Authorization" : f"Bearer {token}"})
    rv = client.post('/hero/Hercules', headers={"Authorization" : f"Bearer {token}"}, json={
            "heroname": "Hercules",
            "atk": 30,
            "hp": 40,
            "max_hp": 40,
            "sprite": "string"
        }
    )
    #create hero
    yield client
    rv = client.delete('/hero/Hercules', headers={"Authorization" : f"Bearer {token}"})
    rv = client.delete('/hero/Odysseus', headers={"Authorization" : f"Bearer {token}"})
    rv = client.delete('/user', headers={"Authorization" : f"Bearer {token}"}, json={"target": -1})
    #delete level
    #delete hero


#http://localhost:5000/hero/<string:heroname>
def test_posthero(client):
    rv = client.post('/hero/Odysseus', json={
            "heroname": "Odysseus",
            "atk": 30,
            "hp": 40,
            "sprite": "string"
        }
    )   
    assert(rv.status_code == 401)

    rv = client.post('/hero/Odysseus', headers={"Authorization" : f"Bearer {token}"}, json={
            "heroname": "Odysseus",
            "atk": 30,
            "hp": 40,
            "sprite": "string"
        }
    )

    json = rv.get_json()
    hero = json['hero']
    assert(rv.status_code == 200)
    assert(hero['heroname'] == 'Odysseus')

    rv = client.post('/hero/Odysseus', headers={"Authorization" : f"Bearer {token}"}, json={
            "heroname": "Odysseus",
            "atk": 30,
            "hp": 40,
            "sprite": "string"
        }
    )

    json = rv.get_json()
    assert(rv.status_code == 404)
    assert(json['message'] == "A hero with name 'Odysseus' already exists.")


def test_gethero(client):
    rv = client.get('/hero/Hercules')
    assert(rv.status_code == 401)

    rv = client.get('/hero/Hercules', headers={"Authorization" : f"Bearer {token}"})
    assert(rv.status_code == 200)
    json = rv.get_json()
    assert(json['heroname'] == "Hercules")

    rv = client.get('/hero/Odysseus', headers={"Authorization" : f"Bearer {token}"})
    assert(rv.status_code == 404)
    json = rv.get_json()
    assert(json['message'] == "Hero not found")
    

def test_puthero(client):
    rv = client.put('/hero/Hercules', json={
            "heroname": "Odysseus",
            "atk": 30,
            "hp": 40,
            "sprite": "string"
        }
    )
    #test required authorization
    assert(rv.status_code == 401)

    rv = client.put('/hero/Hercules', headers={"Authorization" : f"Bearer {token}"}, json={
            "heroname": "Odysseus",
            "atk": 30,
            "hp": 40,
            "sprite": "string"
        }
    )
    #updating when heroname exists but data["heroname"] does not
    json = rv.get_json()
    assert(json['message'] == "Hero updated")
    assert(rv.status_code == 200)

    rv = client.get('/hero/Hercules', headers={"Authorization" : f"Bearer {token}"})
    #previous test continued
    assert(rv.status_code == 404)

    rv = client.get('/hero/Odysseus', headers={"Authorization" : f"Bearer {token}"})
    #previous test continued
    assert(rv.status_code == 200)
    
    rv = client.put('/hero/Hercules', headers={"Authorization" : f"Bearer {token}"}, json={
            "heroname": "Odysseus",
            "atk": 30,
            "hp": 40,
            "sprite": "string"
        }
    )
    #testing when heroname doesn't exist but data["heroname"] does
    json = rv.get_json()
    assert(json['message'] == "A hero with name 'Odysseus' already exists.")
    assert(rv.status_code == 404)

    rv = client.put('/hero/Hercules', headers={"Authorization" : f"Bearer {token}"}, json={
            "heroname": "Hercules",
            "atk": 30,
            "hp": 40,
            "sprite": "string"
        }
    )
    json = rv.get_json()
    #test when neither heroname exists
    assert(json['message'] == "Hero created successfully")
    assert(rv.status_code == 201)

    rv = client.put('/hero/Hercules', headers={"Authorization" : f"Bearer {token}"}, json={
            "heroname": "Odysseus",
            "atk": 30,
            "hp": 40,
            "sprite": "string"
        }
    )
    json = rv.get_json()
    #test when both exist
    assert(json['message'] == "A hero with name 'Odysseus' already exists.")
    assert(rv.status_code == 404)


def test_deletehero(client):
    rv = client.delete('/hero/Hercules')
    assert(rv.status_code == 401)

    rv = client.delete('/hero/Hercules', headers={"Authorization" : f"Bearer {token}"})
    json = rv.get_json()
    assert("message" in json == {'message': 'Hero deleted'})
    assert(rv.status_code == 200)

    rv = client.delete('/hero/Hercules', headers={"Authorization" : f"Bearer {token}"})
    json = rv.get_json()
    assert("message" in json == {'message': 'That hero does not exist'})
    assert(rv.status_code == 404)

#http://localhost:5000/heroes
def test_get_allheroes(client):
    rv = client.post('/hero/Odysseus', headers={"Authorization" : f"Bearer {token}"}, json={
            "heroname": "Odysseus",
            "atk": 30,
            "hp": 40,
            "sprite": "string"
        }
    )

    rv = client.get('/heroes', headers={"Authorization" : f"Bearer {token}"})
    json = rv.get_json()
    assert(rv.status_code == 200)
    heroes = json["heroes"]
    hero1 = heroes[0]
    assert(hero1["heroname"] == 'Hercules')
    hero2 = heroes[1]
    assert(hero2["heroname"] == 'Odysseus')

    rv = client.get('/heroes')
    json = rv.get_json()
    assert(rv.status_code == 401)

    rv = client.delete('/hero/Hercules', headers={"Authorization" : f"Bearer {token}"})
    rv = client.delete('/hero/Odysseus', headers={"Authorization" : f"Bearer {token}"})

    rv = client.get('/heroes', headers={"Authorization" : f"Bearer {token}"})
    json = rv.get_json()
    assert(rv.status_code == 404)