#!/usr/bin/python
import sys, unittest

sys.path.append(sys.path[0] + '/../' )
from Container import Container

# ----- TEST CLASSES -----

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
        
class ContainerTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        container = Container()
        self.assertEqual(container._Container__container, { })

    def test_set(self):
        container = Container()
        container.set_param('key', 'value')
        self.assertEquals(container._Container__container, { 'key': 'value' })
        
        # Duplicate key
        self.assertRaises(ValueError, container.set_param, 'key', 'value')

    def test_get(self):
        container = Container()
        container.set_param('key', 'value')
        
        val = container.get_param('key')
        self.assertEquals(val, 'value')

        # Unexisting key
        self.assertRaises(ValueError, container.get_param, 'unexisting')
        
        # Complex dictionnary
        complex_dict = {'tuple' : (1, 2, 3), 'foo': 'bar'}
        container.set_param('dict', complex_dict)
        self.assertEquals(container.get_param('dict'), complex_dict)

        # Object
        tmp = Container()
        container.set_param('container', tmp)
        self.assertEquals(container.get_param('container'), tmp)
        
if __name__ == '__main__':
    unittest.main()