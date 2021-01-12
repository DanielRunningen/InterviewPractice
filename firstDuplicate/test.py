import unittest
import timeout_decorator
from solution import firstDuplicate

EXECUTION_TIME_LIMIT = 4

# All tests in this class come directly from CodeSignal
class CodeSignalTests(unittest.TestCase):
    def setUp(self):
        self.example1 = [2, 1, 3, 5, 3, 2]
        self.example2 = [2, 2]
        self.example3 = [2, 4, 3, 5, 1]

    @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
    def test_1(self):
        expected = 3
        actual = firstDuplicate(self.example1)
        self.assertEqual(actual, expected)

    @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
    def test_2(self):
        expected = 2
        actual = firstDuplicate(self.example2)
        self.assertEqual(actual, expected)

    @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
    def test_3(self):
        expected = -1
        actual = firstDuplicate(self.example3)
        self.assertEqual(actual, expected)

    @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
    def test_4(self):
        expected = -1
        actual = firstDuplicate([1])
        self.assertEqual(actual, expected)

    @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
    def test_5(self):
        expected = 5
        actual = firstDuplicate([5, 5, 5, 5, 5])
        self.assertEqual(actual, expected)

    @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
    def test_6(self):
        expected = -1
        actual = firstDuplicate([2, 1])
        self.assertEqual(actual, expected)

    @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
    def test_7(self):
        expected = -1
        actual = firstDuplicate([2, 1, 3])
        self.assertEqual(actual, expected)

    @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
    def test_8(self):
        expected = 3
        actual = firstDuplicate([2, 3, 3])
        self.assertEqual(actual, expected)

    @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
    def test_9(self):
        expected = 3
        actual = firstDuplicate([3, 3, 3])
        self.assertEqual(actual, expected)

    @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
    def test_10(self):
        expected = 6
        actual = firstDuplicate([8, 4, 6, 2, 6, 4, 7, 9, 5, 8])
        self.assertEqual(actual, expected)

    @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
    def test_11(self):
        expected = -1
        actual = firstDuplicate([10, 6, 8, 4, 9, 1, 7, 2, 5, 3])
        self.assertEqual(actual, expected)

    @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
    def test_12(self):
        expected = 1
        actual = firstDuplicate([1, 1, 2, 2, 1])
        self.assertEqual(actual, expected)

    @timeout_decorator.timeout(EXECUTION_TIME_LIMIT)
    def test_emptyList(self):
        expected = -1
        actual = firstDuplicate([])
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
