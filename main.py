import sys

from PyQt5 import QtWidgets, QtCore

from continued_fraction.calculator_request_form import CalculatorRequestForm
from continued_fraction.continued_fraction import ContinuedFraction, LatexStyle
from continued_fraction.expression_evaluator import ExpressionEvaluator
from gui.main_window import MainWindow


class LatexRenderingError(Exception):
    pass


class MainApp(QtWidgets.QApplication):

    def __init__(self, argv):
        super().__init__(argv)
        self.main_window = MainWindow()
        self.expression_evaluator = ExpressionEvaluator()
        self.main_window.submitted.connect(self.process_form)

    def exec_(self) -> int:
        self.main_window.show()
        return super().exec_()

    @QtCore.pyqtSlot(CalculatorRequestForm)
    def process_form(self, form: CalculatorRequestForm):
        try:
            # TODO - Abstract this
            value = self.expression_evaluator.eval_(form.expression)
            numerators = form.make_numerator_iterator()
            cf = ContinuedFraction(value, form.depth, numerators)
            latex = cf.to_latex(LatexStyle(form.latex_style))
            self.main_window.display_result_latex(latex)
        except RecursionError:
            self.main_window.process_exception(LatexRenderingError(
                "Recursion depth too large for latex rendering engine\n"
                "Use modern latex rendering (inline) or decrease requested depth"))
        except Exception as e:
            self.main_window.process_exception(e)


if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec_())

    # TODO - Errors to implement
    # Not enough numerators for requested depth
