import sys
from mod_python import apache

basepath = '/home/dev/pymvc/src'
sys.path.append(basepath)
mvc = apache.import_module("mvc")
from mvc import Kernel

def handler(req):
    kernel = Kernel(basepath)
    return kernel.run(req)
