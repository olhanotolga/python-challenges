def is_palindrome(input):
	exceptions = [" ", "!", "?", ".", ",", "-", "–", "—", "_"]

	if not isinstance(input, int) and not isinstance(input, float) and not isinstance(input, str):
		return "Unsupported input type"

	if isinstance(input, int) or isinstance(input, float):
		input = str(input)

	if isinstance(input, str):
		clean_input = ""
		for ch in input:
			if (not ch in exceptions):
				clean_input += ch
		lc_clean_input = clean_input.lower()

		length = len(lc_clean_input)
		half = round(length / 2)
		for i in range(half):
			if (not lc_clean_input[i] == lc_clean_input[length - 1 - i]):
				return False

		return True

def test_answer():
	assert is_palindrome(34543) == True
	assert is_palindrome("Madam") == True
	assert is_palindrome("In girum imus nocte et consumimur igni") == True
	assert is_palindrome("I am a palindrome") == False
	assert is_palindrome(["M", "A", "D", "A", "M"]) == "Unsupported input type"