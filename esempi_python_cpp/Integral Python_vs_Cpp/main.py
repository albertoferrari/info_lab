#cppyy is an automatic Python-C++ bindings generator
# for calling C++ from Python
# and Python from C++
import cppyy        
cppyy.include("cpp_integral.cpp")       #C++ -> Python

from cppyy.gbl import cpp_integral      #C++ function
from py_integral import py_integral     #Python function

import time
def main():
    print('C++ start')
    t0 = time.time()
    i = cpp_integral(1, 10, 10_000_000)
    t = time.time() - t0
    print("C++ end   \t",f"val. {i:10.4f}\t time{t:10.4f}")
    
    print('Python start')
    t0 = time.time()
    i = py_integral(1, 10, 10_000_000)
    t = time.time() - t0
    print("Python end\t",f"val. {i:10.4f}\t time{t:10.4f}")

main()
