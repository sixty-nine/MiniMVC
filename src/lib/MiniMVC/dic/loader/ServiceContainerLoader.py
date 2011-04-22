import sys, os, yaml

class ServiceContainerLoader(object):
    
    def __init__(self):
        self.__loaders = []
    
    def register_section_loader(self, loader):
        if not loader in self.__loaders:
            self.__loaders.append(loader)
    
    def load(self, container, yamlfile):
    
        if not os.path.exists(yamlfile):
            raise ValueError, "Unexisting file '%s'" % (yamlfile)

        stream = file(yamlfile, 'r')
        config = yaml.load(stream)
        for item in config:
            handled = False
            for loader in self.__loaders:
                handled = loader.load(container, item, config[item])
                if handled: break
            
            if not handled:
                container.set_param(item, config[item])
#
# This file is part of the MiniMVC package
#
# (c) dreamcraft.ch
#
# This source file is subject to the MIT license that is bundled
# with this source code in the file LICENSE.
#

import sys, os, yaml

class ServiceContainerLoader(object):
    
    def __init__(self):
        self.__loaders = []
    
    def register_section_loader(self, loader):
        if not loader in self.__loaders:
            self.__loaders.append(loader)
    
    def load(self, container, yamlfile):
    
        if not os.path.exists(yamlfile):
            raise ValueError, "Unexisting file '%s'" % (yamlfile)

        stream = file(yamlfile, 'r')
        config = yaml.load(stream)
        for item in config:
            handled = False
            for loader in self.__loaders:
                handled = loader.load(container, item, config[item])
                if handled: break
            
            if not handled:
                container.set_param(item, config[item])
