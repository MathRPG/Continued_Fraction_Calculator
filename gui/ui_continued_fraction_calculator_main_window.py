# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'continued_fraction_calculator_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ContinuedFractionCalculatorMainWindow(object):
    def setupUi(self, ContinuedFractionCalculatorMainWindow):
        ContinuedFractionCalculatorMainWindow.setObjectName("ContinuedFractionCalculatorMainWindow")
        ContinuedFractionCalculatorMainWindow.resize(400, 626)
        ContinuedFractionCalculatorMainWindow.setStatusTip("")
        ContinuedFractionCalculatorMainWindow.setWhatsThis("")
        ContinuedFractionCalculatorMainWindow.setAccessibleName("")
        ContinuedFractionCalculatorMainWindow.setAccessibleDescription("")
        ContinuedFractionCalculatorMainWindow.setWindowFilePath("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ContinuedFractionCalculatorMainWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(ContinuedFractionCalculatorMainWindow)
        self.label.setToolTip("")
        self.label.setText("Continued Fraction Calculator")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(ContinuedFractionCalculatorMainWindow)
        self.label_2.setToolTip("")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.expression_line_edit = QtWidgets.QLineEdit(ContinuedFractionCalculatorMainWindow)
        self.expression_line_edit.setToolTip("")
        self.expression_line_edit.setPlaceholderText("")
        self.expression_line_edit.setObjectName("expression_line_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.expression_line_edit)
        self.label_3 = QtWidgets.QLabel(ContinuedFractionCalculatorMainWindow)
        self.label_3.setToolTip("")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.depth_slider = QtWidgets.QSlider(ContinuedFractionCalculatorMainWindow)
        self.depth_slider.setToolTip("")
        self.depth_slider.setMinimum(0)
        self.depth_slider.setMaximum(40)
        self.depth_slider.setProperty("value", 5)
        self.depth_slider.setOrientation(QtCore.Qt.Horizontal)
        self.depth_slider.setInvertedAppearance(False)
        self.depth_slider.setInvertedControls(False)
        self.depth_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.depth_slider.setTickInterval(5)
        self.depth_slider.setObjectName("depth_slider")
        self.horizontalLayout_2.addWidget(self.depth_slider)
        self.depth_spin_box = QtWidgets.QSpinBox(ContinuedFractionCalculatorMainWindow)
        self.depth_spin_box.setMaximum(40)
        self.depth_spin_box.setProperty("value", 5)
        self.depth_spin_box.setObjectName("depth_spin_box")
        self.horizontalLayout_2.addWidget(self.depth_spin_box)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(ContinuedFractionCalculatorMainWindow)
        self.label_4.setToolTip("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.numerators_simple_radio_button = QtWidgets.QRadioButton(ContinuedFractionCalculatorMainWindow)
        self.numerators_simple_radio_button.setToolTip("")
        self.numerators_simple_radio_button.setChecked(True)
        self.numerators_simple_radio_button.setObjectName("numerators_simple_radio_button")
        self.verticalLayout.addWidget(self.numerators_simple_radio_button)
        self.numerators_customized_radio_button = QtWidgets.QRadioButton(ContinuedFractionCalculatorMainWindow)
        self.numerators_customized_radio_button.setToolTip("")
        self.numerators_customized_radio_button.setChecked(False)
        self.numerators_customized_radio_button.setObjectName("numerators_customized_radio_button")
        self.verticalLayout.addWidget(self.numerators_customized_radio_button)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(ContinuedFractionCalculatorMainWindow)
        self.label_5.setToolTip("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(ContinuedFractionCalculatorMainWindow)
        self.label_6.setToolTip("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.numerators_sequence_line_edit = QtWidgets.QLineEdit(ContinuedFractionCalculatorMainWindow)
        self.numerators_sequence_line_edit.setEnabled(False)
        self.numerators_sequence_line_edit.setToolTip("")
        self.numerators_sequence_line_edit.setPlaceholderText("")
        self.numerators_sequence_line_edit.setObjectName("numerators_sequence_line_edit")
        self.gridLayout.addWidget(self.numerators_sequence_line_edit, 1, 0, 1, 1)
        self.numerators_cycle_line_edit = QtWidgets.QLineEdit(ContinuedFractionCalculatorMainWindow)
        self.numerators_cycle_line_edit.setEnabled(False)
        self.numerators_cycle_line_edit.setToolTip("")
        self.numerators_cycle_line_edit.setPlaceholderText("")
        self.numerators_cycle_line_edit.setObjectName("numerators_cycle_line_edit")
        self.gridLayout.addWidget(self.numerators_cycle_line_edit, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.calculate_push_button = QtWidgets.QPushButton(ContinuedFractionCalculatorMainWindow)
        self.calculate_push_button.setToolTip("")
        self.calculate_push_button.setObjectName("calculate_push_button")
        self.verticalLayout_2.addWidget(self.calculate_push_button)
        self.line = QtWidgets.QFrame(ContinuedFractionCalculatorMainWindow)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.label_7 = QtWidgets.QLabel(ContinuedFractionCalculatorMainWindow)
        self.label_7.setToolTip("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.result_render_area = QtWidgets.QLabel(ContinuedFractionCalculatorMainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_render_area.sizePolicy().hasHeightForWidth())
        self.result_render_area.setSizePolicy(sizePolicy)
        self.result_render_area.setAlignment(QtCore.Qt.AlignCenter)
        self.result_render_area.setObjectName("result_render_area")
        self.verticalLayout_2.addWidget(self.result_render_area)

        self.retranslateUi(ContinuedFractionCalculatorMainWindow)
        self.numerators_simple_radio_button.toggled['bool'].connect(self.numerators_sequence_line_edit.setDisabled)
        self.numerators_simple_radio_button.toggled['bool'].connect(self.numerators_cycle_line_edit.setDisabled)
        self.depth_slider.valueChanged['int'].connect(self.depth_spin_box.setValue)
        self.depth_spin_box.valueChanged['int'].connect(self.depth_slider.setValue)
        QtCore.QMetaObject.connectSlotsByName(ContinuedFractionCalculatorMainWindow)

    def retranslateUi(self, ContinuedFractionCalculatorMainWindow):
        _translate = QtCore.QCoreApplication.translate
        ContinuedFractionCalculatorMainWindow.setWindowTitle(_translate("ContinuedFractionCalculatorMainWindow", "Continued Fraction Calculator"))
        self.label_2.setText(_translate("ContinuedFractionCalculatorMainWindow", "Expression"))
        self.label_3.setText(_translate("ContinuedFractionCalculatorMainWindow", "Depth"))
        self.label_4.setText(_translate("ContinuedFractionCalculatorMainWindow", "Numerators"))
        self.numerators_simple_radio_button.setText(_translate("ContinuedFractionCalculatorMainWindow", "Simple"))
        self.numerators_customized_radio_button.setText(_translate("ContinuedFractionCalculatorMainWindow", "Customized"))
        self.label_5.setText(_translate("ContinuedFractionCalculatorMainWindow", "Sequence"))
        self.label_6.setText(_translate("ContinuedFractionCalculatorMainWindow", "Cycle"))
        self.calculate_push_button.setText(_translate("ContinuedFractionCalculatorMainWindow", "Calculate"))
        self.label_7.setText(_translate("ContinuedFractionCalculatorMainWindow", "Results"))
        self.result_render_area.setText(_translate("ContinuedFractionCalculatorMainWindow", "Results will be rendered here"))
