import math
import sys

import matplotlib as mpl
import matplotlib.pyplot
from PyQt5 import QtWidgets, QtGui, QtCore
from matplotlib.backends.backend_agg import FigureCanvasAgg

from gui.simple_continued_fraction_calculator_ui import Ui_SimpleContinuedFractionCalculatorForm
from simple_continuous_fraction import get_cf_latex_from_value


class RefactoredMainApp(QtWidgets.QApplication):
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
        self.main_widget = RefactoredSimpleContinuedFractionCalculatorWindow()
        self.main_widget.submitted.connect(self.process_form_inputs)

    def exec_(self) -> int:
        self.main_widget.show()
        return super().exec_()

    def process_form_inputs(self, expression, depth):
        try:
            pixmap = self.get_fraction_pixmap_from_expression_with_depth(expression, depth)
            self.main_widget.display_fraction(pixmap)
        except Exception as e:
            self.main_widget.process_exception(e)

    def get_fraction_pixmap_from_expression_with_depth(self, expression, depth):
        expression_evaluated = eval(expression, {}, self.EVALUATION_SYMBOL_LIST)
        fraction_latex = get_cf_latex_from_value(expression_evaluated, depth=depth)
        return get_pixmap_from_latex(fraction_latex)


class RefactoredSimpleContinuedFractionCalculatorWindow(QtWidgets.QWidget, Ui_SimpleContinuedFractionCalculatorForm):
    submitted = QtCore.pyqtSignal(str, int)

    DEFAULT_DEPTH_SPIN_BOX_MINIMUM = 1
    DEFAULT_DEPTH_SPIN_BOX_MAXIMUM = 40

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.set_spin_box_bounds(self.DEFAULT_DEPTH_SPIN_BOX_MINIMUM, self.DEFAULT_DEPTH_SPIN_BOX_MAXIMUM)

        self.form_expression_line_edit.returnPressed.connect(self.submit_input)
        self.form_submit_push_button.clicked.connect(self.submit_input)

    def set_spin_box_bounds(self, minimum, maximum):
        self.form_depth_spin_box.setMinimum(minimum)
        self.form_depth_spin_box.setMaximum(maximum)

    def submit_input(self):
        expression = self.form_expression_line_edit.text()
        depth = self.form_depth_spin_box.value()
        self.submitted.emit(expression, depth)

    @QtCore.pyqtSlot(QtGui.QPixmap)
    def display_fraction(self, pixmap):
        self.result_render_label.setPixmap(pixmap)
        self.result_render_label.show()

    @QtCore.pyqtSlot(Exception)
    def process_exception(self, exception):
        QtWidgets.QMessageBox.critical(self, str(type(exception)), str(exception))


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

    app = RefactoredMainApp(sys.argv)
    sys.exit(app.exec_())

# Alternative latex rendering:
# https://gist.github.com/gmarull/dcc8218385014559c1ca46047457c364
# import sys
# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtSvg import QSvgWidget
#
# from io import BytesIO
# import matplotlib.pyplot as plt
#
#
# # matplotlib: force computer modern font set
# plt.rc('mathtext', fontset='cm')
#
#
# def tex2svg(formula, fontsize=12, dpi=300):
#     """Render TeX formula to SVG.
#     Args:
#         formula (str): TeX formula.
#         fontsize (int, optional): Font size.
#         dpi (int, optional): DPI.
#     Returns:
#         str: SVG render.
#     """
#
#     fig = plt.figure(figsize=(0.01, 0.01))
#     fig.text(0, 0, r'${}$'.format(formula), fontsize=fontsize)
#
#     output = BytesIO()
#     fig.savefig(output, dpi=dpi, transparent=True, format='svg',
#                 bbox_inches='tight', pad_inches=0.0, frameon=False)
#     plt.close(fig)
#
#     output.seek(0)
#     return output.read()
#
#
# def main():
#     FORMULA = r'\int_{-\infty}^\infty e^{-x^2}\,dx = \sqrt{\pi}'
#
#     app = QApplication(sys.argv)
#
#     svg = QSvgWidget()
#     svg.load(tex2svg(FORMULA))
#     svg.show()
#
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()
