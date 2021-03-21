from PyQt5 import QtWidgets, QtCore, QtGui

from gui.simple_continued_fraction_calculator_ui import Ui_SimpleContinuedFractionCalculatorForm


class SimpleContinuedFractionCalculatorWindow(QtWidgets.QWidget, Ui_SimpleContinuedFractionCalculatorForm):
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
    def display_result_pixmap(self, pixmap):
        self.result_render_label.setPixmap(pixmap)
        self.result_render_label.show()

    @QtCore.pyqtSlot(Exception)
    def process_exception(self, exception):
        # TODO: Better Exception Handling; I'm thinking custom messages and/or making the text boxes red
        QtWidgets.QMessageBox.critical(self, str(type(exception)), str(exception))
