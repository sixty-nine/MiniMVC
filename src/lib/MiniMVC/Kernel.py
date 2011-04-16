import os, sys
from Router import Router
from ServiceContainer import ServiceContainer
from ServiceContainerLoader import ServiceContainerLoader
from ObjectFactory import ObjectFactory


class Kernel(object):

    def __init__(self):
        
        self.__basepath = os.path.dirname( os.path.realpath(os.path.realpath( __file__ ) + '/../../' ) )
        self.__container = self._create_container()
        self.__router = Router()

        sys.path.append(self.__basepath)
        import app

        routes = self.__container.get_param('routes')
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
            return False

    def _create_container(self):
        container = ServiceContainer()
        container.set_param('sys.kernel', self)
        container.set_param('sys.container', container)
        container.set_param('sys.basepath', self.__basepath)
        
        ServiceContainerLoader.load(container, self.__basepath + '/app/config/config.yml')
        return container

    @property
    def container(self):
        return self.__container
