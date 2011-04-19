import dic

class Controller(dic.ContainerAware):

    def __init__(self, container):
        ContainerAware.__init__(container)
