# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jun/Documents/UWB_and_CAD/view/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1861, 1114)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setObjectName("centralwidget")
        self.formGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.formGroupBox.setGeometry(QtCore.QRect(20, 10, 221, 201))
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
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 250, 791, 791))
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.setObjectName("graphicsView")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(270, 10, 291, 201))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 81, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 71, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(30, 120, 61, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(60, 160, 31, 20))
        self.label_6.setObjectName("label_6")
        self.horizontal_textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.horizontal_textEdit.setGeometry(QtCore.QRect(100, 30, 61, 31))
        self.horizontal_textEdit.setObjectName("horizontal_textEdit")
        self.computer_size_textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.computer_size_textEdit.setGeometry(QtCore.QRect(100, 70, 61, 31))
        self.computer_size_textEdit.setObjectName("computer_size_textEdit")
        self.dpi_textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.dpi_textEdit.setGeometry(QtCore.QRect(100, 110, 61, 31))
        self.dpi_textEdit.setObjectName("dpi_textEdit")
        self.dot_pitch_textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.dot_pitch_textEdit.setGeometry(QtCore.QRect(100, 150, 61, 31))
        self.dot_pitch_textEdit.setObjectName("dot_pitch_textEdit")
        self.longitudinal_textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.longitudinal_textEdit.setGeometry(QtCore.QRect(190, 30, 61, 31))
        self.longitudinal_textEdit.setObjectName("longitudinal_textEdit")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(170, 30, 21, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(170, 80, 61, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(170, 120, 61, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(170, 160, 91, 20))
        self.label_10.setObjectName("label_10")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(580, 10, 221, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(10, 40, 31, 20))
        self.label_11.setObjectName("label_11")
        self.brick_length_textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.brick_length_textEdit.setGeometry(QtCore.QRect(40, 30, 61, 31))
        self.brick_length_textEdit.setObjectName("brick_length_textEdit")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(120, 40, 31, 20))
        self.label_12.setObjectName("label_12")
        self.brick_width_textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.brick_width_textEdit.setGeometry(QtCore.QRect(150, 30, 61, 31))
        self.brick_width_textEdit.setObjectName("brick_width_textEdit")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(820, 780, 1061, 261))
        self.groupBox_3.setObjectName("groupBox_3")
        self.anchorTable = QtWidgets.QTableWidget(self.groupBox_3)
        self.anchorTable.setGeometry(QtCore.QRect(20, 30, 291, 171))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.anchorTable.sizePolicy().hasHeightForWidth())
        self.anchorTable.setSizePolicy(sizePolicy)
        self.anchorTable.setMinimumSize(QtCore.QSize(0, 112))
        self.anchorTable.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.anchorTable.setFont(font)
        self.anchorTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.anchorTable.setAlternatingRowColors(True)
        self.anchorTable.setRowCount(5)
        self.anchorTable.setColumnCount(4)
        self.anchorTable.setObjectName("anchorTable")
        self.anchorTable.horizontalHeader().setDefaultSectionSize(72)
        self.anchorTable.horizontalHeader().setMinimumSectionSize(70)
        self.anchorTable.horizontalHeader().setStretchLastSection(False)
        self.anchorTable.verticalHeader().setVisible(False)
        self.anchorTable.verticalHeader().setDefaultSectionSize(27)
        self.anchorTable.verticalHeader().setHighlightSections(True)
        self.anchorTable.verticalHeader().setMinimumSectionSize(20)
        self.vertexTable = QtWidgets.QTableWidget(self.groupBox_3)
        self.vertexTable.setGeometry(QtCore.QRect(330, 30, 311, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vertexTable.sizePolicy().hasHeightForWidth())
        self.vertexTable.setSizePolicy(sizePolicy)
        self.vertexTable.setMinimumSize(QtCore.QSize(0, 112))
        self.vertexTable.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vertexTable.setFont(font)
        self.vertexTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.vertexTable.setAlternatingRowColors(True)
        self.vertexTable.setRowCount(11)
        self.vertexTable.setColumnCount(4)
        self.vertexTable.setObjectName("vertexTable")
        self.vertexTable.horizontalHeader().setDefaultSectionSize(72)
        self.vertexTable.horizontalHeader().setMinimumSectionSize(70)
        self.vertexTable.horizontalHeader().setStretchLastSection(False)
        self.vertexTable.verticalHeader().setVisible(False)
        self.vertexTable.verticalHeader().setDefaultSectionSize(27)
        self.vertexTable.verticalHeader().setHighlightSections(True)
        self.vertexTable.verticalHeader().setMinimumSectionSize(20)
        self.brickTable = QtWidgets.QTableWidget(self.groupBox_3)
        self.brickTable.setGeometry(QtCore.QRect(660, 30, 380, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brickTable.sizePolicy().hasHeightForWidth())
        self.brickTable.setSizePolicy(sizePolicy)
        self.brickTable.setMinimumSize(QtCore.QSize(0, 112))
        self.brickTable.setMaximumSize(QtCore.QSize(380, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.brickTable.setFont(font)
        self.brickTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.brickTable.setAlternatingRowColors(True)
        self.brickTable.setRowCount(21)
        self.brickTable.setColumnCount(5)
        self.brickTable.setObjectName("brickTable")
        self.brickTable.horizontalHeader().setDefaultSectionSize(72)
        self.brickTable.horizontalHeader().setMinimumSectionSize(70)
        self.brickTable.horizontalHeader().setStretchLastSection(False)
        self.brickTable.verticalHeader().setVisible(False)
        self.brickTable.verticalHeader().setDefaultSectionSize(27)
        self.brickTable.verticalHeader().setHighlightSections(True)
        self.brickTable.verticalHeader().setMinimumSectionSize(20)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(580, 100, 221, 111))
        self.groupBox_4.setObjectName("groupBox_4")
        self.room_num_textEdit = QtWidgets.QTextEdit(self.groupBox_4)
        self.room_num_textEdit.setGeometry(QtCore.QRect(110, 30, 81, 31))
        self.room_num_textEdit.setObjectName("room_num_textEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 71, 20))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(10, 60, 91, 41))
        self.label.setObjectName("label")
        self.ratio_textEdit = QtWidgets.QTextEdit(self.groupBox_4)
        self.ratio_textEdit.setGeometry(QtCore.QRect(110, 70, 82, 31))
        self.ratio_textEdit.setObjectName("ratio_textEdit")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(1360, 10, 481, 651))
        self.groupBox_6.setObjectName("groupBox_6")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox.setGeometry(QtCore.QRect(150, 40, 251, 26))
        self.comboBox.setObjectName("comboBox")
        self.label_13 = QtWidgets.QLabel(self.groupBox_6)
        self.label_13.setGeometry(QtCore.QRect(40, 40, 101, 21))
        self.label_13.setObjectName("label_13")
        self.room_label = QtWidgets.QLabel(self.groupBox_6)
        self.room_label.setGeometry(QtCore.QRect(30, 80, 431, 551))
        self.room_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.room_label.setAlignment(QtCore.Qt.AlignCenter)
        self.room_label.setObjectName("room_label")
        self.comboBox.raise_()
        self.comboBox.raise_()
        self.label_13.raise_()
        self.room_label.raise_()
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(830, 10, 491, 651))
        self.groupBox_7.setObjectName("groupBox_7")
        self.drawing_label = QtWidgets.QLabel(self.groupBox_7)
        self.drawing_label.setGeometry(QtCore.QRect(10, 30, 451, 581))
        self.drawing_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.drawing_label.setAlignment(QtCore.Qt.AlignCenter)
        self.drawing_label.setObjectName("drawing_label")
        self.cad_label = QtWidgets.QLabel(self.groupBox_7)
        self.cad_label.setGeometry(QtCore.QRect(30, 620, 131, 31))
        self.cad_label.setAutoFillBackground(False)
        self.cad_label.setObjectName("cad_label")
        self.drawing_label.raise_()
        self.drawing_label.raise_()
        self.cad_label.raise_()
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1360, 670, 481, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.left_Button.setObjectName("left_Button")
        self.horizontalLayout.addWidget(self.left_Button)
        self.right_Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.right_Button.setObjectName("right_Button")
        self.horizontalLayout.addWidget(self.right_Button)
        self.confirm_Button = QtWidgets.QPushButton(self.centralwidget)
        self.confirm_Button.setGeometry(QtCore.QRect(1360, 715, 481, 41))
        self.confirm_Button.setObjectName("confirm_Button")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(830, 670, 491, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.choose_pdf_Button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.choose_pdf_Button.setObjectName("choose_pdf_Button")
        self.horizontalLayout_2.addWidget(self.choose_pdf_Button)
        self.analyse_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.analyse_button.setAutoRepeatInterval(100)
        self.analyse_button.setDefault(True)
        self.analyse_button.setObjectName("analyse_button")
        self.horizontalLayout_2.addWidget(self.analyse_button)
        self.formGroupBox.raise_()
        self.graphicsView.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.groupBox_4.raise_()
        self.groupBox_6.raise_()
        self.groupBox_7.raise_()
        self.horizontalLayoutWidget.raise_()
        self.confirm_Button.raise_()
        self.left_Button.raise_()
        self.horizontalLayoutWidget_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1861, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.formGroupBox.setTitle(_translate("MainWindow", "串口设置"))
        self.s1__lb_1.setText(_translate("MainWindow", "串口检测："))
        self.s1__box_1.setText(_translate("MainWindow", "检测串口"))
        self.s1__lb_2.setText(_translate("MainWindow", "串口选择："))
        self.open_serial_button.setText(_translate("MainWindow", "打开串口"))
        self.close_serial_button.setText(_translate("MainWindow", "关闭串口"))
        self.groupBox.setTitle(_translate("MainWindow", "dpi设置"))
        self.label_3.setText(_translate("MainWindow", "电脑分辨率："))
        self.label_4.setText(_translate("MainWindow", "电脑尺寸："))
        self.label_5.setText(_translate("MainWindow", " =   dpi："))
        self.label_6.setText(_translate("MainWindow", "="))
        self.horizontal_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">1920</span></p></body></html>"))
        self.computer_size_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">15.6</span></p></body></html>"))
        self.dpi_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">141.22</span></p></body></html>"))
        self.dot_pitch_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">0.1799</span></p></body></html>"))
        self.longitudinal_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">1080</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "X"))
        self.label_8.setText(_translate("MainWindow", "英寸"))
        self.label_9.setText(_translate("MainWindow", "PPI"))
        self.label_10.setText(_translate("MainWindow", "mm dot pitch"))
        self.groupBox_2.setTitle(_translate("MainWindow", "砖块设置 (单位 / mm)"))
        self.label_11.setText(_translate("MainWindow", "长："))
        self.brick_length_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">3</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "宽："))
        self.brick_width_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">3</span></p></body></html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "坐标点设置"))
        self.groupBox_4.setTitle(_translate("MainWindow", "其他设置"))
        self.room_num_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">3</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "房间个数："))
        self.label.setText(_translate("MainWindow", "  图纸比例   1："))
        self.ratio_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">50</span></p></body></html>"))
        self.groupBox_6.setTitle(_translate("MainWindow", "区域选择框"))
        self.label_13.setText(_translate("MainWindow", "请选择房间号："))
        self.room_label.setText(_translate("MainWindow", "房间显示位置"))
        self.groupBox_7.setTitle(_translate("MainWindow", "图纸显示框"))
        self.drawing_label.setText(_translate("MainWindow", "图纸显示位置"))
        self.cad_label.setText(_translate("MainWindow", "图纸名称"))
        self.left_Button.setText(_translate("MainWindow", "左转"))
        self.right_Button.setText(_translate("MainWindow", "右转"))
        self.confirm_Button.setText(_translate("MainWindow", "确认"))
        self.choose_pdf_Button.setText(_translate("MainWindow", "选择PDF文件"))
        self.analyse_button.setText(_translate("MainWindow", "数据分析"))


