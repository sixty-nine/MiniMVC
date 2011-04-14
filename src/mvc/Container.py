import sys, os, yaml
from ObjectFactory import ObjectFactory

class Container:

    def __init__(self):
        self.__dic = {}

    def set(self, key, value):
        if not key in self.__dic:
            #TODO: should we do parameters expansion here?
            self.__dic[key] = value
        else:
            raise ValueError, "Key '%s' already exists in container" % (key)

    def get(self, key):
        if key in self.__dic:
            return self.__dic[key]
        else:
            raise ValueError, "Key '%s' does not exist in container" % (key)

    def load(self, yaml_file):
        if not os.path.exists(yaml_file):
            raise ValueError, "Unexisting file '%s'" % (yaml_file)

        # Load the yaml config
        stream = file(yaml_file, 'r')
        config = yaml.load(stream)
        for item in config:
            self.set(item, config[item])

        # Do parameter expansion
        for key in self.__dic:
            self.__dic[key] = self._expand_parameters(self.__dic[key])

        self._instanciate_services()

    def dump(self):
        print "\n-----( CONTAINER DUMP )--------------------------------------------------------------------------"
        for key in sorted(self.__dic.keys()):
            print key + ':' 
            print '  ', self.__dic[key]
        print "-------------------------------------------------------------------------------------------------\n"

    def _instanciate_services(self):
        # Instanciate services
        if 'services' in self.__dic:
            services = self.get('services')
            #TODO: sort the services to resolve dependencies problems
            list = sorted(services.keys())

            for name in list:
                service_def = services[name]
                if not 'class' in service_def:
                    raise ValueError, "Missing class in service '%s' definition" % (name)

                params = []
                if 'params' in service_def:
                    params_def = service_def['params']
                    for param in params_def:
                        params.append(self._expand_services(param))
                
                self.set(name, ObjectFactory.instantiate(service_def['class'], params))

    def _expand_parameters(self, value):
        if isinstance(value, basestring) and value.startswith('%'):
            # string
            key = value[1:]
            if key in self.__dic:
                return self._expand_parameters(self.__dic[key])
        elif isinstance(value, list):
            # list
            new_value = []
            for item in value:
                new_value.append(self._expand_parameters(item))
            return new_value
        elif isinstance(value, dict):
            # dictionnary
            new_value = {}
            for key in value:
                new_value[key] = self._expand_parameters(value[key])
            return new_value

        return value

    def _expand_services(self, value):
        if isinstance(value, basestring) and value.startswith('@'):
            key = value[1:]
            if key in self.__dic:
                return self.__dic[key]
        return value