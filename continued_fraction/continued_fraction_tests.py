import math
import unittest


class ContinuedFraction:

    def __init__(self, value: float, max_depth: int = 5):
        self._as = self.convert_value_to_denominator_array(value, max_depth)

    @staticmethod
    def convert_value_to_denominator_array(value, max_depth):
        array = []
        while max_depth >= 0:
            a, frac = ContinuedFraction.split_integer(value)
            array.append(a)
            if math.isclose(frac, 0):
                break
            value = 1 / frac
            max_depth -= 1
        return array

    @staticmethod
    def split_integer(value):
        rounded = round(value)
        if math.isclose(value, rounded):
            return rounded, 0

        integer_part = math.floor(value)
        return integer_part, value - integer_part

    def to_latex(self) -> str:
        latex = str(self._as[-1])

        for a in self._as[-2::-1]:
            latex = r'%d + \dfrac{1}{%s}' % (a, latex)

        return f'${latex}$'


class ContinuedFractionTestCase(unittest.TestCase):

    def test_integer_returns_integer(self):
        self.assertEqual('0', ContinuedFraction(0).to_latex())
        self.assertEqual('1', ContinuedFraction(1).to_latex())

    def test_depth_1(self):
        self.assertEqual(r'1 + \dfrac{1}{2}', ContinuedFraction(1 + 1 / 2).to_latex())
        self.assertEqual(r'2 + \dfrac{1}{3}', ContinuedFraction(2 + 1 / 3).to_latex())

    def test_negatives(self):
        self.assertEqual(r'-1 + \dfrac{1}{2}', ContinuedFraction(-1 + 1 / 2).to_latex())
        self.assertEqual(r'0 + \dfrac{1}{2}', ContinuedFraction(1 + 1 / -2).to_latex())
        self.assertEqual(r'-2 + \dfrac{1}{2}', ContinuedFraction(-1 + 1 / -2).to_latex())

    def test_depth_2(self):
        self.assertEqual(r'1 + \dfrac{1}{1 + \dfrac{1}{2}}', ContinuedFraction(1 + 1 / (1 + 1 / 2)).to_latex())

    def test_max_depth(self):
        golden_ratio = (math.sqrt(5) + 1) / 2
        self.assertEqual(r'1', ContinuedFraction(golden_ratio, max_depth=0).to_latex())
        self.assertEqual(r'1 + \dfrac{1}{1 + \dfrac{1}{1 + \dfrac{1}{1}}}',
                         ContinuedFraction(golden_ratio, max_depth=3).to_latex())


if __name__ == '__main__':
    unittest.main()
