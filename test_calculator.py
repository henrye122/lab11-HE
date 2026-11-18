# GitHub URL: https://github.com/henrye122/lab11-HE.git
# Partner 1: Henry Edinger

"""Tests for both Lab 11 partners. Run: python -m unittest -v test_calculator

All ten required test names are preserved, with an additional test for exp.
"""

import unittest

import calculator


class TestCalculator(unittest.TestCase):
    # Partner 1 responsibilities

    def test_multiply(self):
        cases = [
            (3, 4, 12),
            (-3, 4, -12),
            (-3, -4, 12),
            (0, 7, 0),
            (1.5, 2.4, 3.6),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertAlmostEqual(calculator.mul(a, b), expected)

    def test_divide(self):
        # The lab requires b / a, so the first argument is the divisor.
        cases = [
            (2, 10, 5),
            (4, 2, 0.5),
            (3, 1, 1 / 3),
            (-2, 10, -5),
            (2, -10, -5),
            (-2, -10, 5),
            (5, 0, 0),
            (0.5, 1.5, 3),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertAlmostEqual(calculator.div(a, b), expected)

    def test_log_invalid_argument(self):
        for base in (2, 10, 0.5):
            for argument in (0, -1, -10.5):
                with self.subTest(base=base, argument=argument):
                    with self.assertRaises(ValueError):
                        calculator.logarithm(base, argument)

    def test_hypotenuse(self):
        cases = [
            (3, 4, 5),
            (-3, 4, 5),
            (3, -4, 5),
            (-3, -4, 5),
            (0, 0, 0),
            (0, -5, 5),
            (1.5, 2, 2.5),
            (1, 1, 1.4142135623730951),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertAlmostEqual(calculator.hypotenuse(a, b), expected)
        for a, b in (("3", 4), (3, None)):
            with self.subTest(a=a, b=b):
                with self.assertRaises(TypeError):
                    calculator.hypotenuse(a, b)

    def test_sqrt(self):
        for value, expected in ((0, 0), (9, 3), (0.25, 0.5), (2, 1.4142135623730951)):
            with self.subTest(value=value):
                self.assertAlmostEqual(calculator.square_root(value), expected)
        for value in (-1, -0.25):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    calculator.square_root(value)
        for value in ("9", None):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    calculator.square_root(value)

    # Partner 2 responsibilities

    def test_add(self):
        cases = [(2, 3, 5), (-2, 3, 1), (-2, -3, -5), (0, 7, 7), (0.1, 0.2, 0.3)]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertAlmostEqual(calculator.add(a, b), expected)

    def test_subtract(self):
        cases = [(7, 3, 4), (3, 7, -4), (-2, -3, 1), (0, 0, 0), (0.3, 0.1, 0.2)]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertAlmostEqual(calculator.subtract(a, b), expected)

    def test_divide_by_zero(self):
        for divisor in (0, 0.0, -0.0):
            for numerator in (0, 5, -5):
                with self.subTest(divisor=divisor, numerator=numerator):
                    with self.assertRaises(ZeroDivisionError):
                        calculator.div(divisor, numerator)

    def test_logarithm(self):
        cases = [
            (2, 8, 3),
            (10, 100, 2),
            (3, 1, 0),
            (2, 2, 1),
            (2, 0.5, -1),
            (0.5, 8, -3),
            (4, 2, 0.5),
        ]
        for base, argument, expected in cases:
            with self.subTest(base=base, argument=argument):
                self.assertAlmostEqual(calculator.logarithm(base, argument), expected)

    def test_log_invalid_base(self):
        for base in (0, -2, 1, 1.0):
            with self.subTest(base=base):
                with self.assertRaises(ValueError):
                    calculator.logarithm(base, 8)

    # Additional coverage for the remaining function in the final merged file.

    def test_exp(self):
        cases = [
            (2, 3, 8),
            (5, 0, 1),
            (0, 3, 0),
            (-2, 3, -8),
            (-2, 4, 16),
            (2, -3, 0.125),
            (9, 0.5, 3),
            (0.5, 2, 0.25),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertAlmostEqual(calculator.exp(a, b), expected)

# Do not touch this
if __name__ == "__main__":
    unittest.main()