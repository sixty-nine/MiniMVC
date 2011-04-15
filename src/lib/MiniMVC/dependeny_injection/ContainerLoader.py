class ContainerLoader:

    def __init__(self, container):
        self.__container = container
        
    def load(self, filename):
        pass
        
    @property
    def container(self):
        return self.__container
