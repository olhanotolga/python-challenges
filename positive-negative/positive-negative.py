import re

"""
Function neutralize takes two eqal-length input strings. It returns one string of the same length where each character is the result of interaction between the character in string 1 and string 2 at the same index.

- When "+" and "+" interact, they remain "+".
- When "-" and "-" interact, they remain "-".
- But when "-" and "+" interact, they become "0".

Arguments: 2 strings containing of exclusively "+" and/or "-" characters.

Output: 1 string containing of exclusively "+", "-", or "0" characters.
"""


def neutralize(str1, str2):
    # type check
    if not isinstance(str1, str) or not isinstance(str2, str):
        return "Must be a string"

    # input strings should be of the equal length
    if not len(str1) == len(str2):
        return "Lengths don't match"

    # check for valid characters (only '+' and '-' are accepted)
    pattern = "^[+-]+$"
    if not re.match(pattern, str1) or not re.match(pattern, str2):
        return "Invalid pattern"

    output = ""

    # instead of writing a series of "if" statements, I used a dictionary
    rules = {"++": "+", "--": "-", "+-": "0", "-+": "0"}

    for i in range(len(str1)):
        output += rules[str1[i] + str2[i]]

    return output


def main():
    answer1 = neutralize("+-+", "+--")
    answer2 = neutralize("--++--", "++--++")
    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
