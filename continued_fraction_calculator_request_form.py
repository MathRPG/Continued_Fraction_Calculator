import itertools
from dataclasses import dataclass
from typing import Optional


@dataclass
class ContinuedFractionCalculatorRequestForm:
    expression: str
    depth: int
    custom_numerator_expression: Optional[tuple[str, str]]

    # TODO: Maybe this is not the best place to put this
    # For instance, you might want to customize the evaluation process form int to a custom evaluator
    # Currently it is very difficult to achieve this, you have to subclass this Form and reimplement the method
    # If the need comes up I will try my best to refactor it, but the architecture is getting messy ngl
    def make_numerator_iterator(self):
        if self.custom_numerator_expression is None:  # Simple continued fraction
            return itertools.cycle({1})
        numerator_sequence = self.parse_numerators_from_comma_separated_values(self.custom_numerator_expression[0])
        numerator_cycle = self.parse_numerators_from_comma_separated_values(self.custom_numerator_expression[1])
        return itertools.chain(numerator_sequence, itertools.cycle(numerator_cycle))

    @staticmethod
    def parse_numerators_from_comma_separated_values(text: str):
        return text and list(map(int, text.split(','))) or []
