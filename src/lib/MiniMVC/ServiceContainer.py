from Service import Service

class ServiceContainer(object):
    
    def __init__(self):
        self.__container = {}

    def set_service(self, name, service_def):
        if not isinstance(service_def, Service):
            raise ValueError, "The definition of '%s' is not a Service" % (name)
        if not name in self.__container:
            self.__container[name] = service_def
        else:
            raise ValueError, "Service '%s' already exists in container" % (name)

    def get_service(self, name):
        if name in self.__container:
            return self._get_instance(name, [])
        else:
            raise ValueError, "Service '%s' does not exist in container" % (name)

    def _get_instance(self, name, to_instantiate):
        service_def = self.__container[name]
        
        # Instanciate the dependencies
        for dependency in service_def.dependencies:

            if not dependency in self.__container:
                raise ValueError, "Dependency '%s' of service '%s' does not exist" % (dependency, name)
            if dependency in to_instantiate:
                raise ValueError, "Circular dependency detected '%s', stack = %s" % (dependency, str(to_instantiate))

            to_instantiate.append(dependency)
            self._get_instance(dependency, to_instantiate)

        # Instanciate the service
        if service_def.is_persistent and service_def.instance != None:
            return service_def.instance
        else:
            if callable(service_def.cls):
                params = []
                for param in service_def.constructor_params:
                    if isinstance(param, basestring) and param.startswith('@'):
                        params.append(self.get_service(param[1:]))
                    else:
                        params.append(param)
                        
                service_def.instance = service_def.cls(*params)
                return service_def.instance
        
        raise ValueError, "Impossible to instantiate service '%s'" % (service_def.full_class_name)