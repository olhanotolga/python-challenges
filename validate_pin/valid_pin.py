__doc__

import re

"""
The function checks the input against a set of conditions and returns a boolean.

Input value: string.

Output: boolean.

Exception: if the input is not of the type string, the returned value is "Must be a string."
"""


def valid(pin):
    if not isinstance(pin, str):
        return "Must be a string"

    pattern = r"^(\d{4})$|^(\d{6})$"
    result = re.match(pattern, pin)

    if result:
        return True
    else:
        return False


def main():
    answer0 = valid("123045")
    answer1 = valid("12345")
    answer2 = valid("")
    answer3 = valid("abc456")
    answer4 = valid(123456)

    print(answer0)
    print(answer1)
    print(answer2)
    print(answer3)
    print(answer4)


if __name__ == "__main__":
    main()
