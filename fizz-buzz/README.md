# FizzBuzz

## Challenge

- The given code takes 3 arguments: `factor1`, `factor2`, and a `range`, and outputs the numbers from 1 to n.
- For each multiple of `factor1`, print "Fizz" instead of the number.
- For each multiple of `factor2`, prints "Buzz" instead of the number.
- For numbers which are multiples of both `factor1` and `factor2`, output "FizzBuzz".

## Pseudocode

```pseudo

function fizz_buzz(factor1, factor2, range):
	if (! typeof(range) is int):
		return 'Input should be an integer'

	for i up to range:
		if (i % factor1 == 0 AND i % factor2 == 0):
			print("FizzBuzz)
		elif (i % factor1 == 0):
			print("Fizz")
		elif (i % factor2 == 0):
			print("Buzz")
		else:
			print(i)
```

## Test cases

`fizz_buzz(3, 5, 16)` outputs the following values: `1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz'`

`fizz_buzz(2, 7, 20)` outputs the following values: 1, `'Fizz', 3, 'Fizz', 5, 'Fizz', 'Buzz', 'Fizz', 9, 'Fizz', 11, 'Fizz', 13, 'FizzBuzz', 15, 'Fizz', 17, 'Fizz', 19`

`fizz_buzz(100)` prints an error because the function requires 3 arguments
