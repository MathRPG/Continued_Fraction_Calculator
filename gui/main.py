import sys

import matplotlib as mpl
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets as qtw, QtGui
from matplotlib.backends.backend_agg import FigureCanvasAgg

from gui.simple_continued_fraction_calculator_ui import Ui_SimpleContinuedFractionCalculatorForm
from test import Ui_main_window
from simple_continuous_fraction import simple_continuous_fraction

class SimpleContinuedFractionCalculatorWindow(qtw.QWidget, Ui_SimpleContinuedFractionCalculatorForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)


    pass

class MainWindowUI(Ui_main_window):

    def setupUi(self, window):
        super(MainWindowUI, self).setupUi(window)
        self.push_button.pressed.connect(self.on_button_click)

    def on_button_click(self):
        expression = self.line_edit.text()
        depth = self.spin_box.value()

        evaluation = eval(expression)

        # DEBUG
        print('Expression: ', expression)
        print('Depth : ', depth)
        print('Eval: ', evaluation)

        frac_latex = '$' + simple_continuous_fraction(evaluation, depth) + '$'
        print(frac_latex)

        self.image.setPixmap(mathTex_to_QPixmap(frac_latex, 14))
        self.image.show()


# Source: https://stackoverflow.com/questions/32035251/displaying-latex-in-pyqt-pyside-qtablewidget
def mathTex_to_QPixmap(mathTex, font_size):
    # ---- set up a mpl figure instance ----

    fig = mpl.pyplot.Figure()
    fig.patch.set_facecolor('none')
    fig.set_canvas(FigureCanvasAgg(fig))
    renderer = fig.canvas.get_renderer()

    # ---- plot the mathTex expression ----

    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    ax.patch.set_facecolor('none')
    t = ax.text(0, 0, mathTex, ha='left', va='bottom', fontsize=font_size)

    # ---- fit figure size to text artist ----

    fwidth, fheight = fig.get_size_inches()
    fig_bbox = fig.get_window_extent(renderer)

    text_bbox = t.get_window_extent(renderer)

    tight_fwidth = text_bbox.width * fwidth / fig_bbox.width
    tight_fheight = text_bbox.height * fheight / fig_bbox.height

    fig.set_size_inches(tight_fwidth, tight_fheight)

    # ---- convert mpl figure to QPixmap ----

    buf, size = fig.canvas.print_to_buffer()
    qimage = QtGui.QImage.rgbSwapped(QtGui.QImage(buf, size[0], size[1],
                                                  QtGui.QImage.Format_ARGB32))
    qpixmap = QtGui.QPixmap(qimage)

    return qpixmap


if __name__ == '__main__':

    app = qtw.QApplication([])

    widget = SimpleContinuedFractionCalculatorWindow()
    widget.show()

    sys.exit(app.exec_())


    # print('hey')
    # app = qtw.QApplication(sys.argv)
    # print('hey')
    #
    # main_window = qtw.QMainWindow()
    # print('hey')
    #
    # ui = MainWindowUI()
    # print('hey')
    #
    # ui.setupUi(main_window)
    # print('hey')
    #
    # main_window.show()
    # print('hey')
    #
    # sys.exit(app.exec_())
