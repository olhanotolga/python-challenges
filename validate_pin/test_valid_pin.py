__doc__

from valid_pin import valid


def test_answer():
    assert valid("1234") == True
    assert valid("45135") == False
    assert valid("89abc1") == False
    assert valid("900876") == True
    assert valid(" 4983") == False
    assert valid("") == False
    assert valid(1234) == "Must be a string"
