import math
import sys

from PyQt5 import QtWidgets

from gui.simple_continued_fraction_calculator_window import SimpleContinuedFractionCalculatorWindow
from simple_continuous_fraction import get_simple_continued_fraction_latex_from_value
from utils.pixmap_from_latex import get_pixmap_from_latex


class MainApp(QtWidgets.QApplication):
    """Docstring"""  # TODO: MainApp Docstring

    EVALUATION_SYMBOL_LIST = {
        'pi': math.pi,
        'e': math.e,
        'phi': (1 + math.sqrt(5)) / 2,
        'sqrt': math.sqrt,
        'sin': math.sin,
        'cos': math.cos,
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
        expression_evaluated = eval(expression, {}, self.EVALUATION_SYMBOL_LIST)
        fraction_latex = get_simple_continued_fraction_latex_from_value(expression_evaluated, depth=depth)
        return get_pixmap_from_latex(fraction_latex)


if __name__ == '__main__':
    sys.setrecursionlimit(5000)  # TODO: What

    app = MainApp(sys.argv)
    sys.exit(app.exec_())
