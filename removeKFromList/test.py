import unittest
import timeout_decorator
from solution import removeKFromList

EXECUTION_TIME_LIMIT = 4

# Singly-linked lists are pre-defined in CodeSignal with this interface:
class ListNode:
   def __init__(self, x):
      self.value = x
      self.next = None

   def toList(self):
      l = [self.value]
      if self.next is not None:
         l.extend(self.next.toList())
      return l

def listToLinkedList(l):
   head = None
   last = None
   while len(l) > 0:
      head = ListNode(l.pop())
      head.next = last
      last = head
   return head

class Tests(unittest.TestCase):
   def setUp(self):
      self.example1 = {
         'l': listToLinkedList([3, 1, 2, 3, 4, 5]),
         'k': 3
      }
      self.example2 = {
         'l': listToLinkedList([1, 2, 3, 4, 5, 6, 7]),
         'k': 10
      }

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_1(self):
      expected = [1, 2, 4, 5]
      actual = removeKFromList(self.example1['l'], self.example1['k']).toList()
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_2(self):
      expected = [1, 2, 3, 4, 5, 6, 7]
      actual = removeKFromList(self.example2['l'], self.example2['k']).toList()
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_3(self):
      expected = None
      actual = removeKFromList(listToLinkedList([1000, 1000]), 1000)
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_4(self):
      expected = None
      actual = removeKFromList(None, -1000)
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_5(self):
      expected = [123, 456, 789]
      actual = removeKFromList(listToLinkedList([123, 456, 789, 0]), 0).toList()
      self.assertEqual(actual, expected)

if __name__ == '__main__':
   unittest.main()
