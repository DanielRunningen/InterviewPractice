import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers.listNode import listToLinkedList

import unittest
import timeout_decorator
from solution import addTwoHugeNumbers

EXECUTION_TIME_LIMIT = 4

# Singly-linked lists are pre-defined in CodeSignal with this interface:
# class ListNode:
#    def __init__(self, x):
#       self.value = x
#       self.next = None

class Tests(unittest.TestCase):
   def setUp(self):
      self.example1 = {
         'a': listToLinkedList([9876, 5432, 1999]),
         'b': listToLinkedList([1, 8001])
      }
      self.example2 = {
         'a': listToLinkedList([123, 4, 5]),
         'b': listToLinkedList([100, 100, 100])
      }

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_1(self):
      expected = [9876, 5434, 0]
      actual = addTwoHugeNumbers(self.example1['a'], self.example1['b']).toList()
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_2(self):
      expected = [223, 104, 105]
      actual = addTwoHugeNumbers(self.example2['a'], self.example2['b']).toList()
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_3(self):
      expected = [0]
      actual = addTwoHugeNumbers(
         listToLinkedList([0]),
         listToLinkedList([0])
      ).toList()
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_4(self):
      expected = [1234, 1234, 0]
      actual = addTwoHugeNumbers(
         listToLinkedList([1234, 1234, 0]),
         listToLinkedList([0])
      ).toList()
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_5(self):
      expected = [1234, 123, 0]
      actual = addTwoHugeNumbers(
         listToLinkedList([0]),
         listToLinkedList([1234, 123, 0])
      ).toList()
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_6(self):
      expected = [9999, 0, 0, 0, 0, 0]
      actual = addTwoHugeNumbers(
         listToLinkedList([1]),
         listToLinkedList([9998, 9999, 9999, 9999, 9999, 9999])
      ).toList()
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_7(self):
      expected = [1, 0, 0, 0, 0, 0, 0]
      actual = addTwoHugeNumbers(
         listToLinkedList([1]),
         listToLinkedList([9999, 9999, 9999, 9999, 9999, 9999])
      ).toList()
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_8(self):
      expected = [8339, 6819]
      actual = addTwoHugeNumbers(
         listToLinkedList([2309]),
         listToLinkedList([8339, 4510])
      ).toList()
      self.assertEqual(actual, expected)

if __name__ == '__main__':
   unittest.main()
