import sys, os, yaml
from Service import Service

class ServiceContainerLoader(object):
    
    @staticmethod
    def load(container, yamlfile):
    
        if not os.path.exists(yamlfile):
            raise ValueError, "Unexisting file '%s'" % (yamlfile)

        stream = file(yamlfile, 'r')
        config = yaml.load(stream)
        for item in config:
            if item == 'services':
                ServiceContainerLoader._load_services(container, config[item])
            else:
                container.set_param(item, config[item])

    @staticmethod
    def _load_services(container, config):
        
        for name in config:
            
            service_def = config[name]
            
            if not 'class' in service_def:
                raise ValueError, "No class defined in service definition '%s'" % (name)
                
            if 'params' in service_def:
                params = service_def['params']
            else:
                params = []
                
            service = Service(service_def['class'], params)
            container.set_service(name, service)


