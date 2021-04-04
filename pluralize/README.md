# Pluralize

## Challenge

Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.

### Notes

Although no irregular plural forms were meant to appear in test cases, I included 100 most common irregular nouns which I check against in a helper function (see `pluralize.py`).

## Pseudocode

```pseudocode

function pluralize(list):
	# iterate through the list and register multiple occurrences
	
	items_dict = {}
	for item in list:
		if not items_dict.get(item):
			items_dict[item] = 1
		else:
			items_dict[item]++
	
	# modify words that occur more than once
	# create a set
	
	final_set = set()
	for d_item in items_dict:
		if items_dict[d_item] > 1:
			final_set.add(d_item + 's')
		elif items_dict[d_item] == 1:
			final_set.add(d_item)
	
	return final_set

```

## Tests

`pluralize(["cow", "pig", "cow", "cow"])` ➞ `{ "cows", "pig" }`

`pluralize(["table", "table", "table"])` ➞ `{ "tables" }`

`pluralize(["chair", "pencil", "arm"])` ➞ `{ "chair", "pencil", "arm" }`
