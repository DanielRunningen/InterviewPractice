# addTwoHugeNumbers

**Source: [CodeSignal](https://app.codesignal.com/)**  
This question is listed as "easy" on their site and is intended to take 30 minutes.

## Problem

You're given `2` huge integers represented by linked lists. Each linked list element is a number from `0` to `9999` that represents a number with exactly `4` digits.
The represented number might have leading zeros.
Your task is to add up these huge integers and return the result in the same format.

## Example

For `a = [9876, 5432, 1999]` and `b = [1, 8001]`, the output should be `addTwoHugeNumbers(a, b) = [9876, 5434, 0]`.

Explanation: `987654321999 + 18001 = 987654340000`.

For `a = [123, 4, 5]` and b = `[100, 100, 100]`, the output should be `addTwoHugeNumbers(a, b) = [223, 104, 105]`.

Explanation: `12300040005 + 10001000100 = 22301040105`.

## Input/Output

* Execution time limit: 4 seconds (py3)
* Inputs:
   * `a` as a singly linked list of integers
      * Guaranteed constraints
         * `0 ≤ a size ≤ 10^4`
         * `0 ≤ element value ≤ 9999`
   * `b` as a singly linked list of integers
      * Guaranteed constraints
         * `0 ≤ a size ≤ 10^4`
         * `0 ≤ element value ≤ 9999`
* Output: a singly linked list of integers that represent the sum of `a` and `b`.
