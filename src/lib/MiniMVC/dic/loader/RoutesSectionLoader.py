from MiniMVC import Router


class RoutesSectionLoader(object):

    def load(self, container, name, config):
        
        if name != 'routes':
            return False
        
        router = container.get_param('sys.router')
        for route in config:
            router.addRoute(route, config[route]['pattern'], config[route]['controller'], config[route]['action'])

        container.set_param('sys.routes', config)
        
        return True
#
# This file is part of the MiniMVC package
#
# (c) dreamcraft.ch
#
# This source file is subject to the MIT license that is bundled
# with this source code in the file LICENSE.
#

from MiniMVC import Router


class RoutesSectionLoader(object):

    def load(self, container, name, config):
        
        if name != 'routes':
            return False
        
        router = container.get_param('sys.router')
        for route in config:
            router.addRoute(route, config[route]['pattern'], config[route]['controller'], config[route]['action'])

        container.set_param('sys.routes', config)
        
        return True
