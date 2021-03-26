import math
import unittest

from simple_continued_fraction import simple_continued_fraction


class SimpleContinuedFractionTestCase(unittest.TestCase):

    def test_integer_returns_integer(self):
        self.assertEqual('0', simple_continued_fraction(0))
        self.assertEqual('1', simple_continued_fraction(1))

    def test_depth_1(self):
        self.assertEqual('1 + \\frac{1}{2}', simple_continued_fraction(1 + 1 / 2))
        self.assertEqual('2 + \\frac{1}{3}', simple_continued_fraction(2 + 1 / 3))

    def test_depth_1_negatives(self):
        self.assertEqual('-1 + \\frac{1}{2}', simple_continued_fraction(-1 + 1 / 2))
        self.assertEqual('0 + \\frac{1}{2}', simple_continued_fraction(1 + 1 / -2))
        self.assertEqual('-2 + \\frac{1}{2}', simple_continued_fraction(-1 + 1 / -2))

    def test_depth_2(self):
        self.assertEqual('1 + \\frac{1}{1 + \\frac{1}{2}}', simple_continued_fraction(1 + 1 / (1 + 1 / 2)))

    def test_limit_depth(self):
        golden_ratio = (math.sqrt(5) + 1) / 2
        self.assertEqual('1 + \\frac{1}{1 + \\frac{1}{1 + \\frac{1}{1}}}',
                         simple_continued_fraction(golden_ratio, depth=4))


if __name__ == '__main__':
    unittest.main()
