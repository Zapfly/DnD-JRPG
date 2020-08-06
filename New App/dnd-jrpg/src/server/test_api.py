#!/src/api
import pytest
import api

from flask import json

@pytest.fixture
def client():
    api.app.config['TESTING'] = True
    client = api.app.test_client()
    rv = client.post('/new-user', json={"username": "TestUser", "password": "TestPass"})
    #create level
    #create hero
    yield client
    rv = client.delete('/new-user', json={"username": "TestUser", "password": "TestPass"})
    #delete level
    #delete hero


def test_getlevel(client):
    #http://localhost:5000/level<string:name>
    pass

def test_gethero(client):
    #http://localhost:5000/hero/<name>
    pass

def test_puthero(client):
    #http://localhost:5000/update-hero
    pass

# def test_posthero(client):
#     rv = client.post('/auth', json={"username": "TestUser", "password": "TestPass"})
#     json = rv.get_json()
#     token = json["access_token"]
#     assert(rv.status_code == 200)

#     rv = client.post('/hero', json={
#             "hero_id": 2,
#             "hero_info": {
#                 "name": "Hercules",
#                 "atk": 30,
#                 "hp": 40,
#                 "sprite": "string"
#             }     
#         }
#     )   
#     assert(rv.status_code == 401)

#     rv = client.post('/hero', headers={"Authorization" : f"JWT {token}"}, json={
#             "hero_id": 2,
#             "hero_info": {
#                 "name": "Hercules",
#                 "atk": 30,
#                 "hp": 40,
#                 "sprite": "string"
#             }     
#         }
#     )
#     assert(token)
#     assert(rv.status_code == 200)

#     rv = client.delete('/hero', headers={"Authorization" : f"JWT {token}"}, json={"hero_id": 2, "hero_info": {"name": "Hercules","atk": 30,"hp": 40,"sprite": "string"}})
#     json = rv.get_json()
#     assert(rv.status_code == 202)

# def test_deletehero(client):
#     rv = client.post('/auth', json={"username": "TestUser", "password": "TestPass"})
#     json = rv.get_json()
#     token = json["access_token"]
#     assert(rv.status_code == 200)

#     rv = client.delete('/hero', json={
#             "hero_id": 2,
#             "hero_info": {
#                 "name": "Hercules",
#                 "atk": 30,
#                 "hp": 40,
#                 "sprite": "string"
#             }
#     })
#     assert(rv.status_code == 401)

#     rv = client.post('/hero', headers={"Authorization" : f"JWT {token}"}, json={
#             "hero_id": 2,
#             "hero_info": {
#                 "name": "Hercules",
#                 "atk": 30,
#                 "hp": 40,
#                 "sprite": "string"
#             }       
#         }
#     )
#     assert(rv.status_code == 200)

#     rv = client.delete('/hero', headers={"Authorization" : f"JWT {token}"}, json={
#             "hero_id": 2,
#             "hero_info": {
#                 "name": "Hercules",
#                 "atk": 30,
#                 "hp": 40,
#                 "sprite": "string"
#             }
#     })

#     json = rv.get_json()
#     assert("message" in json == {'message': 'Hero deleted'})
#     assert(rv.status_code == 202)

#     rv = client.delete('/hero', headers={"Authorization" : f"JWT {token}"}, json={
#             "hero_id": 2,
#             "hero_info": {
#                 "name": "Hercules",
#                 "atk": 30,
#                 "hp": 40,
#                 "sprite": "string"
#             }
#     })

#     json = rv.get_json()
#     assert("message" in json == {'message': 'That hero does not exist'})
#     assert(rv.status_code == 400)

def test_postuser(client):
    #http://localhost:5000/new-user
    rv = client.delete('/new-user', json={"username": "TestUser1", "password": "TestPass"})
    json = rv.get_json()

    rv = client.post('/new-user', json={"username": "TestUser1", "password": "TestPass"})
    json = rv.get_json()
    assert("message" in json)
    assert(rv.status_code == 201)

    rv = client.post('/new-user', json={"username": "TestUser1", "password": "TestPass"})
    json = rv.get_json()
    assert("message" in json)
    assert(rv.status_code == 400)

    rv = client.delete('/new-user', json={"username": "TestUser1", "password": "TestPass"})
    json = rv.get_json()
    assert("message" in json)
    assert(rv.status_code == 202)
    

def test_auth(client):
    #http://localhost:5000/auth
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



