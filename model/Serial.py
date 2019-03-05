import sys

import serial
import serial.tools.list_ports

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QPushButton, QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsRectItem, QGraphicsEllipseItem
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, pyqtSlot, QObject,QRectF
from PyQt5.QtGui import QBrush, QPen, QColor

from Ui_serialwindow import Ui_Frame

class Serial(QtWidgets.QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super(Serial, self).__init__(parent=parent)
        self.setupUi(self)
        print("hello world")
        self.serial_uwb =serial.Serial()
        self.port_check()

    def port_check(self):
        """ 检测所有串口 """
        self.com_dict = {} # 将所有串口信息存储在字典中
        port_list = list(serial.tools.list_ports.comports())
        self.s1__box_2.clear()
        for port in port_list:
            self.com_dict["%s" % port[0]] = "%s" % port[1]
            self.s1__box_2.addItem(port[0])
        if len(self.com_dict) == 0:
            self.open_serial_button.setEnabled(False)


if __name__ == '__main__':
    serial_app = QtWidgets.QApplication(sys.argv)

    serial_form = Serial()
    serial_form.show()

    sys.exit(serial_app.exec_())
