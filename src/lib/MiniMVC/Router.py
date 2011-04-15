import sys, re
from routes import Mapper

class Router(object):

    def __init__(self):
        self.__mapper = Mapper()

    def addRoute(self, name, pattern, controller, action):
        self.__mapper.connect(name, pattern, controller = controller, action = action)

    def route(self, path):
        route = self.__mapper.routematch(path)
        if route:
            params = {}
            for param in route[0]:
                if param != 'controller' and param != 'action':
                    params[param] = route[0][param]

            return { 
                'controller': route[0]['controller'], 
                'action': route[0]['action'],
                'params': params
            }

        return False
