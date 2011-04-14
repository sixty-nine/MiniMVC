import sys, os
from mod_python import apache

basepath = os.path.dirname( os.path.realpath( __file__ ) )
sys.path.append(basepath)

from mvc import Kernel

def handler(req):
    kernel = Kernel()
    return kernel.run(req)
