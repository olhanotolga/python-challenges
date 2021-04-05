__doc__

from wash_your_hands import wash_hands


def test_answer():
    assert wash_hands(8, 7) == "You spent 588 min 0 sec washing your hands!"
    assert wash_hands(0, 0) == "You spent 0 min 0 sec washing your hands!"
    assert wash_hands(7, 9) == "You spent 661 min 30 sec washing your hands!"
