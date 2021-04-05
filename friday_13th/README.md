# Friday the 13th

## Challenge

Given the month and year as numbers, return whether that month contains a Friday 13th.

### Notes

January will be given as 1, February as 2, etc ...

## Pseudocode

```pseudocode
function has_friday_13(month, year):
	# use datetime module to construct a date object with the given arguments
	date_obj = date(year, month, 13)

	# use the .isoweekday() method to check the day of the week
	weekday = date_obj.isoweekday()

	# return True if it is Friday, otherwise return False
	if weekday == 5:
		return True
	else:
		return False
		
```

## Tests

`has_friday_13(3, 2020)` ➞ `True`

`has_friday_13(10, 2017)` ➞ `True`

`has_friday_13(1, 1985)` ➞ `False`
