# Wash Your Hands

## Challenge

It takes 21 seconds to wash your hands and help prevent the spread of COVID-19.

Create a function that takes the number of times a person washes their hands per day **N** and the number of months they follow this routine **nM** and calculates the duration in **minutes and seconds** that person spends washing their hands.

## Pseudocode

```pseudocode
function wash_hands(times_a_day, n_months):
	total_seconds = twenty_one_seconds * times_a_day * days_in_month * n_months
	
	full_minutes = total_seconds // 60
	rest_seconds = total_seconds % 60

	return 'You spent {full_minutes} min {rest_seconds} sec washing your hands!'
```

## Tests

`wash_hands(8, 7)` outputs "588 minutes and 0 seconds"

`wash_hands(0, 0)` outputs "0 minutes and 0 seconds"

`wash_hands(7, 9)` outputs "661 minutes and 30 seconds"