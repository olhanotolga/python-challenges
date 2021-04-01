import re


def valid(pin):
    if not isinstance(pin, str):
        return "Must be a string"

    pattern = r"^(\d{4})$|^(\d{6})$"
    result = re.match(pattern, pin)

    if result:
        return True
    else:
        return False


def test_answer():
    assert valid("1234") == True
    assert valid("45135") == False
    assert valid("89abc1") == False
    assert valid("900876") == True
    assert valid(" 4983") == False
    assert valid("") == False
    assert valid(1234) == "Must be a string"
