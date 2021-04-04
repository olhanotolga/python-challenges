__doc__

import censored_strings


def test_answer():
    assert (
        censored_strings.uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo")
        == "Where did my vowels go?"
    )
    assert censored_strings.uncensor("abcd", "") == "abcd"
    assert censored_strings.uncensor("*PP*RC*S*", "UEAE") == "UPPERCASE"
    assert censored_strings.uncensor("*PP*RC*SE", "UEAE") == "UPPERCASE"
    assert censored_strings.uncensor("*PP*RC*S*", "UEAEO") == "UPPERCASE"
