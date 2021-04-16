import math
from enum import Enum


class LatexStyle(Enum):
    LEGACY = 'legacy'
    MODERN = 'modern'


class NotEnoughNumerators(Exception):
    pass


class ContinuedFraction:

    def __init__(self, value: float, max_depth: int, numerators):
        as_ = []
        bs_ = []
        current_depth = 0
        self.value = value

        while True:
            a, frac = ContinuedFraction.split_float(value)
            as_.append(a)

            if math.isclose(frac, 0):
                self.is_approximation = False
                break

            if current_depth == max_depth:
                self.is_approximation = True
                break

            try:
                b = next(numerators)
            except StopIteration:
                raise NotEnoughNumerators("Not enough numerators to accommodate requested depth")

            bs_.append(b)

            value = b / frac
            current_depth += 1

        self.as_ = as_
        self.bs_ = bs_
        self.depth_reached = current_depth

    @staticmethod
    def split_float(v) -> tuple[int, float]:
        r = round(v)
        if math.isclose(v, r):
            return r, 0.0
        i = math.floor(v)
        return i, v - i

    def array_copies(self):
        as_ = self.as_.copy()
        bs_ = self.bs_.copy()
        return as_, bs_

    def to_latex(self, latex_style: LatexStyle) -> str:
        style_to_method = {
            LatexStyle.LEGACY: self.to_latex_legacy,
            LatexStyle.MODERN: self.to_latex_modern,
        }
        return style_to_method[latex_style]()

    def to_latex_legacy(self):
        as_, bs_ = self.array_copies()
        text = str(as_.pop())

        if self.is_approximation:
            text += r'+\ddots'

        for a, b in zip(reversed(as_), reversed(bs_)):
            text = r'%d + \dfrac{%d}{%s}' % (a, b, text)

        return text

    def to_latex_modern(self):
        as_, bs_ = self.array_copies()
        text = str(as_.pop(0))

        for a, b in zip(as_, bs_):
            text += r'+\dfrac{\;%d\;|}{|\;%d\;}' % (b, a)

        if self.is_approximation:
            text += r'+\cdots'

        return text
