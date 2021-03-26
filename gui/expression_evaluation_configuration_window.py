from PyQt5 import QtWidgets, QtCore

from gui.ui_expression_evaluation_configuration_window import Ui_ExpressionEvaluationConfigurationWindow


class ExpressionEvaluationConfigurationWindow(QtWidgets.QWidget, Ui_ExpressionEvaluationConfigurationWindow):
    added = QtCore.pyqtSignal(str, str)
    removed = QtCore.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    @QtCore.pyqtSlot(dict[str, str])
    def update_tokens(self, token_dict=None):
        if token_dict is None:
            token_dict = {}

        for token, expr in token_dict.items():
            print(f'Token {token} is binded to expression {expr}')
