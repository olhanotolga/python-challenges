def wash_hands(n_times, n_months):
	n_sec = 21
	days_in_month = 30
	total_seconds = n_sec * n_times * days_in_month * n_months
	full_minutes = total_seconds // 60
	rest_seconds = total_seconds % 60
	return f'You spent {full_minutes} min {rest_seconds} sec washing your hands!'

def test_answer():
	assert wash_hands(8, 7) == 'You spent 588 min 0 sec washing your hands!'
	assert wash_hands(0, 0) == 'You spent 0 min 0 sec washing your hands!'
	assert wash_hands(7, 9) == 'You spent 661 min 30 sec washing your hands!'