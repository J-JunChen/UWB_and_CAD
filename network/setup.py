from distutils.core import setup, Extension

module = Extension('_RTLSClient', sources=[
                   'RTLSClient.cpp', "RTLSClient_wrap.cxx","trilateration.cpp"],)

setup(
    name='RTLSClient',
    version='1.0',
    ext_modules=[module],
    py_module=['RTLSClient'],
)
