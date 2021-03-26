import decimal
import math
import sys
from decimal import Decimal

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from continued_fraction_calculator_form import ContinuedFractionCalculatorForm
from gui.continued_fraction_calculator_window import ContinuedFractionCalculatorWindow
from simple_continuous_fraction import get_simple_continued_fraction_latex_from_value
from utils.latex_utils import latex_to_pixmap


class MainApp(QApplication):
    # TODO: Better errors, extract evaluation step to its own module

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
        self.main_window = ContinuedFractionCalculatorWindow()
        self.main_window.submitted.connect(self.process_form)

    def exec_(self) -> int:
        self.main_window.show()
        return super().exec_()

    @QtCore.pyqtSlot(ContinuedFractionCalculatorForm)
    def process_form(self, form: ContinuedFractionCalculatorForm):
        try:
            result_pixmap = self.form_to_result_pixmap(form)
            self.main_window.display_result_pixmap(result_pixmap)
        except Exception as e:
            self.main_window.process_exception(e)

    def form_to_result_pixmap(self, form):
        value = self.evaluate_expression(form.expression)
        fraction_latex = get_simple_continued_fraction_latex_from_value(value, depth=form.depth)
        return latex_to_pixmap(fraction_latex, font_size=12)

    def evaluate_expression(self, expression):
        return eval(expression, {}, self.EVALUATION_SYMBOL_LIST)


if __name__ == '__main__':
    sys.setrecursionlimit(5000)  # TODO: What
    decimal.getcontext().prec = 100

    app = MainApp(sys.argv)
    sys.exit(app.exec_())
