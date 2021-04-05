__doc__


def wash_hands(n_times, n_months):
    """
    The function takes 2 arguments:

                n_times: int

                n_months: int

    Return value: formatted string which contains digital representation of full total minutes and the remainder in seconds.

    Internal constants:

                - 21 seconds — duration of hand washing (int)

                - 30 days — average number of days in one month (int)

    """

    # constants
    n_sec = 21
    days_in_month = 30

    total_seconds = n_sec * n_times * days_in_month * n_months
    full_minutes = total_seconds // 60
    rest_seconds = total_seconds % 60

    return f"You spent {full_minutes} min {rest_seconds} sec washing your hands!"


def main():
    answer1 = wash_hands(8, 7)
    answer2 = wash_hands(0, 0)
    answer3 = wash_hands(7, 9)
    print(answer1)
    print(answer2)
    print(answer3)


if __name__ == "__main__":
    main()
