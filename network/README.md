## 使用SWIG进行Python和C++的混合编程


### (1)	example.h：头文件
```
#include<iostream>  
using namespace std;  
  
int fact(int n);
```

### (2)	example.cpp : 源文件（主要实现的功能是阶乘）
```
#include "example.h"  
  
int fact(int n){   
    if (n < 0){  
        return 0;  
    }  
    if (n == 0){  
        return 1;  
    }  
    else{  
        return n * fact(n-1);  
    }  
}  
```

### (3)	example.i ：接口文件 
(interface file 包含了ANSI C 的函数原型和变量声明；
%module指令定义了将被SWIG创建的模块的名称；
%{ %}这一块为了生成混编代码而提供了插入额外代码的定位，例如C++的头文件、C/C++额外声明)
```
%module example  
  
%{  
#include "example.h"  
%}  

%include "example.h"  
```

通过SWIG的命令：```$ swig -c++ -python example.i``` 接口文件，
创建 example.py 和 example_wrap.cxx 文件，其中 example.py 就是 C++ 功能的 Python 实现文件。

### (4)	setup.py 文件
setup操作就是利用distutils这个库来创建你的包，其中需要的是数据就是在setup.py填写的文件。
```
from distutils.core import setup, Extension  # 加入混合编程需要的库  
  
example_module = Extension("_example",sources=["example.cpp","example_wrap.cxx",],) # 源文件模块  
  
setup(name='example',   
    version='0.1', # 版本号  
    author='Jun', # 作者名字  
    description="""Simple swig example from docs""", # 描述  
    ext_modules=[example_module],   
    py_modules=['example'], # Python模块  
)  
```
最后，利用命令：```$ python setup.py build_ext --inplace``` 将创建 C++ 的动态链接库，
最后 Python 便能够调用所创建的包。

测试 example 模块是否存在：```$ python -c 'import example'```

