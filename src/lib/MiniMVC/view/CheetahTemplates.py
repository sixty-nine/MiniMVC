from Cheetah.Template import Template

class CheetahTemplates(object):
    
    def __init__(self, container):
        self.container = container

    def render(self, template, params):
        return str(Template ( file = self.container.get_param('sys.basepath') + '/app/templates/' + template + '.cheetah', searchList = [params] ))
