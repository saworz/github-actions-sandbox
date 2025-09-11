from utils import add_numbers


def test_add_numbers_positive():
    assert add_numbers(2, 3) == 5

def test_add_numbers_negative():
    assert add_numbers(-1, -2) == -3

def test_add_numbers_with_zero():
    assert add_numbers(0, 5) == 5

def test_add_numbers_with_string():
    try:
        add_numbers(2, "3")
    except TypeError:
        assert True
    else:
        assert False

def test_add_numbers_floats():
    assert add_numbers(2.5, 3.5) == 6.0