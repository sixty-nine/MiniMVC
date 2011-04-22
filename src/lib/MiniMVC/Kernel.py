import os, sys
from Router import Router
from dic import ServiceContainer
from dic.loader import ServiceContainerLoader
from dic.loader import ServicesSectionLoader
from dic.loader import DatabaseSectionLoader
from dic.loader import RoutesSectionLoader
from ObjectFactory import ObjectFactory
from orm.ORM import ORM
from logbook import Logger, NullHandler
        

class Kernel(object):

    def __init__(self):

        # Basic setup
        self.__basepath = os.path.dirname( os.path.realpath(os.path.realpath( __file__ ) + '/../../' ) )
        self.__router = Router()

        # Load container
        self.__container = self._create_container()

        # Setup logging
        if self.__container.has_service('log.handler'):
            self.__log_handler = self.__container.get_service('log.handler')
        else:
            self.__log_handler = NullHandler()

        self.__log_handler.push_thread()
        self.__logger = Logger('MiniMVC')
        self.__container.set_param('sys.log', self.__logger)
        
        # Import application
        sys.path.append(self.__basepath)
        import app

        self.__logger.info('Kernel started')

    def run(self, request):

        query_string = request.unparsed_uri
        self.__logger.info('Request: ' + query_string)
        route = self.__router.route(query_string)
        if route:
            self.__logger.info('Route matched: %s.%s(%s)' % (route['controller'], route['action'], route['params']))
            self.__container.set_param('sys.matched_route', route)
            request.parameters = route['params']
            res = ObjectFactory.instantiate_and_call(route['controller'], [self.__container], route['action'], request)
        else:
            self.__logger.warn('No matching route found for: ' + query_string)
            res = False

        # Shutdown logger and return
        self.__log_handler.pop_thread()

        # Return the local request log
        self.request_log = self.__container.get_service('log.test_handler').records
        
        return res

    def _create_container(self):
        container = ServiceContainer()
        container.set_param('sys.kernel', self)
        container.set_param('sys.container', container)
        container.set_param('sys.basepath', self.__basepath)
        container.set_param('sys.router', self.__router)
        #container.set_param('sys.log', self.__logger)
        
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
#
# This file is part of the MiniMVC package
#
# (c) dreamcraft.ch
#
# This source file is subject to the MIT license that is bundled
# with this source code in the file LICENSE.
#

import os, sys
from Router import Router
from dic import ServiceContainer
from dic.loader import ServiceContainerLoader
from dic.loader import ServicesSectionLoader
from dic.loader import DatabaseSectionLoader
from dic.loader import RoutesSectionLoader
from ObjectFactory import ObjectFactory
from orm.ORM import ORM
from logbook import Logger, NullHandler
        

class Kernel(object):

    def __init__(self):

        # Basic setup
        self.__basepath = os.path.dirname( os.path.realpath(os.path.realpath( __file__ ) + '/../../' ) )
        self.__router = Router()

        # Load container
        self.__container = self._create_container()

        # Setup logging
        if self.__container.has_service('log.handler'):
            self.__log_handler = self.__container.get_service('log.handler')
        else:
            self.__log_handler = NullHandler()

        self.__log_handler.push_thread()
        self.__logger = Logger('MiniMVC')
        self.__container.set_param('sys.log', self.__logger)
        
        # Import application
        sys.path.append(self.__basepath)
        import app

        self.__logger.info('Kernel started')

    def run(self, request):

        query_string = request.unparsed_uri
        self.__logger.info('Request: ' + query_string)
        route = self.__router.route(query_string)
        if route:
            self.__logger.info('Route matched: %s.%s(%s)' % (route['controller'], route['action'], route['params']))
            self.__container.set_param('sys.matched_route', route)
            request.parameters = route['params']
            res = ObjectFactory.instantiate_and_call(route['controller'], [self.__container], route['action'], request)
        else:
            self.__logger.warn('No matching route found for: ' + query_string)
            res = False

        # Shutdown logger and return
        self.__log_handler.pop_thread()

        # Return the local request log
        self.request_log = self.__container.get_service('log.test_handler').records
        
        return res

    def _create_container(self):
        container = ServiceContainer()
        container.set_param('sys.kernel', self)
        container.set_param('sys.container', container)
        container.set_param('sys.basepath', self.__basepath)
        container.set_param('sys.router', self.__router)
        #container.set_param('sys.log', self.__logger)
        
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
