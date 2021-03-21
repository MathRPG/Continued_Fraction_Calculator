# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scf_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SimpleContinuedFractionCalculatorForm(object):
    def setupUi(self, SimpleContinuedFractionCalculatorForm):
        SimpleContinuedFractionCalculatorForm.setObjectName("SimpleContinuedFractionCalculatorForm")
        SimpleContinuedFractionCalculatorForm.resize(640, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SimpleContinuedFractionCalculatorForm.sizePolicy().hasHeightForWidth())
        SimpleContinuedFractionCalculatorForm.setSizePolicy(sizePolicy)
        SimpleContinuedFractionCalculatorForm.setMinimumSize(QtCore.QSize(640, 800))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(14)
        SimpleContinuedFractionCalculatorForm.setFont(font)
        SimpleContinuedFractionCalculatorForm.setWindowTitle("Calculator")
        self.verticalLayout = QtWidgets.QVBoxLayout(SimpleContinuedFractionCalculatorForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_label = QtWidgets.QLabel(SimpleContinuedFractionCalculatorForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setMinimumSize(QtCore.QSize(622, 40))
        self.title_label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.form_expression_label = QtWidgets.QLabel(SimpleContinuedFractionCalculatorForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.form_expression_label.sizePolicy().hasHeightForWidth())
        self.form_expression_label.setSizePolicy(sizePolicy)
        self.form_expression_label.setMinimumSize(QtCore.QSize(0, 20))
        self.form_expression_label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.form_expression_label.setFont(font)
        self.form_expression_label.setObjectName("form_expression_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.form_expression_label)
        self.form_expression_line_edit = QtWidgets.QLineEdit(SimpleContinuedFractionCalculatorForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.form_expression_line_edit.sizePolicy().hasHeightForWidth())
        self.form_expression_line_edit.setSizePolicy(sizePolicy)
        self.form_expression_line_edit.setMinimumSize(QtCore.QSize(0, 40))
        self.form_expression_line_edit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.form_expression_line_edit.setBaseSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.form_expression_line_edit.setFont(font)
        self.form_expression_line_edit.setText("")
        self.form_expression_line_edit.setObjectName("form_expression_line_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.form_expression_line_edit)
        self.form_depth_label = QtWidgets.QLabel(SimpleContinuedFractionCalculatorForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.form_depth_label.sizePolicy().hasHeightForWidth())
        self.form_depth_label.setSizePolicy(sizePolicy)
        self.form_depth_label.setMinimumSize(QtCore.QSize(0, 20))
        self.form_depth_label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.form_depth_label.setFont(font)
        self.form_depth_label.setObjectName("form_depth_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.form_depth_label)
        self.form_depth_spin_box = QtWidgets.QSpinBox(SimpleContinuedFractionCalculatorForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.form_depth_spin_box.sizePolicy().hasHeightForWidth())
        self.form_depth_spin_box.setSizePolicy(sizePolicy)
        self.form_depth_spin_box.setMinimumSize(QtCore.QSize(0, 40))
        self.form_depth_spin_box.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.form_depth_spin_box.setFont(font)
        self.form_depth_spin_box.setObjectName("form_depth_spin_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.form_depth_spin_box)
        self.verticalLayout.addLayout(self.formLayout)
        self.form_submit_push_button = QtWidgets.QPushButton(SimpleContinuedFractionCalculatorForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.form_submit_push_button.sizePolicy().hasHeightForWidth())
        self.form_submit_push_button.setSizePolicy(sizePolicy)
        self.form_submit_push_button.setMinimumSize(QtCore.QSize(0, 30))
        self.form_submit_push_button.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.form_submit_push_button.setFont(font)
        self.form_submit_push_button.setFlat(False)
        self.form_submit_push_button.setObjectName("form_submit_push_button")
        self.verticalLayout.addWidget(self.form_submit_push_button, 0, QtCore.Qt.AlignHCenter)
        self.form_results_horizontal_line = QtWidgets.QFrame(SimpleContinuedFractionCalculatorForm)
        self.form_results_horizontal_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.form_results_horizontal_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.form_results_horizontal_line.setObjectName("form_results_horizontal_line")
        self.verticalLayout.addWidget(self.form_results_horizontal_line)
        self.result_label = QtWidgets.QLabel(SimpleContinuedFractionCalculatorForm)
        self.result_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_label.sizePolicy().hasHeightForWidth())
        self.result_label.setSizePolicy(sizePolicy)
        self.result_label.setMinimumSize(QtCore.QSize(0, 21))
        self.result_label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.result_label.setBaseSize(QtCore.QSize(0, 12))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.result_label.setFont(font)
        self.result_label.setObjectName("result_label")
        self.verticalLayout.addWidget(self.result_label, 0, QtCore.Qt.AlignHCenter)
        self.result_render_label = QtWidgets.QLabel(SimpleContinuedFractionCalculatorForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_render_label.sizePolicy().hasHeightForWidth())
        self.result_render_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.result_render_label.setFont(font)
        self.result_render_label.setStyleSheet("border: 1pt solid black")
        self.result_render_label.setAlignment(QtCore.Qt.AlignCenter)
        self.result_render_label.setObjectName("result_render_label")
        self.verticalLayout.addWidget(self.result_render_label)

        self.retranslateUi(SimpleContinuedFractionCalculatorForm)
        QtCore.QMetaObject.connectSlotsByName(SimpleContinuedFractionCalculatorForm)

    def retranslateUi(self, SimpleContinuedFractionCalculatorForm):
        _translate = QtCore.QCoreApplication.translate
        self.title_label.setText(_translate("SimpleContinuedFractionCalculatorForm", "Simple Continued Fraction Calculator"))
        self.form_expression_label.setText(_translate("SimpleContinuedFractionCalculatorForm", "Expression"))
        self.form_expression_line_edit.setPlaceholderText(_translate("SimpleContinuedFractionCalculatorForm", "Type Here"))
        self.form_depth_label.setText(_translate("SimpleContinuedFractionCalculatorForm", "Depth"))
        self.form_submit_push_button.setText(_translate("SimpleContinuedFractionCalculatorForm", "Calculate"))
        self.result_label.setText(_translate("SimpleContinuedFractionCalculatorForm", "Result"))
        self.result_render_label.setText(_translate("SimpleContinuedFractionCalculatorForm", "Result Fraction will be rendered here"))
