from dataclasses import dataclass


@dataclass
class ContinuedFractionCalculatorRequestForm:
    expression: str
    depth: int
    numerators: iter
