# firstNotRepeatingCharacter

**Source: [CodeSignal](https://app.codesignal.com/)**  
This question is listed as "easy" on their site and is intended to take 15 minutes.  
It is supposedly one of the questions asked by Amazon during interviews.

## Problem

Given a string `s` consisting of small English letters, find and return the first instance of a non-repeating character in it.
If there is no such character, return `'_'`.

## Example

For `s = "abacabad"`, the output should be `firstNotRepeatingCharacter(s) = 'c'`.

There are 2 non-repeating characters in the string: `'c'` and `'d'`. Return `'c'` since it appears in the string first.

For `s = "abacabaabacaba"`, the output should be `firstNotRepeatingCharacter(s) = '_'`.

There are no characters in this string that do not repeat.

## Input/Output

* Execution time limit: 4 seconds (py3)
* Type: string `s`
* Guaranteed constraints
  * A string that contains only lowercase English letters.
  * `1 ≤ s.length ≤ 105`
* Output: char, the first non-repeating character in `s`, or `'_'` if there are no characters that do not repeat.
