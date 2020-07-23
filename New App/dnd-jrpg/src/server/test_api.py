#!/src/api
import pytest
import api

test_func = api.func(4)
def test_simplefunc():
    assert api.simple_func() == "this is a function from api.py"


def test_answer():
    assert api.func(4) == 5
#--------------------------------------------------
def test_getlevel():
    #http://localhost:5000/level<string:name>
    pass

def test_gethero():
    #http://localhost:5000/hero/<name>
    pass

def test_puthero():
    #http://localhost:5000/update-hero
    pass

def test_postuser():
    #http://localhost:5000/new-user
    pass

def test_getuser():
    #http://localhost:5000/user/<name>
    pass
