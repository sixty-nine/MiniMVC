#!/usr/bin/python
import sys, unittest

sys.path.append(sys.path[0] + '/../../' )
from MiniMVC.ServiceContainer import ServiceContainer
from MiniMVC.ServiceContainerLoader import ServiceContainerLoader
from MiniMVC.loaders.DatabaseSectionLoader import DatabaseSectionLoader
from MiniMVC.loaders.ServicesSectionLoader import ServicesSectionLoader

class TestClass1:
    def __init__(self):
        pass

class TestClass2:
    def __init__(self, name):
        self.name = name
        
class TestClass3:
    def __init__(self, class1, class2):
        self.class1 = class1
        self.class2 = class2

class ServiceContainerLoaderTestCase(unittest.TestCase):

    def test_load(self):
        container = ServiceContainer()
        loader = ServiceContainerLoader()
        loader.register_section_loader(DatabaseSectionLoader())
        loader.register_section_loader(ServicesSectionLoader())
        loader.load(container, sys.path[0]  + '/fixtures/config.yml')

        #container.dump()
        
        # Test parameters
        self.assertEquals('bar', container.get_param('foo'))
        self.assertEquals(['one', 'two', 'three'], container.get_param('list'))
        self.assertEquals({'something': 'something else', 'whatever': ['list 1', 'list 2']}, container.get_param('dict'))
        self.assertEquals('bar', container.get_param('param1'))
        self.assertEquals('%unexisting', container.get_param('param2'))
        self.assertEquals(['one', 'two', 'three'], container.get_param('param3'))
        self.assertEquals(['bar', '%bar'], container.get_param('param4'))
        self.assertEquals([['one', 'two', 'three'], ['bar', '%bar']], container.get_param('param5'))
        self.assertEquals({'value2': ['one', 'two', 'three'], 'value1': 'bar'}, container.get_param('param6'))
        self.assertEquals([[['one', 'two', 'three'], ['bar', '%bar']], {'value2': ['one', 'two', 'three'], 'value1': 'bar'}], container.get_param('param7'))
        
        # Test services
        i1 = container.get_service('test1')
        i2 = container.get_service('test2')
        i3 = container.get_service('test3')

        self.assertTrue(isinstance(i1, getattr(sys.modules['ServiceContainerLoaderTestCase'], 'TestClass1')))
        self.assertTrue(isinstance(i2, getattr(sys.modules['ServiceContainerLoaderTestCase'], 'TestClass2')))
        self.assertTrue(isinstance(i3, getattr(sys.modules['ServiceContainerLoaderTestCase'], 'TestClass3')))

        self.assertEquals('my_name', i2.name)
        self.assertTrue(isinstance(i3.class1, getattr(sys.modules['ServiceContainerLoaderTestCase'], 'TestClass1')))
        self.assertTrue(isinstance(i3.class2, getattr(sys.modules['ServiceContainerLoaderTestCase'], 'TestClass2')))

if __name__ == '__main__':
    unittest.main()
