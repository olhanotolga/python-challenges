# Palindrome Checker

## Challenge

A palindrome is a number/string that is same forwards and backwards. For example 545, 151, 34543, 343, 171, 48984 are palindrome. A string like LOL, MADAM are also palindromes. Write a function called `is_palindrome` that takes an variable and returns `True` (or `False`) if the variable is (or not) a palindrome.

## Pseudocode

```pseudo
function is_palindrome(input):
	exceptions = [" ", "!", "?", ".", ",", "-", "–", "—", "_"]

	if type(input) != "int" && type(input) != "float" && type(input) != "str":
		return "Unsupported input type"

	if type(input) == "int" || type(input) == "float":
		str(input)

	if type(input) == "str":
		clean_input = ""
		for ch in input:
			if (! ch in exceptions):
				clean_input += ch
		clean_input = clean_input.lowercase()

		length = len(clean_input)
		half = round(length / 2)
		
		for i in range(half):
			if (! input[i] == input[length - 1 - i]):
				return False
		
		return True

```

## Tests

```python
assert is_palindrome(34543) == True
assert is_palindrome("Madam") == True
assert is_palindrome("In girum imus nocte et consumimur igni") == True
assert is_palindrome("I am a palindrome") == False
assert is_palindrome(["M", "A", "D", "A", "M"]) == "Unsupported input type"

```
