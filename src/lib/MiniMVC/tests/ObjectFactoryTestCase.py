#!/usr/bin/python
import sys, unittest

sys.path.append(sys.path[0] + '/../../' )
from MiniMVC.ObjectFactory import ObjectFactory
from MiniMVC.dic import Container

class ObjectFactoryTestCase(unittest.TestCase):

    def test_parse_class_name(self):
    
        self.assertEquals(('__main__', 'MyClass'), ObjectFactory.parse_class_name('MyClass'))
        self.assertEquals(('MyModule', 'MyClass'), ObjectFactory.parse_class_name('MyModule.MyClass'))
        self.assertEquals(('MyPackage.MyModule', 'MyClass'), ObjectFactory.parse_class_name('MyPackage.MyModule.MyClass'))

    def test_import_module(self):
        
        m = ObjectFactory.import_module('MiniMVC.dic')
    
if __name__ == '__main__':
    unittest.main()