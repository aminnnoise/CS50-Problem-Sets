from fuel import convert , gauge
import pytest

def test_one():
    assert gauge(convert('100/1000')) == '10%'
    assert gauge(convert('5/10')) == '50%'

def test_two():
    assert gauge(convert('1/1000')) == 'E'
    assert gauge(convert('5000/5000')) == 'F'
    assert gauge(convert('9999/10000')) == 'F'

def test_excepts():
    with pytest.raises(ZeroDivisionError):
        convert('10/0')

    with pytest.raises(ValueError):
        convert('moao/as')

    with pytest.raises(ValueError):
        convert('-1/2')


def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    assert convert("0/100") == 0

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"