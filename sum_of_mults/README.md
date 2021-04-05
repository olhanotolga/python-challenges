# Sum of multiples

## Description

Calculate the sum of multiples of 3 and 5 in a range from 0 to 1000.

## Pseudocode

```pseudo
func(num1, num2, range_start, range_end):
	sum = 0
	for i from range_start to range_end:
		if (i % num1 == 0) or (i % num2 == 0):
			sum += i

```

## Tests

```python
assert sum_of_multiples(3, 5, [1, 10]) == 23
assert sum_of_multiples(3, 5, [1, 100]) == 2318
assert sum_of_multiples(3, 5, [1, 1000]) == 233168
assert sum_of_multiples(3, 5, [1, 10000]) == 23331668
assert sum_of_multiples(3, 7, [1, 200]) == 8530
```
