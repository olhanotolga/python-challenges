import re


def neutralize(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        return "Must be a string"

    if not len(str1) == len(str2):
        return "Lengths don't match"

    pattern = "^[+-]+$"
    if not re.match(pattern, str1) or not re.match(pattern, str2):
        return "Invalid pattern"

    output = ""

    rules = {"++": "+", "--": "-", "+-": "0", "-+": "0"}

    for i in range(len(str1)):
        output += rules[str1[i] + str2[i]]

    return output


def test_answer():
    assert neutralize("+-+", "+--") == "+-0"
    assert neutralize("--++--", "++--++") == "000000"
    assert neutralize("-+-+-+", "-+-+-+") == "-+-+-+"
    assert neutralize("-++-", "-+-+") == "-+00"
    assert neutralize("+0+", "+--") == "Invalid pattern"
    assert neutralize("+-++", "+--") == "Lengths don't match"
    assert neutralize(["+", "-", "+"], ["+", "-", "-"]) == "Must be a string"
