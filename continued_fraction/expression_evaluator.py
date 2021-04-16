from decimal import Decimal


class EvaluationError(Exception):
    pass


class ExpressionEvaluator:
    DEFAULT_TOKEN_DICT = {
        'pi': Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253'),
        'e': Decimal('2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785'),
    }

    def __init__(self, token_dict=None):
        self.token_dict = (token_dict or ExpressionEvaluator.DEFAULT_TOKEN_DICT).copy()

    def eval_(self, expr):
        try:
            return eval(expr, {}, self.token_dict)
        except SyntaxError:
            raise EvaluationError("Invalid Expression Syntax")
        except NameError:
            raise EvaluationError("Unrecognized Tokens in Expression")
