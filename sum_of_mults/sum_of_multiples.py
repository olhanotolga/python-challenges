__doc__


def sum_of_multiples(num1, num2, from_to):
    """
    The function calculates the sum of multiples of num1 and num2 within the range from_to.

    Takes 3 arguments of types:

    1. numeric

    2. numeric

    3. sequence/list.

    Returns the sum of all multiples within the range provided in the list.
    """

    # just in case, sort the from_to sequence
    from_to.sort()
    fr = from_to[0]
    to = from_to[1]

    return sum([i for i in range(fr, to) if i % num1 == 0 or i % num2 == 0])


def main():
    n1 = 3
    n2 = 7
    start = 1
    end = 2000
    answer = sum_of_multiples(n1, n2, [start, end])
    print(
        f"Sum of all numbers between {start} and {end} that are multiples of {n1} and {n2} is {answer}."
    )


if __name__ == "__main__":
    main()
