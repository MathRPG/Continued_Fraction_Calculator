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
        # TODO: One box can be empty at a time, but not both
        numerator_sequence = map(int, self.custom_numerator_expression[0].split(','))
        numerator_cycle = map(int, self.custom_numerator_expression[1].split(','))
        return itertools.chain(numerator_sequence, itertools.cycle(numerator_cycle))
