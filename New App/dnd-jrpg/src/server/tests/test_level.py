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
    token = json["access_token"]
    rv = client.delete('/hero/Hercules', headers={"Authorization" : f"JWT {token}"}, json={"user_id": test_user_id})
    rv = client.delete('/hero/Odysseus', headers={"Authorization" : f"JWT {token}"}, json={"user_id": test_user_id})


    #create level
    #create hero
    yield client
    rv = client.delete('/user', json={"username": "TestUser", "password": "TestPass"})
    #delete level
    #delete hero
    rv = client.delete('/hero/Hercules', headers={"Authorization" : f"JWT {token}"}, json={"user_id": test_user_id})
    rv = client.delete('/hero/Odysseus', headers={"Authorization" : f"JWT {token}"}, json={"user_id": test_user_id})



def test_getlevel(client):
    #http://localhost:5000/level<string:name>
    pass
