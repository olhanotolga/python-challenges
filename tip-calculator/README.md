# Tip calculator

For any number of guests sharing a restaurant bill, calculate how much tip each guest needs to pay.

Use variables to store the number of guests, the amount of the bill and the tip in percentage, e.g.

```python
guest = 2
bill = 80
tipPercentage = 10
```

Create a function which takes these values as input and outputs the total amount each guest needs to pay as well as the amount of tip that is included, eg `Each guest needs to pay: 44 euro` and `The amount of tip for each guest is: 4 euro`.

## Pseudocode

```pseudo
func(num_guests, bill_total, tip_percentage):
	bill_each = bill_total / num_guests
	tip_each = bill_each * tip_percentage/100
	bill_w_tip_each = bill_each + tip_each
	
	output: "Each guest needs to pay {bill_each} EUR + {tip_each} EUR tip — a total of {bill_w_tip_each} EUR."
```

## Tests

```python
assert calculate_tip(2, 80, 10) == "Each guest needs to pay 40.0 EUR + 4.0 EUR tip — a total of 44.0 EUR."
assert calculate_tip(4, 50, 10) == "Each guest needs to pay 12.5 EUR + 1.25 EUR tip — a total of 13.75 EUR (rounded to 14)."
assert calculate_tip(3, 80, 8) == "Each guest needs to pay 26.67 EUR + 2.13 EUR tip — a total of 28.8 EUR (rounded to 29)."
```
