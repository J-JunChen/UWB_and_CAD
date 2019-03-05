# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jun/Documents/UWB_and_CAD/model/serialwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(339, 226)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.formGroupBox = QtWidgets.QGroupBox(Frame)
        self.formGroupBox.setGeometry(QtCore.QRect(60, 20, 221, 201))
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.s1__lb_1 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_1.setObjectName("s1__lb_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.s1__lb_1)
        self.s1__box_1 = QtWidgets.QPushButton(self.formGroupBox)
        self.s1__box_1.setAutoRepeatInterval(100)
        self.s1__box_1.setDefault(True)
        self.s1__box_1.setObjectName("s1__box_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.s1__box_1)
        self.s1__lb_2 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_2.setObjectName("s1__lb_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.s1__lb_2)
        self.s1__box_2 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_2.setObjectName("s1__box_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.s1__box_2)
        self.open_serial_button = QtWidgets.QPushButton(self.formGroupBox)
        self.open_serial_button.setObjectName("open_serial_button")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.open_serial_button)
        self.close_serial_button = QtWidgets.QPushButton(self.formGroupBox)
        self.close_serial_button.setObjectName("close_serial_button")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.close_serial_button)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.formGroupBox.setTitle(_translate("Frame", "串口设置"))
        self.s1__lb_1.setText(_translate("Frame", "串口检测："))
        self.s1__box_1.setText(_translate("Frame", "检测串口"))
        self.s1__lb_2.setText(_translate("Frame", "串口选择："))
        self.open_serial_button.setText(_translate("Frame", "打开串口"))
        self.close_serial_button.setText(_translate("Frame", "关闭串口"))


