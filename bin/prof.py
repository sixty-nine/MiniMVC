#!/usr/bin/python
import os, sys
import profile

basepath = os.path.realpath(os.path.dirname( os.path.realpath( __file__ )) + '/../src/lib')
sys.path.append(basepath)

from MiniMVC import Kernel

def main():
  kernel = Kernel()

profile.run('main()', 'profile.prof')

import pstats
pstats.Stats('profile.prof').sort_stats('cumulative').print_stats('/home/dev/pymvc/src/lib/')
