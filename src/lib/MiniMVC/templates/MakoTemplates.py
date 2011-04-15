from mako.template import Template

class MakoTemplates:
    
    @staticmethod
    def render(template, params):
        return Template(filename = template + '.mako').render(**params)