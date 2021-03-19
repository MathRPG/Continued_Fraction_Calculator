import math
import sys

import matplotlib as mpl
import matplotlib.pyplot
from PyQt5 import QtWidgets, QtGui
from matplotlib.backends.backend_agg import FigureCanvasAgg

from gui.simple_continued_fraction_calculator_ui import Ui_SimpleContinuedFractionCalculatorForm
from simple_continuous_fraction import simple_continuous_fraction


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.form_depth_spin_box.setMinimum(1)
        self.form_depth_spin_box.setMaximum(40)

        self.form_submit_push_button.clicked.connect(self.submit_form)

        self.show()

    def submit_form(self):
        expression = self.form_expression_line_edit.text()
        depth = self.form_depth_spin_box.value()

        try:
            evaluation = eval(expression, self.EVAL_SYMBOLS)
        except (SyntaxError, NameError):
            self.form_expression_line_edit.setText('')
            QtWidgets.QMessageBox.critical(self, 'Error', 'Invalid Expression')
            return

        latex = None

        try:
            latex = self.get_cf_latex_from_value(evaluation, depth)
        except Exception as e:
            self.form_depth_spin_box.setValue(15)
            QtWidgets.QMessageBox.critical(self, 'Error', 'Calculation Failed')
            print(e)
            return

        pixmap = None

        try:
            pixmap = self.get_pixmap_from_latex(latex, font_size=12)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, 'Error', 'Rendering Failed')
            print(e)
            return

        self.result_render_label.setPixmap(pixmap)
        self.result_render_label.show()

    @staticmethod
    def get_cf_latex_from_value(value, depth):
        return f'${simple_continuous_fraction(value, depth)}$'

    @staticmethod
    def get_pixmap_from_latex(latex, font_size=20):
        fig = mpl.pyplot.figure()
        fig.patch.set_facecolor('none')
        fig.set_canvas(FigureCanvasAgg(fig))
        renderer = fig.canvas.get_renderer()

        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('off')
        # ax.patch.set_facecolor('none')
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

    sys.setrecursionlimit(10000)

    app = QtWidgets.QApplication(sys.argv)

    widget = SimpleContinuedFractionCalculatorWindow()
    # widget.show()

    sys.exit(app.exec_())
