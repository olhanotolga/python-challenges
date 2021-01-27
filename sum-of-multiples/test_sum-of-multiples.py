def sum_of_multiples(num1, num2, from_to):
	from_to.sort()
	fr = from_to[0]
	to = from_to[1]
	total = 0
	for i in range(fr, to):
		if i % num1 == 0 or i % num2 == 0:
			total += i
	return total

def test_answer():
	assert sum_of_multiples(3, 5, [1, 10]) == 23
	assert sum_of_multiples(3, 5, [1, 100]) == 2318
	assert sum_of_multiples(3, 5, [1, 1000]) == 233168
	assert sum_of_multiples(3, 5, [1, 10000]) == 23331668
	assert sum_of_multiples(3, 7, [1, 200]) == 8530
