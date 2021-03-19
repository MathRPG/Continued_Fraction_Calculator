import math
import sys

import matplotlib as mpl
import matplotlib.pyplot
from PyQt5 import QtWidgets, QtGui, QtCore
from matplotlib.backends.backend_agg import FigureCanvasAgg

from gui.simple_continued_fraction_calculator_ui import Ui_SimpleContinuedFractionCalculatorForm
from simple_continuous_fraction import get_cf_latex_from_value


class SimpleContinuedFractionCalculatorRequestForm:

    def __init__(self, expression, depth):
        self.expression = expression
        self.depth = depth


class SimpleContinuedFractionCalculatorWindow(QtWidgets.QWidget, Ui_SimpleContinuedFractionCalculatorForm):
    EVAL_SYMBOLS = {
        # VARIABLES
        'pi': math.pi,
        'e': math.e,
        'phi': (1 + math.sqrt(5)) / 2,

        # FUNCTIONS
        'sqrt': math.sqrt,
        'sin': math.sin,
        'cos': math.cos,
    }

    submitted = QtCore.pyqtSignal(SimpleContinuedFractionCalculatorRequestForm)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.form_depth_spin_box.setMinimum(1)
        self.form_depth_spin_box.setMaximum(40)

        self.form_submit_push_button.clicked.connect(self.interpret_form_external)

        self.show()

    def interpret_form_external(self):
        expression = self.form_expression_line_edit.text()
        depth = self.form_depth_spin_box.value()

        evaluation = self.parse_expression(expression)

        if evaluation is None:
            return

        latex = self.get_latex(evaluation, depth)

        if latex is None:
            return

        try:
            pixmap = get_pixmap_from_latex(latex, font_size=12)
        except (Exception, RuntimeError):
            QtWidgets.QMessageBox.critical(self, 'Error', 'Rendering Failed')
            return

        self.result_render_label.setPixmap(pixmap)
        self.result_render_label.show()

    def parse_expression(self, expression):
        try:
            return eval(expression, self.EVAL_SYMBOLS)
        except (SyntaxError, NameError, ValueError):
            self.form_expression_line_edit.clear()
            QtWidgets.QMessageBox.critical(self, 'Error', 'Invalid Expression')
            return None

    def get_latex(self, value, depth):
        try:
            return get_cf_latex_from_value(value, depth)
        except (Exception, RuntimeError):
            QtWidgets.QMessageBox.critical(self, 'Error', 'Calculation Failed')
            return None


# Source: https://stackoverflow.com/questions/32035251/displaying-latex-in-pyqt-pyside-qtablewidget
def get_pixmap_from_latex(latex, font_size=20):
    mpl.pyplot.close('all')  # TODO: This is dumb

    fig = mpl.pyplot.figure()
    fig.patch.set_facecolor('none')
    fig.set_canvas(FigureCanvasAgg(fig))
    renderer = fig.canvas.get_renderer()

    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    t = ax.text(0, 0, latex, ha='left', va='bottom', fontsize=font_size)

    fig_width, fig_height = fig.get_size_inches()
    fig_bbox = fig.get_window_extent(renderer)
    text_bbox = t.get_window_extent(renderer)

    tight_fig_width = text_bbox.width * fig_width / fig_bbox.width
    tight_fig_height = text_bbox.height * fig_height / fig_bbox.height

    fig.set_size_inches(tight_fig_width, tight_fig_height)

    buf, size = fig.canvas.print_to_buffer()

    q_image = QtGui.QImage.rgbSwapped(QtGui.QImage(buf, size[0], size[1], QtGui.QImage.Format_ARGB32))

    q_pixmap = QtGui.QPixmap(q_image)

    return q_pixmap


if __name__ == '__main__':
    sys.setrecursionlimit(5000)  # TODO: What

    app = QtWidgets.QApplication(sys.argv)
    widget = SimpleContinuedFractionCalculatorWindow()
    sys.exit(app.exec_())
