import unittest
import timeout_decorator
from solution import firstNotRepeatingCharacter

EXECUTION_TIME_LIMIT = 4

class CodeSignalTests(unittest.TestCase):
   def setUp(self):
      self.example1 = "abacabad"
      self.example2 = "abacabaabacaba"

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_1(self):
      expected = 'c'
      actual = firstNotRepeatingCharacter(self.example1)
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_2(self):
      expected = '_'
      actual = firstNotRepeatingCharacter(self.example2)
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_3(self):
      expected = 'z'
      actual = firstNotRepeatingCharacter("z")
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_4(self):
      expected = 'c'
      actual = firstNotRepeatingCharacter("bcb")
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_5(self):
      expected = '_'
      actual = firstNotRepeatingCharacter("bcccccccb")
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_6(self):
      expected = 'd'
      actual = firstNotRepeatingCharacter("abcdefghijklmnopqrstuvwxyziflskecznslkjfabe")
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_7(self):
      expected = '_'
      actual = firstNotRepeatingCharacter("zzz")
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_8(self):
      expected = 'y'
      actual = firstNotRepeatingCharacter("bcccccccccccccyb")
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_9(self):
      expected = 'd'
      actual = firstNotRepeatingCharacter("xdnxxlvupzuwgigeqjggosgljuhliybkjpibyatofcjbfxwtalc")
      self.assertEqual(actual, expected)

   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_10(self):
      expected = 'g'
      actual = firstNotRepeatingCharacter("ngrhhqbhnsipkcoqjyviikvxbxyphsnjpdxkhtadltsuxbfbrkof")
      self.assertEqual(actual, expected)

class CustomTests(unittest.TestCase):
   @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
   def test_emptyString(self):
      expected = '_'
      actual = firstNotRepeatingCharacter("")
      self.assertEqual(actual, expected)

if __name__ == '__main__':
   unittest.main()
