import sys, os
from .. Service import Service

class ServicesSectionLoader(object):

    def load(self, container, name, config):
        
        if name != 'services':
            return False

        for name in config:
            
            service_def = config[name]
            
            if not 'class' in service_def:
                return False
                
            if 'params' in service_def:
                params = service_def['params']
            else:
                params = []

            # TODO: named parameters
            # TODO: property injection
                
            service = Service(service_def['class'], params)
            container.set_service(name, service)

        return True
