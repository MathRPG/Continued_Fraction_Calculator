import math
from itertools import repeat


class ContinuedFraction:

    def __init__(self, value: float, max_depth: int = 5, numerators=repeat(1)):
        self.av, self.bv = self.convert_value_to_continued_fraction_as_array(value, max_depth, numerators)

    @staticmethod
    def convert_value_to_continued_fraction_as_array(value, max_depth, numerators):
        av = []
        bv = []
        current_depth = 0
        while True:
            a, frac = ContinuedFraction.split_integer(value)
            av.append(a)
            if math.isclose(frac, 0) or current_depth == max_depth:
                break
            b = next(numerators)
            value = b / frac
            bv.append(b)
            current_depth += 1
        return av, bv

    @staticmethod
    def split_integer(value):
        rounded = round(value)
        if math.isclose(value, rounded):
            return rounded, 0

        integer_part = math.floor(value)
        return integer_part, value - integer_part

    def to_latex(self) -> str:
        ai, bi = reversed(self.av), reversed(self.bv)

        latex = str(next(ai))

        for a, b in zip(ai, bi):
            latex = r'%d + \dfrac{%d}{%s}' % (a, b, latex)

        return latex


if __name__ == '__main__':
    print(ContinuedFraction(1 + 2 / 3).to_latex())
