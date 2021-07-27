# isListPalindrome

**Source: [CodeSignal](https://app.codesignal.com/)**
This question is listed as "easy" on their site and is intended to take 30 minutes.
It is supposedly one of the questions asked by Amazon and Facebook during interviews.

## Problem

Given a singly linked list of integers, determine whether or not it's a palindrome.

_Note: Try to solve this task in `O(n)` time using `O(1)` additional space, where `n` is the number of elements in `l`, since this is what you'll be asked to do during an interview._

_Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node `l` of the linked list._

## Example

For `l = [0, 1, 0]`, the output should be `isListPalindrome(l) = true`.

For `l = [1, 2, 2, 3]`, the output should be `isListPalindrome(l) = false`.

## Input/Output

* Execution time limit: Execution time limit: 4 seconds (py3)
* Inputs:
   * `l` as a singly linked list of integers
      * Guaranteed constraints
         * `0 ≤ list size ≤ 5 · 10^5`
         * `-10^9 ≤ element value ≤ 10^9`
* Output: boolean, `true` if `l` is a palindrome, otherwise return `false`.
