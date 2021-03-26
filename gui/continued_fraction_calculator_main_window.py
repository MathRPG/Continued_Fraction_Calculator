from itertools import chain, cycle, repeat

from PyQt5 import QtWidgets, QtCore, QtGui

from continued_fraction_calculator_request_form import ContinuedFractionCalculatorRequestForm
from gui.ui_continued_fraction_calculator_main_window import Ui_ContinuedFractionCalculatorMainWindow


class ContinuedFractionCalculatorMainWindow(QtWidgets.QWidget, Ui_ContinuedFractionCalculatorMainWindow):
    submitted = QtCore.pyqtSignal(ContinuedFractionCalculatorRequestForm)

    DEPTH_DEFAULT_MIN = 0
    DEPTH_DEFAULT_MAX = 40

    def __init__(self, depth_min=DEPTH_DEFAULT_MIN, depth_max=DEPTH_DEFAULT_MAX, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.set_depth_range(depth_min, depth_max)

        self.calculate_push_button.clicked.connect(self.submit_input)

    def set_depth_range(self, min_, max_):
        self.depth_slider.setRange(min_, max_)
        self.depth_spin_box.setRange(min_, max_)

    def submit_input(self):
        expression = self.expression_line_edit.text()
        depth = self.depth_slider.value()
        numerators = self.get_numerators()
        self.submitted.emit(ContinuedFractionCalculatorRequestForm(expression, depth, numerators))

    def get_numerators(self):
        # TODO: After making evaluation class, use it
        # TODO: Actually, send raw text and process it later
        if self.numerators_customized_radio_button.isChecked():

            if (tokens := self.numerators_cycle_line_edit.text().strip().split(',')) != ['']:
                sequence = map(int, tokens)
            else:
                sequence = iter([])

            if self.numerators_cycle_line_edit:
                _cycle = map(int, self.numerators_cycle_line_edit.text().split(','))
            else:
                _cycle = iter([])

            return chain(sequence, cycle(_cycle))
        else:
            return repeat(1)

    @QtCore.pyqtSlot(QtGui.QPixmap)
    def display_result_pixmap(self, pixmap):
        self.result_render_area.setPixmap(pixmap)
        self.result_render_area.show()

    @QtCore.pyqtSlot(Exception)
    def process_exception(self, exception):
        # TODO: Better Exception handling
        QtWidgets.QMessageBox.critical(self, type(exception).__name__, str(exception))
