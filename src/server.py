#!/usr/bin/python
import os, sys, string
import time
import mimetypes

from mvc import Controller
from mvc import Kernel
from mvc import Daemon
from mvc import CheetahTemplates

class HelloController(Controller):

    def __init__(self, container):
        Controller.__init__(self, container)

    def helloAction(self, params):
        self.header(200, 'text/plain')
        self.output('Hello world')

class ContentController(Controller):

    CONTENT_BASE_PATH = sys.path[0] + '/public/'

    def __init__(self, container):
        Controller.__init__(self, container)

    def showAction(self, params):

        filename = ContentController.CONTENT_BASE_PATH + '/' + params['path_info']
        if os.access(filename, os.R_OK) and not os.path.isdir(filename):
            #TODO: is there any possibility to access files outside the root with ..?
            file = open(filename, "r")
            content = file.read()
            file.close()

            mime = mimetypes.guess_type(filename)
            if mime[0]: 
                mime = mime[0] 
            else: 
                mime = 'text/plain'

            self.header(200, mime)
            self.output(content)
        else:
            self.error404()


class MyDaemon(Daemon):

    def __init__(self, pidfile):
        logfile =  sys.path[0] + '/log/server.log'
        if not os.path.exists(logfile):
            file = open(logfile, 'w')
            file.write('')
            file.close()

        super(MyDaemon, self).__init__(pidfile, logfile, logfile, logfile)
        self.kernel = Kernel()

    def run(self):
        self.kernel.start()
        while True:
            time.sleep(1)


#DEBUG CODE:
kernel = Kernel()
kernel.run()
sys.exit(0)


if __name__ == '__main__':
    daemon = MyDaemon('/tmp/torrent-server.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            print 'Starting server'
            daemon.start()
            sys.exit(0)
        elif 'stop' == sys.argv[1]:
            print 'Stoping server'
            daemon.stop()
            sys.exit(0)
        elif 'restart' == sys.argv[1]:
            print 'Restarting server'
            daemon.restart()
            sys.exit(0)
        elif 'status' == sys.argv[1]:
            if daemon.is_running():
                print 'Daemon running'
            else:
                print 'Daemon not running'
            sys.exit(0)

    print "usage: %s start|stop|restart|status" % sys.argv[0]
    sys.exit(2)
