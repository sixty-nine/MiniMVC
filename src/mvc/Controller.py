class Controller(object):

    def __init__(self, container):
        self.__container = container
        self.__server = container.get('http_server')

    @property
    def server(self):
        return self.__server
        
    @property
    def container(self):
        return self.__container

    def redirect(self, url):
        self.__server.send_response(301)
        self.__server.send_header('Location', url)
        self.__server.end_headers()

    def error404(self):
        self.__server.send_response(404)
        self.__server.end_headers()

    def header(self, result_code, content_type):
        self.__server.send_response(result_code)
        self.__server.send_header('Content-type', content_type)
        self.__server.end_headers()

    def output(self, content):
        self.__server.wfile.write(content)
