from mako.template import Template
from mako.lookup import TemplateLookup

class MakoTemplates:
    
    def __init__(self, container):
        self.container = container
        
    def render(self, template, params):
        mylookup = TemplateLookup(directories=[self.container.get_param('sys.basepath') + '/app/templates/'])
        mytemplate = mylookup.get_template(template + '.mako')
        return mytemplate.render(**params)
