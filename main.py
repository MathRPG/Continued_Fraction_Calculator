import decimal
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from continued_fraction.continued_fraction import ContinuedFraction
from continued_fraction_calculator_request_form import ContinuedFractionCalculatorRequestForm
from expression_evalutator import ExpressionEvaluator
from gui.continued_fraction_calculator_main_window import ContinuedFractionCalculatorMainWindow
from utils.latex_utils import latex_to_pixmap


class MainApp(QApplication):

    # TODO: Better errors, extract evaluation step to its own module

    def __init__(self, argv):
        super().__init__(argv)
        self.main_window = ContinuedFractionCalculatorMainWindow()
        self.main_window.submitted.connect(self.process_form)

    def exec_(self) -> int:
        self.main_window.show()
        return super().exec_()

    @QtCore.pyqtSlot(ContinuedFractionCalculatorRequestForm)
    def process_form(self, form: ContinuedFractionCalculatorRequestForm):
        try:
            result_pixmap = self.form_to_result_pixmap(form)
            self.main_window.display_result_pixmap(result_pixmap)
        except Exception as e:
            self.main_window.process_exception(e)

    def form_to_result_pixmap(self, form):
        value = ExpressionEvaluator.evaluate_expression(form.expression)
        fraction_latex = ContinuedFraction(value, max_depth=form.depth, numerators=form.numerators).to_latex()
        return latex_to_pixmap(f'${fraction_latex}$', font_size=12)


if __name__ == '__main__':
    sys.setrecursionlimit(5000)  # TODO: What
    decimal.getcontext().prec = 200

    app = MainApp(sys.argv)
    sys.exit(app.exec_())
