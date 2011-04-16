class ObjectFactory(object):

    @staticmethod
    def instantiate(full_class_name, params):
        cls = ObjectFactory.get_class(full_class_name)
        if callable(cls):
            return cls(*params)
        else:
            raise ValueError, "The class is not callable"

    @staticmethod
    def instantiate_and_call(full_class_name, constructor_params, function_name, function_params):
        inst = ObjectFactory.instantiate(full_class_name, constructor_params)
        func = getattr(inst, function_name)
        return func(function_params)
            
            
    @staticmethod
    def get_class(full_class_name):
        if full_class_name.find('.') != -1:
            parts = full_class_name.split('.')
        else:
            parts = ['__main__', full_class_name]

        #print parts, parts[:-1], parts[-1:]
        
        module = ".".join(parts[:-1])
        for comp in parts[-1:]:
            m = __import__(module, globals(), locals(), [comp], -1)
            c = getattr(m , comp)
        return c

    @staticmethod
    def get_class_from_name(full_class_name):
        (module_name, class_name) = ObjectFactory.parse_class_name(full_class_name)
        module = ObjectFactory.import_module(module_name)
        cls = ObjectFactory.get_module_class(module, class_name)
        return (module, cls)

    @staticmethod
    def parse_class_name(full_class_name):
        if full_class_name.find('.') != -1:
            parts = full_class_name.split('.')
        else:
            parts = ['__main__', full_class_name]
        module = ".".join(parts[:-1])
        cls = parts[-1]
        return (module, cls)

    @staticmethod
    def import_module(module_name):
        return __import__(module_name, globals(), locals(), [], -1)

    @staticmethod
    def get_module_class(module, class_name):
        return getattr(module, class_name)
