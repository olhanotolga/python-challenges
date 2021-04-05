from sum_of_multiples import sum_of_multiples


def test_answer():
    assert sum_of_multiples(3, 5, [1, 10]) == 23
    assert sum_of_multiples(3, 5, [1, 100]) == 2318
    assert sum_of_multiples(3, 5, [1, 1000]) == 233168
    assert sum_of_multiples(3, 5, [1, 10000]) == 23331668
    assert sum_of_multiples(3, 7, [1, 200]) == 8530
