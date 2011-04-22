import re

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
        if isinstance(value, list):
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

        while isinstance(value, basestring):
            m = re.search('%(.*)%', value)
            if not m: break
            key = m.group(1)
            if key in self.__container:
                if isinstance(self.__container[key], basestring):
                    value = value.replace('%'+key+'%', self.__container[key])
                else:
                    if '%'+key+'%' == value:
                        value = self._expand_parameters(self.__container[key])
                    else:
                        raise ValueError, "Error while trying to expand the parameter '%s' in the expression '%s'" % (key, value)
            else:
                raise ValueError, "The parameter '%s' was not found in the container" % (key)
            
        return value

    def __str__(self):
        return "MiniMVC.Container"
#
# This file is part of the MiniMVC package
#
# (c) dreamcraft.ch
#
# This source file is subject to the MIT license that is bundled
# with this source code in the file LICENSE.
#

import re

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
        if isinstance(value, list):
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

        while isinstance(value, basestring):
            m = re.search('%(.*)%', value)
            if not m: break
            key = m.group(1)
            if key in self.__container:
                if isinstance(self.__container[key], basestring):
                    value = value.replace('%'+key+'%', self.__container[key])
                else:
                    if '%'+key+'%' == value:
                        value = self._expand_parameters(self.__container[key])
                    else:
                        raise ValueError, "Error while trying to expand the parameter '%s' in the expression '%s'" % (key, value)
            else:
                raise ValueError, "The parameter '%s' was not found in the container" % (key)
            
        return value

    def __str__(self):
        return "MiniMVC.Container"
