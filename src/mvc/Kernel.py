import yaml
import os, sys
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from Router import Router
from Container import Container
from ObjectFactory import ObjectFactory

class MyRequestHandler(BaseHTTPRequestHandler):

    def __init__(self, request, client_address, server):
        self.__container = self._create_container()
        self.__router = Router()
        routes = self.__container.get('routes')

        for route in routes:
            self.__router.addRoute(route, routes[route]['pattern'], routes[route]['controller'], routes[route]['action'])

        BaseHTTPRequestHandler.__init__(self, request, client_address, server)
    
    def do_GET(self):
        route = self.__router.route(self.path)
        if route:
            ObjectFactory.instantiate_and_call(route['controller'], [self.__container], route['action'], route['params'])
        else:
            # Not found
            self.send_response(404)
            self.end_headers()

    def _create_container(self):
        container = Container()
        container.set('http_server', self)
        container.set('container', container)
        #TODO: extract the config loader so that multiple formats (xml, yaml) can be used
        container.load(sys.path[0] + '/config/config.yml')
        return container

class Kernel(object):

    def __init__(self):
        try:
            self.__httpd = HTTPServer(('', 8000), MyRequestHandler)
        except:
            pass

    def run(self):
        try:
            self.start()
        except:
            self.stop()

    def start(self):
        print 'Server started...'
        self.__httpd.serve_forever()

    def stop(self):
        print 'Server shutting down'
        self.__httpd.socket.close()
