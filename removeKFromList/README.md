# removeKFromList

**Source: [CodeSignal](https://app.codesignal.com/)**  
This question is listed as "easy" on their site and is intended to take 15 minutes.

## Problem

Given a singly linked list of integers `l` and an integer `k`, remove all elements from list `l` that have a value equal to `k`.

_Note: Try to solve this task in `O(n)` time using `O(1)` additional space, where n is the number of elements in the list, since this is what you'll be asked to do during an interview._

_Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node `l` of the linked list._

## Example

For `l = [3, 1, 2, 3, 4, 5]` and `k = 3`, the output should be `removeKFromList(l, k) = [1, 2, 4, 5]`.

For `l = [1, 2, 3, 4, 5, 6, 7]` and `k = 10`, the output should be `removeKFromList(l, k) = [1, 2, 3, 4, 5, 6, 7]`.

## Input/Output

* Execution time limit: Execution time limit: 4 seconds (py3)
* Inputs:
   * `l` as a singly linked list of integers
      * Guaranteed constraints
         * `0 ≤ list size ≤ 10^5`
         * `-1000 ≤ element value ≤ 1000`
   * `k` as an integer
      * Guaranteed constraints
         * `-1000 ≤ k ≤ 1000`
* Output: a singly linked list of integers, `l` with all instances of `k` removed.
