# mergeTwoLinkedList

**Source: [CodeSignal](https://app.codesignal.com/)**  
This question is listed as "medium" on their site and is intended to take 30 minutes.

## Problem

Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

_Note: Your solution should have `O(l1.length + l2.length)` time complexity, since this is what you will be asked to accomplish in an interview._

## Example

For `l1 = [1, 2, 3]` and `l2 = [4, 5, 6]`, the output should be `mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6]`.

For `l1 = [1, 1, 2, 4]` and `l2 = [0, 3, 5]`, the output should be `mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5]`.

## Input/Output

* Execution time limit: 4 seconds (py3)
* Inputs:
   * `l1` as a singly linked list of integers n ascending order
      * Guaranteed constraints
         * `0 ≤ list size ≤ 10^4`
         * `-10^9 ≤ element value ≤ 10^9`
   * `l2` as a singly linked list of integers n ascending order
      * Guaranteed constraints
         * `0 ≤ list size ≤ 10^4`
         * `-10^9 ≤ element value ≤ 10^9`
* Output: a singly linked list of integers in ascending order that contains all elements from both `l1` and `l2`.
