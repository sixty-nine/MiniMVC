class Controller(object):

    def __init__(self, container):
        self.__container = container

    @property
    def container(self):
        return self.__container
