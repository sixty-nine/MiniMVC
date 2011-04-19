from Service import Service
from Container import Container
from ServiceContainer import ServiceContainer

class ContainerAware(object):

    def __init__(self, container):
        self.__container = container

    @property
    def container(self):
        return self.__container
