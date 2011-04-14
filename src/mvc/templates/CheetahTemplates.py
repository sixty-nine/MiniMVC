from Cheetah.Template import Template

class CheetahTemplates:
    
    @staticmethod
    def render(template, params):
        return Template ( file =template + '.cheetah', searchList = [params] )