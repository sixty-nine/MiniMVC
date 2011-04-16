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
            for loader in self.__loaders:
                if loader.load(container, config[item]):
                    continue
            container.set_param(item, config[item])
