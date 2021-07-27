import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers.listNode import listToLinkedList

import unittest
import timeout_decorator
from solution import mergeTwoLinkedLists

EXECUTION_TIME_LIMIT = 4

class Tests(unittest.TestCase):
   def setUp(self):
      self.example1 = {
         'l1': listToLinkedList([1, 2, 3]),
         'l2': listToLinkedList([4, 5, 6])
      }
      self.example2 = {
         'l1': listToLinkedList([1, 1, 2, 4]),
         'l2': listToLinkedList([0, 3, 5])
      }

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_1(self):
      expected = [1, 2, 3, 4, 5, 6]
      actual = mergeTwoLinkedLists(self.example1['l1'], self.example1['l2']).toList()
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_2(self):
      expected = [0, 1, 1, 2, 3, 4, 5]
      actual = mergeTwoLinkedLists(self.example2['l1'], self.example2['l2']).toList()
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_3(self):
      expected = [2, 3, 5, 10, 15, 20, 40]
      actual = mergeTwoLinkedLists(
         listToLinkedList([5, 10, 15, 40]),
         listToLinkedList([2, 3, 20])
      ).toList()
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_4(self):
      expected = [1, 1, 2, 4]
      actual = mergeTwoLinkedLists(
         listToLinkedList([1, 1]),
         listToLinkedList([2, 4])
      ).toList()
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_5(self):
      expected = [1, 1, 2, 2, 4, 7, 7, 8]
      actual = mergeTwoLinkedLists(
         listToLinkedList([]),
         listToLinkedList([1, 1, 2, 2, 4, 7, 7, 8])
      ).toList()
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_6(self):
      expected = None
      actual = mergeTwoLinkedLists(None, None)
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_7(self):
      expected = [1, 1, 4]
      actual = mergeTwoLinkedLists(
         listToLinkedList([1, 1, 4]),
         listToLinkedList([])
      ).toList()
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_8(self):
      expected = [0, 1, 1]
      actual = mergeTwoLinkedLists(
         listToLinkedList([1, 1]),
         listToLinkedList([0])
      ).toList()
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_9(self):
      expected = [0, 2]
      actual = mergeTwoLinkedLists(
         listToLinkedList([0]),
         listToLinkedList([2])
      ).toList()
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_10(self):
      expected = [-1000000000, 1, 1000000000]
      actual = mergeTwoLinkedLists(
         listToLinkedList([1]),
         listToLinkedList([-1000000000, 1000000000])
      ).toList()
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_11(self):
      expected = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
      actual = mergeTwoLinkedLists(
         listToLinkedList([-1, -1, 0, 1]),
         listToLinkedList([-1, 0, 0, 1, 1])
      ).toList()
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_12(self):
      expected = [
         -815817641, -780990573, -670826849, -426491047, -404817961,
         242026249, 437929670, 520408640, 731519938
      ]
      actual = mergeTwoLinkedLists(
         listToLinkedList([-780990573, -670826849, -404817961, 242026249, 731519938]),
         listToLinkedList([-815817641, -426491047, 437929670, 520408640])
      ).toList()
      self.assertEqual(actual, expected)

if __name__ == '__main__':
   unittest.main()
