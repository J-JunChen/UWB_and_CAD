import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QPushButton, QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsRectItem, QGraphicsEllipseItem, QTableWidgetItem, QLabel
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, pyqtSlot, QObject, QRectF
from PyQt5.QtGui import QBrush, QPen, QColor

from Ui_test_mouse import Ui_MainWindow


class Main_Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main_Window, self).__init__(parent=parent)
        self.setupUi(self)
        # self.initUi()
        # self.setMouseTracking(True)
        self.graphicsView.setMouseTracking(True)
        # self.graphicsView = GraphicsView()
        

    def initUi(self):
        self.setGeometry(400, 300, 400, 300)
        self.setWindowTitle("键盘响应事件")
        self.lab1 = QLabel("方向", self)
        self.lab1.setGeometry(200, 150, 100, 100)
        self.lab2 = QLabel("显示鼠标坐标", self)
        self.lab2.setGeometry(200, 80, 100, 100)

    def mouseMoveEvent(self, event):
        graph_w = self.graphicsView.width()
        graph_h = self.graphicsView.height()
        graph_x = self.graphicsView.x()
        graph_y = self.graphicsView.y()

        self.pos = event.pos()
        

        self.graphicsView.mouseMoveEvent(event)
        
    
    # def wheelEvent(self, event):
    #     print("你上当了")
        # self.graphicsView.wheelEvent(event)



class GraphicsView(QGraphicsView):
    def __init__(self):
        super(GraphicsView, self).__init__()
        print("haha")
    
    def wheelEvent(self, event):
        print("wheelEvent")
    
    def mouseMoveEvent(self, event):
        self.pos = event.pos()
        print(self.pos)
        self.update()


if __name__ == '__main__':
    main_app = QtWidgets.QApplication(sys.argv)

    main_form = Main_Window()
    main_form.show()

    sys.exit(main_app.exec_())
