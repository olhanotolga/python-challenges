# Pluralize

## Challenge

Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.

### Notes

- This is an oversimplification of the English language so no edge cases will appear.
- Only focus on whether or not to add an `s` to the ends of words.

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
