# C\*ns\*r\*d Str\*ngs

## Challenge

Someone has attempted to censor my strings by replacing every vowel with a `*`, `l*k* th*s`. Luckily, I've been able to find the vowels that were removed.

Given a censored string and a string of the censored vowels, return the original uncensored string.

### Notes

- The vowels are given in the correct order.
- The number of vowels will match the number of `*` characters in the censored string.

## Pseudocode

```pseudocode
function uncensor(censored_str, vowels_str):
	ready_for_formatting = censored_str.replace('*', '{}')

	vowels_list = list(vowels_str)
	
	formatted = ready_for_formatting.format(*vowels_list)

	return formatted
```

## Tests

`uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo")` ➞ `"Where did my vowels go?"`

`uncensor("abcd", "")` ➞ `"abcd"`

`uncensor("*PP*RC*S*", "UEAE")` ➞ `"UPPERCASE"`
