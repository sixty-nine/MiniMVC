import os, sys, string
import mimetypes

from MiniMVC import Controller
from MiniMVC.view import CheetahTemplates

class DemoController(Controller):

    def __init__(self, container):
        Controller.__init__(self, container)

    def indexAction(self, request):
        view = self.container.get_service('view')
        request.content_type = "text/html"
        request.write(view.render('index', { }))  
        return True

        
    def helloAction(self, request):
        request.content_type = "text/plain"
        request.write('Hello world !')
        return True
    
    def makoAction(self, request):
        view = self.container.get_service('view')
        request.content_type = "text/html"
        request.write(view.render('hello', { 'subtitle': 'Hello world'}))  
        return True

    def cheetahAction(self, request):
        # Templating engine should not be directly accessed, you should rather get it from the container (see makoAction)
        view = CheetahTemplates(self.container)
        request.content_type = "text/html"
        request.write(view.render('hello', { 'subtitle': 'Hello world'}))
        return True

class ContentController(Controller):

    def __init__(self, container):
        Controller.__init__(self, container)

    def showAction(self, request):

        path = request.parameters['path_info']
        filename = self.container.get_param('sys.basepath') + '/app/public/' + path
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
            return True
        else:
            return False
