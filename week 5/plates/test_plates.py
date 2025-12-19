from plates import is_valid

def test_dot():
    assert is_valid("PI3.14") == False
    assert is_valid("cs50") == True

def test_start_with_zero():
    assert is_valid("cs05") == False

def test_end_with_string():
    assert is_valid("cs50p") == False

def test_len():
    assert is_valid("O") == False
    assert is_valid("OOOOOOOOOOOOOOOOOOOO") == False

def test_four():
    assert is_valid('1505') == False