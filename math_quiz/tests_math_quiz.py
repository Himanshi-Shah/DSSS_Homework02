import unittest
from math_quiz import rand_int_generator, operator_generator, perform_operation


class TestMathGame(unittest.TestCase):

    def test_rand_int_generator(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = rand_int_generator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_operator_generator(self):
        # TODO
        valid_operators = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random values
            operator = operator_generator()
            self.assertIn(operator, valid_operators)

    def test_perform_operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                ''' TODO add more test cases here '''
                (9, 5, '-', '9 - 5', 4),
                (3, 6, '*', '3 + 6', 18),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                answer = perform_operation(num1, num2, operator)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
