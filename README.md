# UWB and CAD
## 上位机软件工作图
![image](https://github.com/J-JunChen/UWB_and_CAD/blob/master/framework.gif)

涉及技术：Python + PyQt5 + OpenCV + 混合编程

项目背景：帮助远程操作员通过上位机与铺砖机器人实现通信，并在上位机中观察机器人在房间中的实时定位和砖块铺设情况反馈。

技术要点：

- 利用 OpenCV 库函数对 CAD 工程图纸进行房间区域的划分，解决了人工手动划分的困难。

- 利用角点定位排序法实现将房间区域等比例地绘制到 Qt 界面上，解决了人工手动绘制的问题，实现了自动化处理工程图的效果。

- 利用 serial 函数库实现与机器人的通信，并结合超宽带(UWB)定位技术计算出机器人在房间中的实时位置，并绘制在上位机中，协助远程操作员观察机器人在上位机中的模拟位置。[Serial Module](https://github.com/J-JunChen/UWB_and_CAD/blob/master/model/Serial.py)

- 利用混合编程技术实现将定位算法集成到 C++ 文件中，缓解了 Python 语言执行效率低的问题，带来了机器人实时定位的效果。


## 配置python3.6环境
- 1、修改conda的源
```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
```

- 2、修改pip全局源，修改 ~/.pip/pip.conf (没有就创建一个)
```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

## 安装相应的Python库
- 1、配置OpenCV
``` 
pip install opencv-python==3.4.4.19
```

- 2、配置Wand
```
pip install Wand==0.4.4
```
其中pdf读取出现问题，error：412时，解决方案如下：
--> I fixed it for me by editing the /etc/ImageMagick-6/policy.xml and changed the rights for the pdf line to "read":
```
<policy domain="coder" rights="read" pattern="PDF" />
```

- 3、配置PyQt5
```
pip install PyQt5
```

- 4、配置pyserial
```
pip install pyserial
```

配置完后以后，需要给予串口(ttyACM0) 权限
```
sudo chmod a+rw /dev/ttyACM0 
```

- 5、配置numpy
