from bank import value

def test_20():
    assert value("Hy Mark") == 20
    assert value("How?") == 20

def test_100():
    assert value("very nice") == 100
    assert value("wow") == 100

def test_0():
    assert value("Hello Mark") == 0
    assert value("Hello mark") == 0
    assert value("HELLO Mark") == 0