__doc__

from palindrome_checker import is_palindrome


def test_answer():
    assert is_palindrome(34543) == True
    assert is_palindrome("Madam") == True
    assert is_palindrome("In girum imus nocte et consumimur igni") == True
    assert is_palindrome("I am a palindrome") == False
    assert is_palindrome(["M", "A", "D", "A", "M"]) == "Unsupported input type"
