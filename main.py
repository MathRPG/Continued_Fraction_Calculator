import decimal
import math
import sys
from decimal import Decimal

from PyQt5.QtWidgets import QApplication

from gui.simple_continued_fraction_calculator_window import SimpleContinuedFractionCalculatorWindow
from simple_continuous_fraction import get_simple_continued_fraction_latex_from_value
from utils.latex_utils import latex_to_pixmap


class MainApp(QApplication):
    """Docstring"""  # TODO: MainApp Docstring

    EVALUATION_SYMBOL_LIST = {
        'pi': Decimal(
            '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'),
        'e': Decimal(
            '2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274'),
        'phi': (1 + math.sqrt(5)) / 2,
        'sqrt': math.sqrt,
        'sin': math.sin,
        'cos': math.cos,
        'Decimal': Decimal,
    }

    def __init__(self, argv):
        super().__init__(argv)
        self.main_widget = SimpleContinuedFractionCalculatorWindow()
        self.main_widget.submitted.connect(self.process_form_inputs)

    def exec_(self) -> int:
        self.main_widget.show()
        return super().exec_()

    def process_form_inputs(self, expression, depth):
        try:
            pixmap = self.get_fraction_pixmap_from_expression_with_depth(expression, depth)
            self.main_widget.display_result_pixmap(pixmap)
        except Exception as e:
            self.main_widget.process_exception(e)

    def get_fraction_pixmap_from_expression_with_depth(self, expression, depth):
        value = self.evaluate_expression(expression)
        fraction_latex = get_simple_continued_fraction_latex_from_value(value, depth=depth)
        return latex_to_pixmap(fraction_latex, font_size=12)

    def evaluate_expression(self, expression):
        # TODO: Better error names/strings
        try:
            return eval(expression, {}, self.EVALUATION_SYMBOL_LIST)
        except NameError:
            raise NameError("Unrecognized Names")
        except SyntaxError:
            raise SyntaxError("Invalid Syntax")
        except Exception as e:
            raise e


if __name__ == '__main__':
    sys.setrecursionlimit(5000)  # TODO: What
    decimal.getcontext().prec = 100

    app = MainApp(sys.argv)
    sys.exit(app.exec_())
