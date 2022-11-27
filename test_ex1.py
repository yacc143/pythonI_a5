import unittest
import ex1

class TestEx1(unittest.TestCase):
    def test_fib_result_0(self):
        self.assertEqual(ex1.fib(0), 0)

    def test_fib_result_1(self):
        self.assertEqual(ex1.fib(1), 1)

    def test_fib_result_2(self):
        self.assertEqual(ex1.fib(2), 1)

    def test_fib_result_3(self):
        self.assertEqual(ex1.fib(3), 2)

    def test_fib_result_7(self):
        self.assertEqual(ex1.fib(7), 13)

    def test_fib_result_minus_2(self):
        self.assertEqual(ex1.fib(-2), -1)

if __name__ == '__main__':
    unittest.main()