#
# This file is part of the MiniMVC package
#
# (c) dreamcraft.ch
#
# This source file is subject to the MIT license that is bundled
# with this source code in the file LICENSE.
#

from __future__ import with_statement
import sys, os, time
from mod_python import apache
import logbook
import cgi

DEBUG = True

basepath = os.path.dirname( os.path.realpath( __file__ ) ) + '/lib'
sys.path.append(basepath)

from MiniMVC import Kernel


def handler(req):

    def inject_info(record, handler):
        pass
    
    if DEBUG: t1 = time.time()
    kernel = Kernel()
    res = kernel.run(req)
    if DEBUG: t2 = time.time()
    if res:
        if DEBUG: show_debug_info(req, t1, t2, kernel)
        return apache.OK
    else:
        return apache.HTTP_NOT_FOUND

def show_debug_info(req, t1, t2, kernel):
    req.write('<pre>')
    req.write('\n\n----------( DEBUG INFORMATION )----------\n')
    req.write( '\n>>> Rendering: %0.3f ms\n' % ((t2-t1)*1000.0) )
    req.write('\n>>> Service container:\n\n  Parameters\n')
    for name in sorted(kernel.container._Container__container.keys()):
        req.write("    %s = %s\n" % (name, cgi.escape(str(kernel.container._Container__container[name]))))
    req.write('\n  Services\n')
    for name in sorted(kernel.container._ServiceContainer__container.keys()):
        req.write("    %s = %s\n" % (name, cgi.escape(str(kernel.container._ServiceContainer__container[name]))))
    req.write('\n>>> Request log:\n\n')
    for log in kernel.request_log:
        req.write('  %s - %s - %s\n' % (log.time, logbook.base._level_names[log.level], log.msg)) 
    req.write('</pre>')
