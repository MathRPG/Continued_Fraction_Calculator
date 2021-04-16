from PyQt5 import QtWidgets, QtCore, QtGui

from continued_fraction.calculator_request_form import CalculatorRequestForm
from gui.ui_main_window import Ui_MainWindow
from utils.latex_to_pixmap import latex_to_pixmap


class MainWindow(QtWidgets.QWidget, Ui_MainWindow):
    submitted = QtCore.pyqtSignal(CalculatorRequestForm)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.calculate_push_button.clicked.connect(self.submit_form)

    def submit_form(self):
        expression = self.expression_line_edit.text()
        depth = self.depth_spin_box.value()
        numerators = self.get_numerator_input()
        latex_style = self.display_format_combo_box.currentText()
        self.submitted.emit(CalculatorRequestForm(expression, depth, numerators, latex_style))

    def get_numerator_input(self):
        if self.numerators_simple_radio_button.isChecked():
            return None
        return self.numerators_sequence_line_edit.text(), self.numerators_cycle_line_edit.text()

    @QtCore.pyqtSlot(QtGui.QPixmap)
    def display_result_latex(self, latex: str):
        pixmap = latex_to_pixmap(f'${latex}$')
        self.result_render_area.setPixmap(pixmap)
        self.result_render_area.show()

    @QtCore.pyqtSlot(Exception)
    def process_exception(self, exception: Exception):
        QtWidgets.QMessageBox.critical(self, type(exception).__name__, str(exception))
