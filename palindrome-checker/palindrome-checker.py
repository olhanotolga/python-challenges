__doc__

def is_palindrome(input):
	"""
	Takes one argument and checks whether it is symmetrical/palindrome. Returns True or False.
	
	Constraints: accepts arguments of numeric types or a string. In case of the former, the input is first converted to a string.

	Additional: case-insensitive; spaces and characters such as "!", "?", ".", etc. are ignored.
	"""

	# an array of ignored characters
	exceptions = [" ", "!", "?", ".", ",", "-", "–", "—", "_"]

	# early return for unsupported input types
	if not isinstance(input, int) and not isinstance(input, float) and not isinstance(input, str):
		return "Unsupported input type"

	# numeric input is converted into a string
	if isinstance(input, int) or isinstance(input, float):
		input = str(input)

	if isinstance(input, str):
		# to truly ignore certain characters, we need to strip the input of them completely
		clean_input = ""
		for ch in input:
			if (not ch in exceptions):
				clean_input += ch
		
		# this renders our string case-insensitive
		lc_clean_input = clean_input.lower()

		length = len(lc_clean_input)
		half = round(length / 2)
		
		# reading the string from the start and back at the same time, comparing characters until the middle
		for i in range(half):
			if (not lc_clean_input[i] == lc_clean_input[length - 1 - i]):
				return False

		return True


def main():
	answer1 = is_palindrome(12378)
	answer2 = is_palindrome("In girum imus nocte et consumimur igni.")
	answer3 = is_palindrome(["M", "A", "D", "A", "M"])
	print(answer1)
	print(answer2)
	print(answer3)

if __name__ == '__main__':
	main()
