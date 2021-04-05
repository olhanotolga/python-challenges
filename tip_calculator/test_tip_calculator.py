__doc__

from tip_calculator import calculate_tip


def test_answer():
    assert (
        calculate_tip(2, 80, 10)
        == "Each guest needs to pay 40.0 EUR + 4.0 EUR tip — a total of 44.0 EUR."
    )
    assert (
        calculate_tip(4, 50, 10)
        == "Each guest needs to pay 12.5 EUR + 1.25 EUR tip — a total of 13.75 EUR (rounded to 14)."
    )
    assert (
        calculate_tip(3, 80, 8)
        == "Each guest needs to pay 26.67 EUR + 2.13 EUR tip — a total of 28.8 EUR (rounded to 29)."
    )
