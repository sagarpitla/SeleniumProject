import  pytest
@pytest.mark.login
def test_m1():
    a=3
    b=4
    assert a+1==b, "Test failed"
    assert a==b, "test failed as a is not eq to b"

def test_m2():
    name= "selenium"
    assert name.upper() == "SELENIUM"
@pytest.mark.login
def test_m3():
    assert True

def test_m4():
    assert  False

@pytest.mark.login
def test_login():
    assert "Admin"=="Admin"