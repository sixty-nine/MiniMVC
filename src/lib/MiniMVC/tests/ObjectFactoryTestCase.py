#!/usr/bin/python
import sys, unittest

sys.path.append(sys.path[0] + '/../' )
from ObjectFactory import ObjectFactory
from Container import Container

class ObjectFactoryTestCase(unittest.TestCase):

    def test_parse_class_name(self):
    
        self.assertEquals(('__main__', 'MyClass'), ObjectFactory.parse_class_name('MyClass'))
        self.assertEquals(('MyModule', 'MyClass'), ObjectFactory.parse_class_name('MyModule.MyClass'))
        self.assertEquals(('MyPackage.MyModule', 'MyClass'), ObjectFactory.parse_class_name('MyPackage.MyModule.MyClass'))

    def test_import_module(self):
        
        m = ObjectFactory.import_module('Container')
        self.assertEquals('Container', m.__name__)
    
if __name__ == '__main__':
    unittest.main()