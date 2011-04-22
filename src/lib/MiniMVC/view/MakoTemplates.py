from mako.template import Template
from mako.lookup import TemplateLookup

class MakoTemplates(object):
    
    def __init__(self, container):
        self.container = container
        
    def render(self, template, params):
        mylookup = TemplateLookup(directories=[self.container.get_param('sys.basepath') + '/app/templates/'])
        mytemplate = mylookup.get_template(template + '.mako')
        return mytemplate.render(**params)
#
# This file is part of the MiniMVC package
#
# (c) dreamcraft.ch
#
# This source file is subject to the MIT license that is bundled
# with this source code in the file LICENSE.
#

from mako.template import Template
from mako.lookup import TemplateLookup

class MakoTemplates(object):
    
    def __init__(self, container):
        self.container = container
        
    def render(self, template, params):
        mylookup = TemplateLookup(directories=[self.container.get_param('sys.basepath') + '/app/templates/'])
        mytemplate = mylookup.get_template(template + '.mako')
        return mytemplate.render(**params)
