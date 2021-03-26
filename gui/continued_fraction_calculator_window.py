from PyQt5 import QtWidgets, QtCore, QtGui

from continued_fraction_calculator_form import ContinuedFractionCalculatorForm
from gui.ui_continued_fraction_calculator_main_window import Ui_ContinuedFractionCalculatorMainWindow


class ContinuedFractionCalculatorWindow(QtWidgets.QWidget, Ui_ContinuedFractionCalculatorMainWindow):
    submitted = QtCore.pyqtSignal(ContinuedFractionCalculatorForm)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.calculate_push_button.clicked.connect(self.submit_input)

    def submit_input(self):
        expression = self.expression_line_edit.text()
        depth = self.depth_slider.value()
        self.submitted.emit(ContinuedFractionCalculatorForm(expression, depth))

    @QtCore.pyqtSlot(QtGui.QPixmap)
    def display_result_pixmap(self, pixmap):
        self.result_render_area.setPixmap(pixmap)
        self.result_render_area.show()

    @QtCore.pyqtSlot(Exception)
    def process_exception(self, exception):
        # TODO: Better Exception handling
        QtWidgets.QMessageBox.critical(self, type(exception).__name__, str(exception))
