import os, sys
from Router import Router
from ServiceContainer import ServiceContainer
from ServiceContainerLoader import ServiceContainerLoader
from loaders.ServicesSectionLoader import ServicesSectionLoader
from loaders.DatabaseSectionLoader import DatabaseSectionLoader
from loaders.RoutesSectionLoader import RoutesSectionLoader
from ObjectFactory import ObjectFactory
from orm.ORM import ORM
from logbook import Logger
        

class Kernel(object):

    def __init__(self):

        self.__basepath = os.path.dirname( os.path.realpath(os.path.realpath( __file__ ) + '/../../' ) )
        self.__router = Router()
        self.__logger = Logger('MiniMVC')

        self.__container = self._create_container()

        sys.path.append(self.__basepath)
        import app

        self.__logger.info('Kernel started')

    def run(self, request):

        # TODO: unhardcode the script name
        query_string = request.unparsed_uri
        self.__logger.info('Request: ' + query_string)
        route = self.__router.route(query_string)
        if route:
            self.__logger.info('Route matched: %s.%s(%s)' % (route['controller'], route['action'], route['params']))
            self.__container.set_param('sys.matched_route', route)
            request.parameters = route['params']
            return ObjectFactory.instantiate_and_call(route['controller'], [self.__container], route['action'], request)
        else:
            self.__logger.warn('No matching route found for: ' + query_string)
            return False

    def _create_container(self):
        container = ServiceContainer()
        container.set_param('sys.kernel', self)
        container.set_param('sys.container', container)
        container.set_param('sys.basepath', self.__basepath)
        container.set_param('sys.router', self.__router)
        container.set_param('sys.log', self.__logger)
        
        loader = ServiceContainerLoader()
        loader.register_section_loader(DatabaseSectionLoader())
        loader.register_section_loader(ServicesSectionLoader())
        loader.register_section_loader(RoutesSectionLoader())

        loader.load(container, self.__basepath + '/app/config/config.yml')
        return container

    def __str__(self):
        return "MiniMVC.Kernel"
        
    @property
    def container(self):
        return self.__container
