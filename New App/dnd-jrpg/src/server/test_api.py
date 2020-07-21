#!/src/api
import pytest
import api

test_func = api.func(4)
def test_simplefunc():
    assert api.simple_func() == "this is a function from api.py"


def test_answer():
    assert api.func(4) == 5

