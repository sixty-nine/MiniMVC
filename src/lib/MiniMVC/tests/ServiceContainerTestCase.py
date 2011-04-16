#!/usr/bin/python
import sys, unittest

sys.path.append(sys.path[0] + '/../' )
from ServiceContainer import ServiceContainer
from Service import Service

class TestClass1:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        
class TestClass2:
    pass
        
class ServiceContainerTestCase(unittest.TestCase):

    def test_init(self):
        s = ServiceContainer()
        self.assertTrue(isinstance(s, ServiceContainer))
        self.assertEquals({}, s._ServiceContainer__container)
        
    def test_set(self):
        s = ServiceContainer()
        service_def = Service('TestClass1', ['param1', 'param2'])
        s.set_service('test', service_def)
        self.assertEquals({'test' : service_def}, s._ServiceContainer__container)
        
    def test_get(self):
        s = ServiceContainer()
        service_def = Service('TestClass1', ['param1', 'param2'])
        s.set_service('test', service_def)
        
        i = s.get_service('test')
        self.assertTrue(isinstance(i, TestClass1))

    def test_get_dependencies(self):

        s = ServiceContainer()
        service_def1 = Service('TestClass1', ['@test2', '@test3'])
        service_def2 = Service('TestClass2', [])
        service_def3 = Service('TestClass2', [])

        s.set_service('test1', service_def1)
        s.set_service('test2', service_def2)
        s.set_service('test3', service_def3)
        
        i1 = s.get_service('test1')
        i2 = s.get_service('test2')
        i3 = s.get_service('test3')
        
        self.assertTrue(isinstance(i1, TestClass1))
        self.assertTrue(isinstance(i2, TestClass2))
        self.assertTrue(isinstance(i3, TestClass2))

        self.assertFalse(i2 == i3)
        self.assertFalse(i1.param1 == i2)
        self.assertFalse(i1.param2 == i3)

    def test_get_persistent_dependencies(self):

        s = ServiceContainer()
        service_def1 = Service('TestClass1', ['@test2', '@test3'])
        service_def2 = Service('TestClass2', [])
        service_def3 = Service('TestClass2', [])

        service_def2.setPersistent(True)
        service_def3.setPersistent(True)

        s.set_service('test1', service_def1)
        s.set_service('test2', service_def2)
        s.set_service('test3', service_def3)
        
        i1 = s.get_service('test1')
        i2 = s.get_service('test2')
        i3 = s.get_service('test3')
        
        self.assertTrue(isinstance(i1, TestClass1))
        self.assertTrue(isinstance(i2, TestClass2))
        self.assertTrue(isinstance(i3, TestClass2))

        self.assertFalse(i2 == i3)
        self.assertTrue(i1.param1 == i2)
        self.assertTrue(i1.param2 == i3)

    def test_circular_dependencies(self):
        s = ServiceContainer()
        service_def1 = Service('TestClass1', ['@test2', ''])
        service_def2 = Service('TestClass1', ['@test1', ''])
        s.set_service('test1', service_def1)
        s.set_service('test2', service_def2)
        
        self.assertRaises(ValueError, s.get_service, 'test1')
        
        
if __name__ == '__main__':
    unittest.main()