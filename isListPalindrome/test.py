import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers.listNode import listToLinkedList

import unittest
import timeout_decorator
from solution import isListPalindrome

EXECUTION_TIME_LIMIT = 4

# Singly-linked lists are pre-defined in CodeSignal with this interface:
# class ListNode:
#    def __init__(self, x):
#       self.value = x
#       self.next = None

class Tests(unittest.TestCase):
   def setUp(self):
      self.example1 = [0, 1, 0]
      self.example2 = [1, 2, 2, 3]

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_1(self):
      expected = True
      actual = isListPalindrome(listToLinkedList(self.example1))
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_2(self):
      expected = False
      actual = isListPalindrome(listToLinkedList(self.example2))
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_3(self):
      expected = True
      actual = isListPalindrome(
         listToLinkedList(
            [1, 1000000000, -1000000000, -1000000000, 1000000000, 1]
         )
      )
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_4(self):
      expected = False
      actual = isListPalindrome(listToLinkedList([1, 2, 3, 3, 2]))
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_5(self):
      expected = False
      actual = isListPalindrome(listToLinkedList([1, 2, 3, 1, 2, 3]))
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_6(self):
      expected = True
      actual = isListPalindrome(None)
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_7(self):
      expected = False
      actual = isListPalindrome(listToLinkedList([3, 5, 3, 5]))
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_8(self):
      expected = False
      actual = isListPalindrome(listToLinkedList([1, 5, 2, 4]))
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_9(self):
      expected = True
      actual = isListPalindrome(listToLinkedList([10]))
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_10(self):
      expected = True
      actual = isListPalindrome(listToLinkedList([0, 0]))
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_11(self):
      expected = False
      actual = isListPalindrome(listToLinkedList([1, 3, 2, 2, 2]))
      self.assertEqual(actual, expected)

if __name__ == '__main__':
   unittest.main()
