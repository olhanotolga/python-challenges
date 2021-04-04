__doc__

import irregular_plurals

irregular_pl_list = irregular_plurals.irregular_plurals


def change_to_plural(word):
    """
    Helper function which takes a word and returns its plural form.
    """

    last_letter = word[len(word) - 1]

    if irregular_pl_list.get(word):
        return irregular_pl_list[word]

    elif last_letter == "s" or last_letter == "x" or last_letter == "z":
        return word + "es"

    else:
        return word + "s"


def pluralize(list):
    """
    1. The function takes one argument — a list.

    2. It returns a set of the list items.

    3. Items which occurred in the original list more than once are added in their multiple form.
    """

    # iterate through the list
    # and register the number of occurrences with a dictionary
    items_dict = {}
    for item in list:
        if not items_dict.get(item):
            items_dict[item] = 1
        else:
            items_dict[item] += 1

    # loop through the dictionary,
    # modify words that occur more than once,
    # create a set with both modified and unmodified items
    final_set = set()
    for d_item in items_dict:
        if items_dict[d_item] > 1:
            final_set.add(change_to_plural(d_item))
        elif items_dict[d_item] == 1:
            final_set.add(d_item)

    return final_set


def main():
    answer1 = pluralize(["cow", "pig", "cow", "cow"])  # { "cows", "pig" }
    answer2 = pluralize(["table", "table", "table"])  # { "tables" }
    answer3 = pluralize(["chair", "pencil", "arm"])  # { "chair", "pencil", "arm" }
    print(answer1)
    print(answer2)
    print(answer3)


if __name__ == "__main__":
    main()
