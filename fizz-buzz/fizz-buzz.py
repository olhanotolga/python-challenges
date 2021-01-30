__doc__

import sys

def fizz_buzz(num1, num2, end_range):

	"""
	Function accepts three integers as input and prints all values within the range between 1 and the input value with the following exceptions:
	1. when current value is a multiple of num1, "Fizz" is printed.
	2. when current value is a multiple of num2, "Buzz" is printed
	3. when current value is a multiple of both num1 and num2, "FizzBuzz" is printed
	"""

	# checking for validity of arguments: should be a positive integer
	if not (isinstance(num1, int) and isinstance(num2, int) and isinstance(end_range, int)) or (num1 < 0 or num2 < 0 or end_range < 0):
		return 'Input should be a positive integer'

	for i in range(1, end_range):
		output = i
		if (i % num1 == 0 and i % num2 == 0):
			output = "FizzBuzz"
		elif (i % num1 == 0):
			output = "Fizz"
		elif (i % num2 == 0):
			output = "Buzz"
		print(output)
	
"""
The main function call introduces error handling, e.g. for cases when a smaller number of arguments is provided.
"""

def main():
	mult_a = 3
	mult_b = 5
	range = 16
	try:
		fizz_buzz(mult_a, mult_b, range)
		print("--------------")
		fizz_buzz(range)
	except:
		print("An error occurred:", sys.exc_info()[1])


if __name__ == '__main__':
	main()