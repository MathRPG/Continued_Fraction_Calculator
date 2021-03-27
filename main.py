import decimal
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from continued_fraction.continued_fraction import ContinuedFraction
from continued_fraction_calculator_request_form import ContinuedFractionCalculatorRequestForm
from expression_evalutator import ExpressionEvaluator
from gui.continued_fraction_calculator_main_window import ContinuedFractionCalculatorMainWindow
from gui.symbol_configuration_window import SymbolConfigurationWindow
from utils.latex_utils import latex_to_pixmap


class MainApp(QApplication):

    # TODO: Better errors, extract evaluation step to its own module

    def __init__(self, argv):
        super().__init__(argv)
        self.main_window = ContinuedFractionCalculatorMainWindow()
        self.main_window.submitted.connect(self.process_form)
        self.expression_evaluator = ExpressionEvaluator()
        self.symbol_window = SymbolConfigurationWindow()
        self.symbol_window.display_symbol_dict(self.expression_evaluator.symbol_dict)

    def exec_(self) -> int:
        self.main_window.show()
        self.symbol_window.show()
        return super().exec_()

    @QtCore.pyqtSlot(ContinuedFractionCalculatorRequestForm)
    def process_form(self, form: ContinuedFractionCalculatorRequestForm):
        try:
            value = self.expression_evaluator.eval_(form.expression)
            numerators = form.make_numerator_iterator()
            fraction_latex = ContinuedFraction(value, max_depth=form.depth, numerators=numerators).to_latex()
            result_pixmap = latex_to_pixmap(f'${fraction_latex}$', font_size=12)
            self.main_window.display_result_pixmap(result_pixmap)
        except Exception as e:
            self.main_window.process_exception(e)


if __name__ == '__main__':
    sys.setrecursionlimit(5000)  # TODO: What
    decimal.getcontext().prec = 200

    app = MainApp(sys.argv)
    sys.exit(app.exec_())
