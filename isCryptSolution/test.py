import unittest
import timeout_decorator
from solution import isCryptSolution

EXECUTION_TIME_LIMIT = 4

# All tests in this class come directly from CodeSignal
class CodeSignalTests(unittest.TestCase):
   def setUp(self):
      self.example1 = {
         'crypt': ['SEND', 'MORE', 'MONEY'],
         'solution': [
            ['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']
         ]
      }
      self.example2 = {
         'crypt': ['TEN', 'TWO', 'ONE'],
         'solution': [
            ['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']
         ]
      }

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_1(self):
      expected = True
      actual = isCryptSolution(self.example1['crypt'], self.example1['solution'])
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_2(self):
      expected = False
      actual = isCryptSolution(self.example2['crypt'], self.example2['solution'])
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_3(self):
      expected = True
      actual = isCryptSolution(
         ['ONE', 'ONE', 'TWO'], 
         [
            ['O', '2'],
            ['T', '4'],
            ['W', '6'],
            ['E', '1'],
            ['N', '3']
         ])
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_4(self):
      expected = False
      actual = isCryptSolution(
         ['ONE', 'ONE', 'TWO'], 
         [
            ['O', '0'],
            ['T', '1'],
            ['W', '2'],
            ['E', '5'],
            ['N', '6']
         ])
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_5(self):
      expected = True
      actual = isCryptSolution(['A', 'A', 'A'], [['A', '0']])
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_6(self):
      expected = False
      actual = isCryptSolution(
         ['A', 'B', 'C'], 
         [
            ['A', '5'],
            ['B', '6'],
            ['C', '1']
         ])
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_7(self):
      expected = False
      actual = isCryptSolution(['AA', 'AA', 'AA'], [['A', '0']])
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_8(self):
      expected = False
      actual = isCryptSolution(['A', 'A', 'A'], [['A', '1']])
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_9(self):
      expected = True
      actual = isCryptSolution(['AA', 'AA', 'BB'], [['A', '1'], ['B', '2']])
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_10(self):
      expected = False
      actual = isCryptSolution(
         ['BAA', 'CAB', 'DAB'], 
         [
            ['A', '0'],
            ['B', '1'],
            ['C', '2'],
            ['D', '4']
         ])
      self.assertEqual(actual, expected)

if __name__ == '__main__':
   unittest.main()
