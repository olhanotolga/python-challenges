__doc__

import datetime


def valid_date(month, year):
    """
    Helper function which validates inputs
    """
    if not isinstance(month, int) or not isinstance(year, int):
        return False
    if month < 1 or month > 12:
        return False
    return True


def has_friday_13(month, year):
    """
    Function which takes 2 arguments as input:

    1 — integer between 1 and 12 (month)

    2 — 4-digit integer (year)

    The function checks whether the given month within the given year contains Friday, the 13th.

    Output value: boolean.

    """

    if not valid_date(month, year):
        return "Enter valid month and year!"

    day = 13
    # use datetime module to construct a date object with the given arguments
    date_obj = datetime.date(year, month, day)

    # use the .isoweekday() method to check the day of the week
    weekday = date_obj.isoweekday()

    # return True if it is Friday, otherwise return False
    if weekday == 5:
        return True
    else:
        return False


def main():
    answer1 = has_friday_13(3, 2020)  # True
    answer2 = has_friday_13(10, 2017)  # True
    answer3 = has_friday_13(1, 1985)  # False
    print(answer1)
    print(answer2)
    print(answer3)


if __name__ == "__main__":
    main()
