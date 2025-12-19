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