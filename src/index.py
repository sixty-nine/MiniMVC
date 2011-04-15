import sys, os
from mod_python import apache

basepath = os.path.dirname( os.path.realpath( __file__ ) ) + '/lib'
sys.path.append(basepath)

from MiniMVC import Kernel

def handler(req):
    kernel = Kernel()
    return kernel.run(req)
