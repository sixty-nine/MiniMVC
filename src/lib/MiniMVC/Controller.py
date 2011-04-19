import dic

class Controller(dic.ContainerAware):

    def __init__(self, container):
        dic.ContainerAware.__init__(self, container)
