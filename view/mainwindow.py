import sys
import os
import numpy as np

import serial
import serial.tools.list_ports

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QPushButton, QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsRectItem, QGraphicsEllipseItem, QTableWidgetItem
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, pyqtSlot, QObject, QRectF
from PyQt5.QtGui import QBrush, QPen, QColor

from Ui_untitled import Ui_MainWindow

dir_path = os.path.dirname(os.path.realpath(__file__))  # 获取当前路径
former_path = dir_path[:dir_path.rfind('/')]
sys.path.append(former_path+'/network')  # ui视图层
import RTLSClient as rc


class Main_Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main_Window, self).__init__(parent=parent)
        self.setupUi(self)
        
        self.init_anchor()
        self.init_vertex()

        self.init_serial()
        self.setWindowTitle("UWB串口助手")
        self.serial_uwb = serial.Serial()
        self.port_check()

        self.graphicsView.scale(1,-1) # x轴倒转
        self.init_graphicsView()
        self.graphics()

        # self.plainTextEdit.set
        

    def init_serial(self):
        """ 初始化串口 """
        # 串口检测按钮
        self.s1__box_1.clicked.connect(self.port_check)
        # 串口信息显示
        # self.s1__box_2.currentTextChanged.connect(self.port_info)
        # 打开串口按钮
        self.open_serial_button.clicked.connect(self.port_open)
        # 关闭串口按钮
        self.close_serial_button.clicked.connect(self.port_close)
        # 接受数据定时器
        self.timer_receive = QTimer(self)
        self.timer_receive.timeout.connect(self.data_receive)
    
    def init_anchor(self):
        """ 初始化基站 """
        self.anchorTable.setItem(0,0, QTableWidgetItem("基站编号"))
        self.anchorTable.setItem(0,1, QTableWidgetItem("X轴 / m"))
        self.anchorTable.setItem(0,2, QTableWidgetItem("Y轴 / m"))
        self.anchorTable.setItem(0,3, QTableWidgetItem("Z轴 / m"))
        self.anchorTable.setItem(1,0, QTableWidgetItem("anchor_0"))
        self.anchorTable.setItem(2,0, QTableWidgetItem("anchor_1"))
        self.anchorTable.setItem(3,0, QTableWidgetItem("anchor_2"))
        self.anchorTable.setItem(4,0, QTableWidgetItem("anchor_3"))
        
        # 初始化anchor_0的X,Y,Z轴
        self.anchorTable.setItem(1,1, QTableWidgetItem("0.00"))
        self.anchorTable.setItem(1,2, QTableWidgetItem("0.00"))
        self.anchorTable.setItem(1,3, QTableWidgetItem("1.50"))

        # 初始化anchor_1的X,Y,Z轴
        self.anchorTable.setItem(2,1, QTableWidgetItem("3.75"))
        self.anchorTable.setItem(2,2, QTableWidgetItem("0.00"))
        self.anchorTable.setItem(2,3, QTableWidgetItem("1.50"))

        # 初始化anchor_2的X,Y,Z轴
        self.anchorTable.setItem(3,1, QTableWidgetItem("0.00"))
        self.anchorTable.setItem(3,2, QTableWidgetItem("7.50"))
        self.anchorTable.setItem(3,3, QTableWidgetItem("1.50"))

        # 初始化anchor_3的X,Y,Z轴
        self.anchorTable.setItem(4,1, QTableWidgetItem("0.00"))
        self.anchorTable.setItem(4,2, QTableWidgetItem("0.00"))
        self.anchorTable.setItem(4,3, QTableWidgetItem("1.50"))
    
    def init_vertex(self):
        """ 初始化顶点 """
        self.vertexTable.setItem(0, 0, QTableWidgetItem("顶点编号"))
        self.vertexTable.setItem(0, 1, QTableWidgetItem("X轴 / m"))
        self.vertexTable.setItem(0, 2, QTableWidgetItem("Y轴 / m"))
        self.vertexTable.setItem(0, 3, QTableWidgetItem("Z轴 / m"))
        for i in range(10):
            self.vertexTable.setItem(i+1, 0, QTableWidgetItem("vertex_"+str(i)))
            self.vertexTable.setItem(i+1, 1, QTableWidgetItem("0.00"))
            self.vertexTable.setItem(i+1, 2, QTableWidgetItem("0.00"))
            self.vertexTable.setItem(i+1, 3, QTableWidgetItem("0.00"))
        

    def port_check(self):
        """ 检测所有串口 """
        self.com_dict = {}  # 将所有串口信息存储在字典中
        port_list = list(serial.tools.list_ports.comports())
        self.s1__box_2.clear()
        for port in port_list:
            self.com_dict["%s" % port[0]] = "%s" % port[1]
            self.s1__box_2.addItem(port[0])
        if len(self.com_dict) == 0:
            self.open_serial_button.setEnabled(False)
        
    def port_open(self):
        """ 打开串口 """
        # self.serial_uwb.port = "COM3"  #串口号
        self.serial_uwb.port = self.s1__box_2.currentText()
        self.serial_uwb.baudrate = int(115200)  # 波特率
        self.serial_uwb.bytesize = int(8)  # 数据位
        self.serial_uwb.parity = "N"  # 奇偶性，即校验位
        self.serial_uwb.stopbits = int(1)  # 停止位
            
        # sudo chmod a+rw /dev/ttyACM0 给予权限

        try:
            self.serial_uwb.open()
        except:
            QMessageBox.critical(self, "Port Error", "此串口不能打开！")
            return None

        # 打开串口接收定时器，周期为2ms
        self.timer_receive.start(200)

        if self.serial_uwb.isOpen():
            self.open_serial_button.setEnabled(False)
            self.close_serial_button.setEnabled(True)

    def port_close(self):
        """ 关闭串口 """
        self.timer_receive.stop()
        try:
            self.serial_uwb.close()
        except:
            pass
        self.open_serial_button.setEnabled(True)
        self.close_serial_button.setEnabled(False)

    def data_receive(self):
        """ 数据接收 """
        try:
            num = self.serial_uwb.inWaiting()
        except:
            self.port_close()
            return None
        if num > 0:
            serial_data = self.serial_uwb.read(num)
            unicode_data = serial_data.decode('iso-8859-1')
            # print(unicode_data)

            data_lines = unicode_data.split('\r\n')  # 列表，一般返回 ma, mc, mr 三个列表

            for line in data_lines:
                data = line.split()
                if len(data) == 10:  # 切断分别为 ma, mc, mr 三个数组
                    # print(data)
                    if data[0] == 'ma':  # 表示基站0到基站x的距离
                        print(data)

                        # MASK=e(0000 1110)表示 RANGE1,RANGE2,RANGE3 都有效， RANGE0无效
                        if data[1] != '0e':
                            print("ma's Range 只有 " + data[1] + " 工作。")
                            # break
                        else:
                            # 16进制转为10进制，距离单位：mm
                            # range_0 = int(data[2],16) #range_0没有'ma'对应的操作说明
                            range_1 = int(data[3], 16)
                            range_2 = int(data[4], 16)
                            # range_3 = int(data[5],16)
                            # print("基站0到基站0的距离：%d"%(range_0)+"，基站0到基站1的距离：%d"%(range_1)+"，基站0到基站2的距离：%d"%(range_2))
                            print("基站0到基站1的距离：%d" % (range_1) +
                                  "，基站0到基站2的距离：%d" % (range_2) + '\n')

                    elif data[0] == 'mc':  # 表示标签x到基站y的距离 (mc：优化过的数据)
                        print(data)
                        # MASK=7(0000 0111)表示 RANGE0,RANGE1,RANGE2 都有效
                        if data[1] != '07':
                            print("mc's Range 只有 " + data[1] + " 工作。")
                            # break
                        else:
                            # 16进制转为10进制，距离单位：mm
                            range_0 = int(data[2], 16)
                            range_1 = int(data[3], 16)
                            range_2 = int(data[4], 16)
                            range_3 = -1
                            count = 3 # 3个基站还是4个基站？

                            print("标签x到基站0的距离：%d" % (range_0) +
                                  "，标签x到基站1的距离：%d" % (range_1) +
                                  "，标签x到基站2的距离：%d" % (range_2) + '\n')

                            anchor = [rc.vec3d(),rc.vec3d(),rc.vec3d(),rc.vec3d()]
                            # anchor_1.x = 3.75  # 单位：米
                            
                            for i in range(4):
                                anchor[i].x = np.float(self.anchorTable.item(i+1,1).text()) # 取 anchorTable 其中 cell 的值
                                anchor[i].y = np.float(self.anchorTable.item(i+1,2).text())
                                anchor[i].z = np.float(self.anchorTable.item(i+1,3).text())


                            # anchor_2.y = 7.5
                            tag_position = rc.vec3d()
                            
                            tag_position = self.getLocation(
                                anchor[0], anchor[1], anchor[2], anchor[3],  range_0, range_1, range_2, range_3, count)
                            
                            print("v = [ %f , %f, %f]" % (tag_position.x, tag_position.y, tag_position.z))

                            self.animation(
                                [tag_position.x, tag_position.y])

        else:
            pass

    def getLocation(self, anchor_0, anchor_1, anchor_2, anchor_3, range_0, range_1, range_2, range_3, count):
        """ 根据trilateration 计算标签的坐标 """
        self.rtls_client = rc.RTLSClient(anchor_0, anchor_1, anchor_2, anchor_3)
        return self.rtls_client.trilaterateTag(range_0, range_1, range_2, range_3, count)

    def init_graphicsView(self):
        """ graphicsView 初始化 """
        axis_x = 375
        axis_y = 750
        w = axis_x
        h = axis_y

        self.rect = QRectF(0, 0, w, h)
        global scene
        scene = QGraphicsScene(self.rect)
        self.graphicsView.setScene(scene)
        scene.addRect(0, 0, w, h)

        # 画坐标系的四个顶点
        ellipse_brush = QBrush(QColor.fromRgb(120, 50, 255))
        scene.addEllipse(
            0-8, 0-8, 15, 15, brush=ellipse_brush)
        scene.addEllipse(
            0-8, h-8, 15, 15, brush=ellipse_brush)
        scene.addEllipse(
            w-8, 0-8, 15, 15, brush=ellipse_brush)
        scene.addEllipse(
            w-8, h-8, 15, 15, brush=ellipse_brush)

        # 画出x, y 轴
        scene.addLine(0, 0, w, 0, pen=QPen(Qt.red))
        scene.addLine(0, 0, 0, h, pen=QPen(Qt.red))

        # 三个基站的位置
        self.anchor_0 = np.array([0, 0], dtype=np.int64)
        self.anchor_1 = np.array([w, 0], dtype=np.int64)
        self.anchor_2 = np.array([0, h], dtype=np.int64)

        global brick_width, brick_height
        brick_width = 1250/10  # 砖长：300mm
        brick_height = 1250/10
        self.brick_gap = 5/10  # 砖间隙：5mm

        global height_num, width_num
        height_num = np.int(self.anchor_2[1]/brick_height)
        width_num = np.int(self.anchor_1[0]/brick_width)

        return w,h # 返回长宽
        
    def graphics(self, robot_point=[0, 0]):
        self.init_graphicsView()
        robot_point[0] = robot_point[0] * 100
        robot_point[1] = robot_point[1] * 100

        global bricks  # 全局
        bricks = np.zeros((width_num*height_num, 5), dtype=int)  # 可利用json数据类型

        """ 砖摆放，从x,y轴出发 """
        for j in range(height_num):
            for i in range(width_num):

                self.brick_x = i*(self.brick_gap+brick_width)
                self.brick_y = j*(self.brick_gap+brick_height)

                bricks[j * width_num + i] = [i, j, self.brick_x,
                               self.brick_y, 0]  # 填写每一块砖的信息
                # print(bricks[i+j])

                rectangle_item = QGraphicsRectItem(
                    self.brick_x, self.brick_y, brick_width, brick_height)
                scene.addItem(rectangle_item)

        print("robot_position: (%d" %
              robot_point[0]+"，%d" % robot_point[1]+")")
        robot_item = QGraphicsEllipseItem(
            robot_point[0], robot_point[1], 10, 10)
        robot_item.setBrush(QBrush(QColor.fromRgb(0, 255, 255)))
        scene.addItem(robot_item)

    def animation(self, robot_point=[0, 0]):
        w,h = self.init_graphicsView()
        robot_point[0] = robot_point[0] * 100
        robot_point[1] = robot_point[1] * 100

        """ 砖摆放，从x,y轴出发 """
        for j in range(height_num):
            for i in range(width_num):

                self.brick_x = i*(self.brick_gap+brick_width)
                self.brick_y = j*(self.brick_gap+brick_height)

                rectangle_item = QGraphicsRectItem(
                    self.brick_x, self.brick_y, brick_width, brick_height)
                
                scene.addItem(rectangle_item)
        # print(bricks)

        # 动态画出铺砖的轨迹
        red_brush = QBrush(QColor.fromRgb(255, 0, 0))
        white_brush = QBrush(QColor.fromRgb(255,255,255))
        for k in range(height_num * width_num):
            if robot_point[0] >= bricks[k][2] and robot_point[0] <= bricks[k][2] + brick_width and robot_point[1] >= bricks[k][3] and robot_point[1] <= bricks[k][3] + brick_height:
                bricks[k][4] = 1
            # else:
            #     bricks[k][4] = 0

        for brick in bricks:  # 铺完一块砖就覆盖颜色
            if brick[4] == 1:
                scene.addRect(brick[2], brick[3], brick_width, brick_height, brush = red_brush)    
            else:
                scene.addRect(brick[2], brick[3], brick_width, brick_height, brush = white_brush)    
            scene.addRect(0, 0, w, h) # 一定要画出最外的矩形区域
            

        robot_item = QGraphicsEllipseItem(
            robot_point[0], robot_point[1], 10, 10)
        robot_item.setBrush(QBrush(QColor.fromRgb(0, 255, 255)))
        scene.addItem(robot_item)

    def wheelEvent(self, event):
        """
            Zoom in or out of the view.
        """
        zoomInFactor = 1.25
        zoomOutFactor = 1 / zoomInFactor

        # Save the scene pos
        oldPos = self.graphicsView.mapToScene(event.pos())
        # print("oldPos：%d" %oldPos[0])

        # Zoom
        if event.angleDelta().y() > 0:
            zoomFactor = zoomInFactor
        else:
            zoomFactor = zoomOutFactor
        self.graphicsView.scale(zoomFactor, zoomFactor)

        # Get the new position
        newPos = self.graphicsView.mapToScene(event.pos())

        # Move scene to old position
        delta = newPos - oldPos
        self.graphicsView.translate(delta.x(), delta.y())



if __name__ == '__main__':
    main_app = QtWidgets.QApplication(sys.argv)

    main_form = Main_Window()
    main_form.show()

    sys.exit(main_app.exec_())
