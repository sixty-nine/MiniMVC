import os, sys, string
import time
import mimetypes

from mvc import Controller
from mvc import Kernel
from mvc import Daemon
from mvc import CheetahTemplates
from mod_python import apache

class HelloController(Controller):

    def __init__(self, container):
        Controller.__init__(self, container)

    def helloAction(self, request):
            request.content_type = "text/plain"
            request.write(str(request.parameters))
            request.write('Hello world !')
            return apache.OK

class ContentController(Controller):

    CONTENT_BASE_PATH ='/home/dev/pymvc/src/public/'

    def __init__(self, container):
        Controller.__init__(self, container)

    def showAction(self, request):

        path = request.parameters['path_info']
        filename = ContentController.CONTENT_BASE_PATH + '/' + path
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

            request.content_type = mime
            request.write(content)
            return apache.OK
        else:
            return apache.HTTP_NOT_FOUND
