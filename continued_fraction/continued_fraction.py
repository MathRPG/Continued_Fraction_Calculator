import math
from itertools import repeat


class ContinuedFraction:
    # TODO: Requires more testing

    def __init__(self, value: float, max_depth: int = 5, numerators=repeat(1)):
        self._as, self._bs = self.convert_value_to_continued_fraction_as_array(value, max_depth, numerators)

    @staticmethod
    def convert_value_to_continued_fraction_as_array(value, max_depth, numerators):
        _as = []
        _bs = []
        current_depth = 0
        while True:
            a, frac = ContinuedFraction.split_integer(value)
            _as.append(a)
            if math.isclose(frac, 0) or current_depth == max_depth:
                break
            b = next(numerators)
            value = b / frac
            _bs.append(b)
            current_depth += 1
        return _as, _bs

    @staticmethod
    def split_integer(value):
        rounded = round(value)
        if math.isclose(value, rounded):
            return rounded, 0

        integer_part = math.floor(value)
        return integer_part, value - integer_part

    def to_latex(self) -> str:
        latex = str(self._as[-1])

        for a, b in zip(self._as[-2::-1], self._bs[::-1]):
            latex = r'%d + \dfrac{%d}{%s}' % (a, b, latex)

        return latex


if __name__ == '__main__':
    print(ContinuedFraction(1 + 2 / 3).to_latex())
