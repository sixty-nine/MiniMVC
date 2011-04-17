#!/usr/bin/python
import sys, unittest
import logbook 

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
        
class TestClass4:
    def __init__(self, a = 1, b = 2, c = 3):
        self.a = a
        self.b = b
        self.c = c

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

        # Service named params
        i4 = container.get_service('test4')
        self.assertTrue(isinstance(i4, getattr(sys.modules['ServiceContainerLoaderTestCase'], 'TestClass4')))
        self.assertEquals(0, i4.a)
        self.assertEquals(1, i4.b)
        self.assertEquals(3, i4.c)

        # Complex service
        log1 = container.get_service('log.handler')
        log2 = container.get_service('log.null_handler')
        log3 = container.get_service('log.file_handler')

        self.assertTrue(isinstance(log1, logbook.NestedSetup))
        self.assertTrue(isinstance(log2, logbook.NullHandler))
        self.assertTrue(isinstance(log3, logbook.FileHandler))
        
        self.assertEquals(log1.objects[0], log2)
        self.assertEquals(log1.objects[1], log3)
        self.assertEquals(log3._filename, '/tmp/testlog.log')
        self.assertEquals(log3.level, logbook.WARNING)


if __name__ == '__main__':
    unittest.main()
