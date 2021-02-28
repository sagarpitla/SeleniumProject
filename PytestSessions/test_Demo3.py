import  pytest

def test_m1():
    a=3
    b=4
    assert a+1==b, "Test failed"
    assert a==b, "test failed as a is not eq to b"

def test_m2():
    name= "selenium"
    assert name.upper() == "SELENIUM"


def test_login():
    assert "Admin" == "Admin1"