import itertools
from dataclasses import dataclass
from typing import Optional


@dataclass
class ContinuedFractionCalculatorRequestForm:
    expression: str
    depth: int
    custom_numerator_expression: Optional[tuple[str, str]]
    latex_style: str

    def make_numerator_iterator(self):
        if self.custom_numerator_expression is None:  # Simple continued fraction
            return itertools.cycle({1})
        numerator_sequence = self.parse_numerators_from_comma_separated_values(self.custom_numerator_expression[0])
        numerator_cycle = self.parse_numerators_from_comma_separated_values(self.custom_numerator_expression[1])
        return itertools.chain(numerator_sequence, itertools.cycle(numerator_cycle))

    @staticmethod
    def parse_numerators_from_comma_separated_values(text: str):
        return text and eval(f'[{text}]') or []
