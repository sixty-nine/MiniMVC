from Service import Service
from Container import Container
from ServiceContainer import ServiceContainer

class ContainerAware(object):

    def __init__(self, container):
        self.__container = container

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

from Service import Service
from Container import Container
from ServiceContainer import ServiceContainer

class ContainerAware(object):

    def __init__(self, container):
        self.__container = container

    @property
    def container(self):
        return self.__container
