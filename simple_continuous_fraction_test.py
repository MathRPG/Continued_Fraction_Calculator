import math
import unittest


def split_integer_and_decimal_parts(value):
    return math.floor(value), value - math.floor(value)


def simple_continuous_fraction(value):
    integer, decimal = split_integer_and_decimal_parts(value)
    if math.isclose(decimal, 0.0):
        return str(integer)
    else:
        denominator = round(1 / decimal)
        return '%d + \\frac{1}{%d}' % (integer, denominator)


class SimpleContinuousFractionTestCase(unittest.TestCase):

    def test_integer_returns_integer(self):
        self.assertEqual('0', simple_continuous_fraction(0))
        self.assertEqual('1', simple_continuous_fraction(1))

    def test_depth_1(self):
        self.assertEqual('1 + \\frac{1}{2}', simple_continuous_fraction(1 + 1 / 2))
        self.assertEqual('2 + \\frac{1}{3}', simple_continuous_fraction(2 + 1 / 3))

    def test_depth_1_negatives(self):
        self.assertEqual('-1 + \\frac{1}{2}', simple_continuous_fraction(-1 + 1 / 2))
        self.assertEqual('0 + \\frac{1}{2}', simple_continuous_fraction(1 + 1 / -2))
        self.assertEqual('-2 + \\frac{1}{2}', simple_continuous_fraction(-1 + 1 / -2))

    # def test_depth_2(self):
    #     self.assertEqual('1 + \\dfrac{1}{1 + \\dfrac{1}{2}}', simple_continuous_fraction(1 + 1 / (1 + 1/2)))


if __name__ == '__main__':
    unittest.main()
