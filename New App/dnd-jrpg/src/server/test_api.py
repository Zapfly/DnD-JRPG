#!/src/api
import pytest
import api

from flask import json

@pytest.fixture
def client():
    api.app.config['TESTING'] = True
    client = api.app.test_client()

    yield client

# test_func = api.func(4)
# def test_simplefunc():
#     assert api.simple_func() == "this is a function from api.py"


# def test_answer():
#     assert api.func(4) == 5
#--------------------------------------------------
def test_getlevel(client):
    #http://localhost:5000/level<string:name>
    pass

def test_gethero(client):
    #http://localhost:5000/hero/<name>
    pass

def test_puthero(client):
    #http://localhost:5000/update-hero
    pass

def test_postuser(client):
    #http://localhost:5000/new-user
    rv = client.post('/new-user', json={"username": "Bob", "password": "asdf"})
    json = rv.get_json()
    assert("message" in json)
    assert(rv.status_code == 201)

    rv = client.delete('/new-user', json={"username": "Bob", "password": "asdf"})
    assert("message" in json)
    assert(rv.status_code == 202)




    

def test_getuser(client):
    #http://localhost:5000/user/<name>
    pass
