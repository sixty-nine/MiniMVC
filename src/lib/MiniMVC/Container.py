import sys, os
from ObjectFactory import ObjectFactory

class Container(object):

    def __init__(self):
        self.__container = {}

    def set_param(self, key, value):
        if not key in self.__container:
            #TODO: should we do parameters expansion here?
            self.__container[key] = value
        else:
            raise ValueError, "Key '%s' already exists in container" % (key)

    def get_param(self, key):
        if key in self.__container:
            return self._expand_parameters(self.__container[key])
        else:
            raise ValueError, "Key '%s' does not exist in container" % (key)

    def _expand_parameters(self, value):
        if isinstance(value, basestring) and value.startswith('%'):
            # string
            key = value[1:]
            if key in self.__container:
                return self._expand_parameters(self.__container[key])
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

    def __str__(self):
        return "MiniMVC.Container"
