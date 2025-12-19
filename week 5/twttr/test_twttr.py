from twttr import shorten
import pytest

def test_strings():
    assert shorten('twitter') == 'twttr'

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_numbers():
    assert shorten("1234") == "1234"
    assert shorten("123456789") == "123456789"

def test_string_with_space():
    assert shorten("hello twitter") == "hll twttr"

def test_punctuation():
    assert shorten("hello twitter!") == "hll twttr!"

