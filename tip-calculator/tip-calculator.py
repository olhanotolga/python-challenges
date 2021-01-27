__doc__

# For any number of guests sharing a restaurant bill, calculate how much tip each guest needs to pay.

def calculate_tip(num_guests, bill_total, tip_perc):
	"""
	Takes 3 numeric arguments: number of guests, a total bill, and the tip percentage.
	Returns a string specifying the bare sum each need to pay, the individual tip amount, and the individual total, optionally rounded.
	"""

	bill_each = round(bill_total / num_guests, 2)
	tip_each = round(bill_each * tip_perc/100, 2)
	bill_w_tip_each = bill_each + tip_each
	
	optional_roundup = ""
	if bill_w_tip_each != round(bill_w_tip_each):
		optional_roundup = f" (rounded to {round(bill_w_tip_each)})"

	output = f"Each guest needs to pay {bill_each} EUR + {tip_each} EUR tip — a total of {bill_w_tip_each} EUR{optional_roundup}."
	
	return output

def main():
	n = 2
	b = 80
	t = 10
	answer = calculate_tip(n, b, t)
	print(answer)

if __name__ == '__main__':
	main()
