# Validate Pin

## Challenge

Create a function to test if a string is a valid pin or not.

A valid pin has:

- Exactly 4 or 6 characters.
- Only numerical characters (0-9).
- No whitespace.

## Pseudocode

```pseudocode
function valid(pin):
	if not string:
		return False

	regex = /^(\d{4})$|^(\d{6})$/

	if regex.match(pin):
		return True
	else:
		return False

```

## Tests

`valid("1234")` ➞ True
`valid("45135")` ➞ False
`valid("89abc1")` ➞ False
`valid("900876")` ➞ True
`valid(" 4983")` ➞ False
`valid("")` ➞ False
