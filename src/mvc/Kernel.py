import yaml
import os, sys
from Router import Router
from Container import Container
from ObjectFactory import ObjectFactory
from mod_python import apache

class Kernel(object):

    def __init__(self):
        
        self.__basepath = os.path.dirname( os.path.realpath(os.path.realpath( __file__ ) + '/../' ) )
        self.__container = self._create_container()
        self.__router = Router()
        
        routes = self.__container.get('routes')
        for route in routes:
            self.__router.addRoute(route, routes[route]['pattern'], routes[route]['controller'], routes[route]['action'])

    def run(self, request):

        # TODO: unhardcode the script name
        query_string = request.unparsed_uri
        route = self.__router.route(query_string)
        if route:
            request.parameters = route['params']
            return ObjectFactory.instantiate_and_call(route['controller'], [self.__container], route['action'], request)
        else:
            # Not found
            return apache.HTTP_NOT_FOUND

    def _create_container(self):
        container = Container()
        container.set('kernel', self)
        container.set('container', container)
        container.set('basepath', self.__basepath)
        #TODO: extract the config loader so that multiple formats (xml, yaml) can be used
        container.load(self.__basepath + '/app/config/config.yml')
        return container
