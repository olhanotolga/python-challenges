__doc__


def type_check(string):
    if not isinstance(string, str):
        return False
    return True


def uncensor(censored_str, chars_str):
    """
    The function takes 2 arguments:

    - a string with '*' denoting censored characters
    - a string of characters which should replace the '*'s

    The function returns a formatted (uncensored) string.
    """

    # 0. do the checks
    if not type_check(censored_str) or not type_check(chars_str):
        return "The argument is not a string!"

    # 1. prepare the string to formatting by replacing * with {}
    ready_for_formatting = censored_str.replace("*", "{}")
    # 2. prapare the chars string by turning it into a list of arguments
    chars_list = list(chars_str)
    # 3. format the string — replace {} with corresponding chars
    formatted = ready_for_formatting.format(*chars_list)

    return formatted


def main():
    answer1 = uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo")  # "Where did my vowels go?"
    answer2 = uncensor("abcd", "")  # "abcd"
    answer3 = uncensor("*PP*RC*S*", "UEAE")  # "UPPERCASE"
    print(answer1)
    print(answer2)
    print(answer3)


if __name__ == "__main__":
    main()
