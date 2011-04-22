from Cheetah.Template import Template

class CheetahTemplates(object):
    
    def __init__(self, container):
        self.container = container

    def render(self, template, params):
        return str(Template ( file = self.container.get_param('sys.basepath') + '/app/templates/' + template + '.cheetah', searchList = [params] ))
#
# This file is part of the MiniMVC package
#
# (c) dreamcraft.ch
#
# This source file is subject to the MIT license that is bundled
# with this source code in the file LICENSE.
#

from Cheetah.Template import Template

class CheetahTemplates(object):
    
    def __init__(self, container):
        self.container = container

    def render(self, template, params):
        return str(Template ( file = self.container.get_param('sys.basepath') + '/app/templates/' + template + '.cheetah', searchList = [params] ))
