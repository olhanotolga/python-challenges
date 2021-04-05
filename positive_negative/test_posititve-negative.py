__doc__

from positive_negative import neutralize


def test_answer():
    assert neutralize("+-+", "+--") == "+-0"
    assert neutralize("--++--", "++--++") == "000000"
    assert neutralize("-+-+-+", "-+-+-+") == "-+-+-+"
    assert neutralize("-++-", "-+-+") == "-+00"
    assert neutralize("+0+", "+--") == "Invalid pattern"
    assert neutralize("+-++", "+--") == "Lengths don't match"
    assert neutralize(["+", "-", "+"], ["+", "-", "-"]) == "Must be a string"
