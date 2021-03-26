import math
import unittest

from continued_fraction import ContinuedFraction


class ContinuedFractionTestCase(unittest.TestCase):

    def test_simple_with_integer(self):
        self.assertEqual('0', ContinuedFraction(0).to_latex())
        self.assertEqual('1', ContinuedFraction(1).to_latex())

    def test_simple_with_depth_1(self):
        self.assertEqual(r'1 + \dfrac{1}{2}', ContinuedFraction(1 + 1 / 2).to_latex())
        self.assertEqual(r'2 + \dfrac{1}{3}', ContinuedFraction(2 + 1 / 3).to_latex())

    def test_simple_with_negatives(self):
        self.assertEqual(r'-1 + \dfrac{1}{2}', ContinuedFraction(-1 + 1 / 2).to_latex())
        self.assertEqual(r'0 + \dfrac{1}{2}', ContinuedFraction(1 + 1 / -2).to_latex())
        self.assertEqual(r'-2 + \dfrac{1}{2}', ContinuedFraction(-1 + 1 / -2).to_latex())

    def test_simple_with_depth_2(self):
        self.assertEqual(r'1 + \dfrac{1}{1 + \dfrac{1}{2}}', ContinuedFraction(1 + 1 / (1 + 1 / 2)).to_latex())

    def test_max_depth(self):
        golden_ratio = (math.sqrt(5) + 1) / 2
        self.assertEqual(r'1', ContinuedFraction(golden_ratio, max_depth=0).to_latex())
        self.assertEqual(r'1 + \dfrac{1}{1 + \dfrac{1}{1 + \dfrac{1}{1}}}',
                         ContinuedFraction(golden_ratio, max_depth=3).to_latex())

    def test_custom_numerators(self):
        self.assertEqual(r'1 + \dfrac{2}{3}',
                         ContinuedFraction(1 + 2 / 3, numerators=iter([2])).to_latex())


if __name__ == '__main__':
    unittest.main()
