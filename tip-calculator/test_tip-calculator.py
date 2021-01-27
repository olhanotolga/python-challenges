def calculate_tip(num_guests, bill_total, tip_perc):
	bill_each = round(bill_total / num_guests, 2)
	tip_each = round(bill_each * tip_perc/100, 2)
	bill_w_tip_each = bill_each + tip_each
	
	optional_roundup = ""
	if bill_w_tip_each != round(bill_w_tip_each):
		optional_roundup = f" (rounded to {round(bill_w_tip_each)})"

	output = f"Each guest needs to pay {bill_each} EUR + {tip_each} EUR tip — a total of {bill_w_tip_each} EUR{optional_roundup}."
	
	return output

def test_answer():
	assert calculate_tip(2, 80, 10) == "Each guest needs to pay 40.0 EUR + 4.0 EUR tip — a total of 44.0 EUR."
	assert calculate_tip(4, 50, 10) == "Each guest needs to pay 12.5 EUR + 1.25 EUR tip — a total of 13.75 EUR (rounded to 14)."
	assert calculate_tip(3, 80, 8) == "Each guest needs to pay 26.67 EUR + 2.13 EUR tip — a total of 28.8 EUR (rounded to 29)."