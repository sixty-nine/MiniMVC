from MiniMVC.ObjectFactory import ObjectFactory

class Service(object):

    def __init__(self, full_class_name, constructor_params, constructor_named_params = {}):
        (module, cls) = ObjectFactory.get_class_from_name(full_class_name)
        self.full_class_name = full_class_name
        self.module = module
        self.cls = cls
        self.constructor_params = constructor_params
        self.constructor_named_params = constructor_named_params
        self.is_persistent = False
        self.instance = None

        # Calculate the dependencies
        self.dependencies = []
        if constructor_params:
            for param in constructor_params:
                if isinstance(param, basestring) and param.startswith('@'):
                    self.dependencies.append(param[1:])

        if constructor_named_params:
            for param in constructor_named_params:
                value = constructor_named_params[param]
                if isinstance(value, basestring) and value.startswith('@'):
                    self.depenendencies.append(value[1:])

    def setPersistent(self, flag):
        self.is_persistent = flag

    def __str__(self):
        return self.full_class_name + "(" + str(self.constructor_params) + ', ' + str(self.constructor_named_params) + ")"
