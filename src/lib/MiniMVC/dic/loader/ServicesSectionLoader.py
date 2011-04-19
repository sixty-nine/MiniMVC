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

            named_params = {}
            if 'named_params' in service_def:
                named_params = service_def['named_params']
                
            # TODO: property injection
                
            service = Service(service_def['class'], params, named_params)
            
            if 'persistent' in service_def and isinstance(service_def['persistent'], bool) and service_def['persistent']:
                service.setPersistent(True)
            
            container.set_service(name, service)

        return True
