import unittest
from bodma.parser import evaluate_expression, validate_expression

class TestParser(unittest.TestCase):
    def test_evaluate_expression(self):
        self.assertEqual(evaluate_expression("2+3*4"), 14)

    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            validate_expression("2+3*a")

if __name__ == '__main__':
    unittest.main()
