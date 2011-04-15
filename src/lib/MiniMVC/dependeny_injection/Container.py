class Container:

    def __init__(self):
        self.__dic = {}
        self.__services = {}

    def set(self, key, value):
        if not key in self.__dic:
            self.__dic[key] = value
        else:
            raise ValueError, "Key '%s' already exists in container" % (key)

    def get(self, key):
        if key in self.__dic:
            return self._expand_parameters(self.__dic[key])
        else:
            raise ValueError, "Key '%s' does not exist in container" % (key)

    def dump(self):
        print "\n-----( CONTAINER DUMP )--------------------------------------------------------------------------"
        print "----- PARAMETERS"
        for key in sorted(self.__dic.keys()):
            print key + ':' 
            print '  ', self.__dic[key]
        print "----- SERVICES"
        for key in sorted(self.__services.keys()):
            print key + ':'
            print '  ', self.__services[key]
        print "-------------------------------------------------------------------------------------------------\n"

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

