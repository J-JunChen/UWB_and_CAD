import sys
import os
import numpy as np
import cv2 as cv

import serial
import serial.tools.list_ports

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QPushButton, QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsRectItem, QGraphicsEllipseItem, QTableWidgetItem, QFileDialog
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, pyqtSlot, QObject, QRectF, QPoint
from PyQt5.QtGui import QBrush, QPen, QColor, QPixmap, QPolygonF

from Ui_MainWindow import Ui_MainWindow

dir_path = os.path.dirname(os.path.realpath(__file__))  # 获取当前路径
former_path = dir_path[:dir_path.rfind('/')]
sys.path.append(former_path+'/network')  # ui视图层
sys.path.append(former_path+'/cad') # cad操作层

import RTLSClient as rc
import Pdf2img
import Analyse_Img as ai


class Main_Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main_Window, self).__init__(parent=parent)
        self.setupUi(self)

        self.init_anchor()
        self.init_vertex()
        self.init_brick()

        self.init_serial()
        self.setWindowTitle("UWB串口助手")
        self.serial_uwb = serial.Serial()
        self.port_check()

        self.graphicsView.scale(1,-1) # x轴倒转
        self.init_graphicsView()
        # self.graphics()

        self.setMouseTracking(True)
        self.graphicsView.setMouseTracking(True)
        print(self.graphicsView.hasMouseTracking())

        self.choose_pdf_Button.clicked.connect(self.choose_pdf_Button_clicked) # 点击”选择PDF文件“
        self.analyse_button.clicked.connect(self.analyse_button_clicked) # 点击“数据分析”
        self.comboBox.activated.connect(self.load_room) # “房间选择”被激活时候的处理
        self.left_Button.clicked.connect(self.left_Button_clicked) # 点击"左转"按钮事件
        self.right_Button.clicked.connect(self.right_Button_clicked) # 点击"右转"按钮事件
        self.confirm_Button.clicked.connect(self.confirm_Button_clicked) # 点击"确认"按钮

        # self.vertexTable.itemChanged.connect(self.graphics)
        self.anchorTable.itemChanged.connect(self.graphics)
   
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

    def init_anchor(self, points = None):
        """ 初始化基站 """
        self.anchorTable.setHorizontalHeaderItem(0, QTableWidgetItem("基站编号"))
        self.anchorTable.setHorizontalHeaderItem(1, QTableWidgetItem("X轴 / m"))
        self.anchorTable.setHorizontalHeaderItem(2, QTableWidgetItem("Y轴 / m"))
        self.anchorTable.setHorizontalHeaderItem(3, QTableWidgetItem("Z轴 / m"))

        self.anchorTable.setItem(0,0, QTableWidgetItem("anchor_0"))
        self.anchorTable.setItem(1,0, QTableWidgetItem("anchor_1"))
        self.anchorTable.setItem(2,0, QTableWidgetItem("anchor_2"))
        self.anchorTable.setItem(3,0, QTableWidgetItem("anchor_3"))

        # 初始化anchor_0的X,Y,Z轴
        self.anchorTable.setItem(0,1, QTableWidgetItem("0.0"))
        self.anchorTable.setItem(0,2, QTableWidgetItem("0.0"))
        self.anchorTable.setItem(0,3, QTableWidgetItem("1.5"))

        # 初始化anchor_1的X,Y,Z轴
        self.anchorTable.setItem(1,1, QTableWidgetItem("3.75"))
        self.anchorTable.setItem(1,2, QTableWidgetItem("0.0"))
        self.anchorTable.setItem(1,3, QTableWidgetItem("1.5"))

        # 初始化anchor_2的X,Y,Z轴
        self.anchorTable.setItem(2,1, QTableWidgetItem("0.0"))
        self.anchorTable.setItem(2,2, QTableWidgetItem("7.5"))
        self.anchorTable.setItem(2,3, QTableWidgetItem("1.5"))

        # 初始化anchor_3的X,Y,Z轴
        self.anchorTable.setItem(3,1, QTableWidgetItem("0.0"))
        self.anchorTable.setItem(3,2, QTableWidgetItem("0.0"))
        self.anchorTable.setItem(3,3, QTableWidgetItem("1.5"))

        if points != None: # 用图像的像素来填充
            self.anchorTable.setItem(1,1, QTableWidgetItem(str(points[1])))
            self.anchorTable.setItem(2,2, QTableWidgetItem(str(points[0])))

    def init_vertex(self, points = None):
        """ 初始化顶点 """
        self.vertexTable.setHorizontalHeaderItem(0, QTableWidgetItem("顶点编号"))
        self.vertexTable.setHorizontalHeaderItem(1, QTableWidgetItem("X轴 / mm"))
        self.vertexTable.setHorizontalHeaderItem(2, QTableWidgetItem("Y轴 / mm"))
        self.vertexTable.setHorizontalHeaderItem(3, QTableWidgetItem("Z轴 / mm"))
        if points is None:
            row_count = self.vertexTable.rowCount()
            for i in range(row_count):
                self.vertexTable.setItem(i, 0, QTableWidgetItem("vertex_"+str(i)))
                self.vertexTable.setItem(i, 1, QTableWidgetItem("0.0"))
                self.vertexTable.setItem(i, 2, QTableWidgetItem("0.0"))
                self.vertexTable.setItem(i, 3, QTableWidgetItem("0.0"))
        else:
            self.vertexTable.clearContents()
            self.vertexTable.setRowCount(len(points)) 
            for i in range(len(points)):
                print(points[i])
                self.vertexTable.setItem(i, 0, QTableWidgetItem("vertex_"+str(i)))
                self.vertexTable.setItem(i, 1, QTableWidgetItem(str(int(points[i][0]))))
                self.vertexTable.setItem(i, 2, QTableWidgetItem(str(int(points[i][1]))))
                self.vertexTable.setItem(i, 3, QTableWidgetItem("0.0"))
            self.graphics() # QT绘制区域
            

    def init_brick(self):
        """ 初始化砖块信息 """
        self.brickTable.setHorizontalHeaderItem(0, QTableWidgetItem("砖块编号"))
        self.brickTable.setHorizontalHeaderItem(1, QTableWidgetItem("X轴 / mm"))
        self.brickTable.setHorizontalHeaderItem(2, QTableWidgetItem("y轴 / mm"))
        self.brickTable.setHorizontalHeaderItem(3, QTableWidgetItem("已完成？"))
        self.brickTable.setHorizontalHeaderItem(4, QTableWidgetItem("取消"))

        row_count = self.brickTable.rowCount() # 砖列表行数


        for i in range(row_count):
            chkBoxItem = QTableWidgetItem()
            chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
            self.brickTable.setItem(i, 4, chkBoxItem)

        self.brickTable.itemClicked.connect(self.handleItemClicked)
        self._list = []

        for i in range(row_count):
            self.brickTable.setItem(i , 0, QTableWidgetItem("brick_" + str(i)))
            self.brickTable.setItem(i , 1, QTableWidgetItem("0.0"))
            self.brickTable.setItem(i , 2, QTableWidgetItem("0.0"))
            self.brickTable.setItem(i , 3, QTableWidgetItem("0"))


    def handleItemClicked(self, item):
        """ 点击取消按钮 """
        if item.checkState() == QtCore.Qt.Checked:
            print('"%s" checked' % item.text())
            self._list.append(item.row())
            print(self._list)
        else:
            print('"%s" Clicked' % item.text())

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

        # sudo chmod a+rw /dev/ttyACM0 #给予权限

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
                                anchor[i].x = np.float(self.anchorTable.item(i,1).text()) # 取 anchorTable 其中 cell 的值
                                anchor[i].y = np.float(self.anchorTable.item(i,2).text())
                                anchor[i].z = np.float(self.anchorTable.item(i,3).text())


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
        """ 
            graphicsView 初始化 ：
            1、画出基站矩阵
            2、画出角点位置，将角点按顺时针连接
        """
        global scene
        scene = QGraphicsScene()
        self.graphicsView.setScene(scene)
        
        anchor = np.zeros((4,3), dtype=float) # anchor_1.x = 3.75  # 单位：米

        for i in range(4):
            anchor[i][0] = np.float(self.anchorTable.item(i,1).text()) * 100 # 取 anchorTable 其中 cell 的值
            anchor[i][1] = np.float(self.anchorTable.item(i,2).text()) * 100
            anchor[i][2] = np.float(self.anchorTable.item(i,3).text()) * 100

        # -------- 画出基站的四个顶点 ---------#
        anchor_brush = QBrush(QColor.fromRgb(120, 50, 255))
        for i in range(4):
            scene.addEllipse(
                anchor[i][0]-8, anchor[i][1]-8, 15, 15, brush=anchor_brush)

        origin_x = anchor[0][0]
        origin_y = anchor[0][1]
        axis_x = anchor[1][0]
        axis_y = anchor[2][1]
        
        # ------- 画出 基站区域 --------#
        scene.addLine(origin_x, origin_y, axis_x,  anchor[1][1], pen=QPen(Qt.green))
        scene.addLine(origin_x, origin_y,  anchor[2][0], axis_y, pen=QPen(Qt.green))

        # ------- 画出x, y 轴 ---------#
        scene.addLine(origin_x, origin_y, axis_x + 20, origin_y, pen=QPen(Qt.red, 4))
        scene.addLine(origin_x, origin_y, origin_x, axis_y + 20, pen=QPen(Qt.red, 4))

        triangle_0 = [
            QPoint(origin_x - 10, axis_y+ 20),
            QPoint(origin_x, axis_y +30),
            QPoint(origin_x + 10 , axis_y+ 20)
        ] # Y轴顶上三角形

        triangle_1 = [
            QPoint(axis_x + 20, origin_y - 10),
            QPoint(axis_x + 30, origin_y),
            QPoint(axis_x + 20, origin_y + 10)
        ] # X轴顶上三角形

        scene.addPolygon(QPolygonF(triangle_0), pen=QPen(Qt.red, 4), brush=QBrush(Qt.red, Qt.SolidPattern))
        scene.addPolygon(QPolygonF(triangle_1), pen=QPen(Qt.red, 4), brush=QBrush(Qt.red, Qt.SolidPattern))

        # ------ 再画出所有角点------- # 
        row_count = self.vertexTable.rowCount()
        vertex = np.zeros((row_count,3), dtype=float) 
        # print("row count: " + str(row_count))

        for i in range(row_count):
            vertex[i][0] = np.float(self.vertexTable.item(i,1).text()) / 10  # 取 vertexrTable 其中 cell 的值
            vertex[i][1] = np.float(self.vertexTable.item(i,2).text()) / 10
            vertex[i][2] = np.float(self.vertexTable.item(i,3).text()) / 10

        vertex_brush = QBrush(QColor.fromRgb(250, 244, 8)) # 红(250) 绿(244) 蓝(8)
        for i in range(row_count):
            scene.addEllipse(
                vertex[i][0]-4, vertex[i][1]-4, 8, 8, brush=vertex_brush)
            if i != row_count -1 :
                scene.addLine(vertex[i][0], vertex[i][1], vertex[i+1][0], vertex[i+1][1], pen=QPen(Qt.blue))
            else:
                scene.addLine(vertex[i][0], vertex[i][1], vertex[0][0], vertex[0][1], pen=QPen(Qt.blue))

        # 再画出砖块
        global brick_width, brick_height
        brick_width = int(self.brick_width_textEdit.toPlainText()) / 10  # 砖长：300mm
        brick_height = int(self.brick_length_textEdit.toPlainText()) / 10
        self.brick_gap = int(self.brick_gap_textEdit.toPlainText()) / 10 # 砖间隙：5mm

        global height_num, width_num
        height_num = np.int(axis_y/brick_height)
        width_num = np.int(axis_x/brick_width)

        return axis_x, axis_y # 返回长宽

    def graphics(self):
        self.init_graphicsView()
        robot_point=[0, 0]
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
                print(bricks[i+j])

                rectangle_item = QGraphicsRectItem(
                    self.brick_x, self.brick_y, brick_width, brick_height)
                
                rectangle_item.setPen(Qt.gray) # setPen:画笔画边框；setBrush:画刷画填充
                scene.addItem(rectangle_item)

                self.brickTable.setItem(j * width_num + i , 0, QTableWidgetItem("brick_" + str(j * width_num + i)))
                self.brickTable.setItem(j * width_num + i , 1, QTableWidgetItem(str(self.brick_x)))
                self.brickTable.setItem(j * width_num + i , 2, QTableWidgetItem(str(self.brick_y)))
                self.brickTable.setItem(j * width_num + i , 3, QTableWidgetItem("0"))

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
                self.brickTable.setItem(k, 3, QTableWidgetItem("1"))
            # else:
            #     bricks[k][4] = 0

        for brick in bricks:  # 铺完一块砖就覆盖颜色
            if brick[4] == 1:
                scene.addRect(brick[2], brick[3], brick_width, brick_height, brush = red_brush)
            else:
                scene.addRect(brick[2], brick[3], brick_width, brick_height, brush = white_brush)
            # scene.addRect(0, 0, w, h) # 一定要画出最外的矩形区域


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

    def choose_pdf_Button_clicked(self):
        """
            选择PDF文件按钮事件
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileRoad, _ = QFileDialog.getOpenFileName(
            self,
            "选择CAD文件",
            "",
            "PDF Files (*.pdf) ;; JPG Files (*.jpg)",
            options=options)
        if fileRoad:
            fileName = os.path.split(fileRoad)[1]  #分离文件名
            self.cad_label.setText("图纸名称：" + fileName)  #修改label 的text
            # self.load_image(fileRoad)
        pictureName = Pdf2img.pdf2img(fileName)
        src = cv.imread(pictureName)
        resizeName = ai.resize(src, 0.47)
        src = cv.imread(resizeName)
        cutName = ai.cut_picture_roi(src)
        self.load_image(cutName, self.drawing_label)

    def load_image(self, image, image_label):
        """
            加载图片：
                1、每次load_image，就清空原来的label.clear()
                2、setPixmap(pixmap.scaled(size(),KeepAsceptRatio))表示按图像比例显示
        """
        # image_label = self.room_label
        image_label.clear() #每次选择
        pixmap = QPixmap(image)

        image_label.setAlignment(QtCore.Qt.AlignCenter)
        image_label.setPixmap(
            pixmap.scaled(image_label.size(),
                          QtCore.Qt.KeepAspectRatio))  #radio：根据图像比例显示图片

    def analyse_button_clicked(self):
        """ 数据分析 """
        src = cv.imread('./cut.jpg')
        num = self.room_num_textEdit.toPlainText()
        # ai.find_contours(src, room_num = int(num))

        self.comboBox.clear()
        
        for i in range(int(num)):
            self.comboBox.addItem(self.tr('contour_' + str(i)))
        self.load_room()
    
    def load_room(self):
        room_name = self.comboBox.currentText()
        # if room
        self.load_image(room_name+'.jpg', self.room_label)
        print(room_name)

    def left_Button_clicked(self):
        room_name = self.comboBox.currentText() + '.jpg'
        src = cv.imread(room_name)
        ai.rotate_picture(src, img_name = room_name, rotate_direction = 'l')
        self.load_image(room_name, self.room_label) # 再显示出来

    def right_Button_clicked(self):
        room_name = self.comboBox.currentText() + '.jpg'
        src = cv.imread(room_name)
        ai.rotate_picture(src, img_name = room_name, rotate_direction = 'r')
        self.load_image(room_name, self.room_label) # 再显示出来

    def confirm_Button_clicked(self):
        """ 点击“确认“按钮，就会传递角点参数给 QgraphicsView 控件，进行绘图 """
        room_name = self.comboBox.currentText() + '.jpg'
        src = cv.imread(room_name)
        

        lines = ai.line_detect(src)
        points, pnum = ai.point_detection(src)
        adjacency_matrix = ai.create_adjacency_matrix(points, pnum, lines)
        clockwise, points = ai.points_sort(adjacency_matrix, points, pnum)
        points = ai.points_adjust_row_and_col(points, pnum)

        ratio = int(self.ratio_textEdit.toPlainText())
        dot_pitch = float(self.dot_pitch_textEdit.toPlainText()) # 0.1815

        points = ai.points_to_real_distance(points, pnum, ratio, dot_pitch)
        # ai.max_area_object_measure(src)
        self.init_vertex(points)
        
        src_height = round(src.shape[0] * ratio * dot_pitch / 1000, 2)
        src_width = round(src.shape[1] * ratio * dot_pitch / 1000, 2)
        self.init_anchor([src_height, src_width]) #图片像素点长宽填充

    def dpi_setting(self):
        print("dpi_setting")
    

if __name__ == '__main__':
    main_app = QtWidgets.QApplication(sys.argv)

    main_form = Main_Window()
    main_form.show()

    sys.exit(main_app.exec_())
