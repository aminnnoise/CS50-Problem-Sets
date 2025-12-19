import pytest
from working import convert

def test_valid_formats():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"
    assert convert("8:00 AM to 5:30 PM") == "08:00 to 17:30"


def test_no_minutes():
    assert convert("12 AM to 1 PM") == "00:00 to 13:00"
    assert convert("1 PM to 12 AM") == "13:00 to 00:00"

def test_case_insensitive():
    assert convert("9 am to 5 pm") == "09:00 to 17:00"
    assert convert("10:30 Pm To 8:50 aM") == "22:30 to 08:50"


def test_invalid_time_range():
    with pytest.raises(ValueError):
        convert("13:00 PM to 1:00 AM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")  
    with pytest.raises(ValueError):
        convert("9 AM to 25 PM")       
    with pytest.raises(ValueError):
        convert("8:70 AM to 5 PM")     

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")         
    with pytest.raises(ValueError):
        convert("9:00 to 5:00 PM")      
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")           
    with pytest.raises(ValueError):
        convert("cat to dog")          
    with pytest.raises(ValueError):
        convert("9:00 AM to 5 PM to 6 PM")  
    with pytest.raises(ValueError):
        convert("9 AM to 5")           