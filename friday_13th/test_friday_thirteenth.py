__doc__

from friday_thirteenth import has_friday_13


def test_answer():
    assert has_friday_13(3, 2020) == True
    assert has_friday_13(10, 2017) == True
    assert has_friday_13(1, 1985) == False
    assert has_friday_13(11, 2020) == True
    assert has_friday_13(8, 2021) == True
    assert has_friday_13(7, 2021) == False
    assert has_friday_13(30, 1985) == "Enter valid month and year!"
