# UWB and CAD
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
