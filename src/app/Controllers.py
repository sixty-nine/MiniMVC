import os, sys, string
import mimetypes
from mod_python import apache

from MiniMVC import Controller
from MiniMVC import CheetahTemplates

class DemoController(Controller):

    def __init__(self, container):
        Controller.__init__(self, container)

    def helloAction(self, request):
        request.content_type = "text/plain"
        request.write('Hello world !')
        return apache.OK
    
    def makoAction(self, request):
        view = self.container.get('view')
        request.content_type = "text/html"
        request.write(view.render(self.container.get('basepath') + '/app/templates/hello', { 'subtitle': 'Hello world'}))  
        return apache.OK

    def cheetahAction(self, request):
        # Templating engine should not be directly accessed, you should rather get it from the container (see makoAction)
        view = CheetahTemplates
        request.content_type = "text/html"
        request.write(view.render(self.container.get('basepath') + '/app/templates/hello', { 'subtitle': 'Hello world'}))
        return apache.OK

class ContentController(Controller):

    def __init__(self, container):
        Controller.__init__(self, container)

    def showAction(self, request):

        path = request.parameters['path_info']
        filename = self.container.get('basepath') + '/app/public/' + path
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
