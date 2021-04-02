# Positive — Negative

## Challenge

Given two strings comprised of + and -, return a new string which shows how the two strings interact in the following way:

- When positives and positives interact, they remain positive.
- When negatives and negatives interact, they remain negative.
- But when negatives and positives interact, they become neutral, and are shown as the number 0.

### Example

```pseudocode
neutralize("+-+", "+--") ➞ "+-0"
# Compare the first characters of each string, then the next in turn.
# "+" against a "+" returns another "+".
# "-" against a "-" returns another "-".
# "+" against a "-" returns "0".
# Return the string of characters.
```

**Note:** The two strings will be the same length.

## Pseudocode

```pseudocode
function neutralize(str1, str2):
		output = ''

		rules = {
			"++": "+",
			"--": "-",
			"+-": "0"
		}

		for i in range(len(str1)):
			output += rules[str1[i] + str2[i]]
		
		return output
```

## Tests

`neutralize("--++--", "++--++")` ➞ `"000000"`

`neutralize("-+-+-+", "-+-+-+")` ➞ `"-+-+-+"`

`neutralize("-++-", "-+-+")` ➞ `"-+00"`
