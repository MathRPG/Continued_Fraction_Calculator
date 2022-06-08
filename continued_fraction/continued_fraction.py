import itertools
import math
from enum import Enum
from typing import Iterator


class ContinuedFraction:
    DEFAULT_MAX_DEPTH = 5
    SIMPLE_CF_NUMERATORS = itertools.repeat(1)

    class NotEnoughNumerators(Exception):
        pass

    def __init__(self, value: float,
                 max_depth: int = DEFAULT_MAX_DEPTH,
                 numerators: Iterator[int] = SIMPLE_CF_NUMERATORS):

        self.nums, self.dens = [], []
        self.calc_depth = 0
        self.value = value
        self.is_exact = False

        while True:
            den, frac = ContinuedFraction.split_integer(value)
            self.dens.append(den)

            if math.isclose(frac, 0.0):
                self.is_exact = True
                break

            if self.calc_depth == max_depth:
                self.is_exact = False
                break

            try:
                num = next(numerators)
            except StopIteration:
                raise self.NotEnoughNumerators("Not enough numerators for requested depth")

            self.nums.append(num)

            value = num / frac
            self.calc_depth += 1

        # Since there is an a_0 but not a b_0, we expect one less numerator than denominators
        assert len(self.nums) == len(self.dens) - 1

    @staticmethod
    def split_integer(v: float) -> tuple[int, float]:
        r = round(v)
        if math.isclose(v, r):
            return r, 0.0
        i = math.floor(v)
        return i, v - i

    class LatexStyle(Enum):
        NESTED = 'nested'
        FLAT = 'flat'

    def to_latex(self, style: LatexStyle) -> str:
        match style:
            case self.LatexStyle.NESTED:
                return self._to_latex_nested()
            case self.LatexStyle.FLAT:
                return self._to_latex_flat()

    def _to_latex_nested(self) -> str:
        nums, dens = self.array_copies()
        text = str(dens.pop())

        if not self.is_exact:
            text += r'+\ddots'

        for num, den in zip(reversed(nums), reversed(dens)):
            text = r'%d + \dfrac{%d}{%s}' % (den, num, text)

        return text

    def _to_latex_flat(self) -> str:
        nums, dens = self.array_copies()
        text = str(dens.pop(0))

        for num, den in zip(nums, dens):
            text += r'+\dfrac{\;%d\;|}{|\;%d\;}' % (num, den)

        if not self.is_exact:
            text += r'+\cdots'

        return text

    def array_copies(self):
        return self.nums.copy(), self.dens.copy()


if __name__ == '__main__':
    print(ContinuedFraction(1 + 2 / 3).to_latex(ContinuedFraction.LatexStyle.NESTED))
