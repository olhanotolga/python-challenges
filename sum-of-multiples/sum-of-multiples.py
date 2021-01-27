__doc__
# calculate the sum of multiples of 3 and 5 in a range from 1 to 1000

def sum_of_multiples(num1, num2, from_to):
	"""
	Takes 3 arguments of types:
	1. numeric
	2. numeric
	3. sequence.
	Returns the sum of all multiples within the range provided in the list.
	"""
	from_to.sort()
	fr = from_to[0]
	to = from_to[1]
	total = 0
	for i in range(fr, to):
		if i % num1 == 0 or i % num2 == 0:
			total += i
	return total

def main():
	n1 = 3
	n2 = 7
	start = 1
	end = 200
	answer = sum_of_multiples(n1, n2, [start, end])
	print(f"Sum of all numbers between {start} and {end} that are multiples of {n1} and {n2} is {answer}.")

if __name__ == '__main__':
	main()