import sys
from mod_python import apache

basepath = '/home/dev/pymvc/src'
sys.path.append(basepath)

from mvc import Kernel

def handler(req):
    kernel = Kernel(basepath)
    return kernel.run(req)
