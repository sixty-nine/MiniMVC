from __future__ import with_statement
import sys, os, time
from mod_python import apache
from logbook import FileHandler
import cgi

DEBUG = True

basepath = os.path.dirname( os.path.realpath( __file__ ) ) + '/lib'
sys.path.append(basepath)

from MiniMVC import Kernel


def handler(req):

    logger = FileHandler('/tmp/application.log', level='WARNING')

    def inject_info(record, handler):
        pass
    
    with logger.threadbound():
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
    req.write('\n\n----------( DEBUG INFORMATION )----------\n\n')
    req.write( 'Rendering: %0.3f ms\n' % ((t2-t1)*1000.0) )
    req.write('Service container:\n  Parameters\n')
    for name in kernel.container._Container__container:
        req.write("    %s = %s\n" % (name, cgi.escape(str(kernel.container._Container__container[name]))))
    req.write('  Services\n')
    for name in kernel.container._ServiceContainer__container:
        req.write("    %s = %s\n" % (name, cgi.escape(str(kernel.container._ServiceContainer__container[name]))))
    req.write('</pre>')
