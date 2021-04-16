import itertools
from dataclasses import dataclass
from typing import Optional


@dataclass
class CalculatorRequestForm:
    expression: str
    depth: int
    numerator_strings: Optional[tuple[str, str]]
    latex_style: str

    def make_numerator_iterator(self):
        if self.numerator_strings is None:
            return itertools.cycle((1,))
        sequence = self.parse_numerator_list(self.numerator_strings[0])
        cycle = self.parse_numerator_list(self.numerator_strings[1])
        return itertools.chain(sequence, itertools.cycle(cycle))

    @staticmethod
    def parse_numerator_list(text: str):
        return list(map(int, text.split(',')))
