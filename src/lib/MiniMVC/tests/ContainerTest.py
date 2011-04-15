#!/usr/bin/python
import sys, unittest

sys.path.append(sys.path[0] + '/../' )
from Container import Container
from Router import Router

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
        self.assertEqual(container._Container__dic, { })

    def test_set(self):
        container = Container()
        container.set('key', 'value')
        self.assertEquals(container._Container__dic, { 'key': 'value' })
        
        # Duplicate key
        self.assertRaises(ValueError, container.set, 'key', 'value')

    def test_get(self):
        container = Container()
        container.set('key', 'value')
        
        val = container.get('key')
        self.assertEquals(val, 'value')

        # Unexisting key
        self.assertRaises(ValueError, container.get, 'unexisting')
        
        # Complex dictionnary
        complex_dict = {'tuple' : (1, 2, 3), 'foo': 'bar'}
        container.set('dict', complex_dict)
        self.assertEquals(container.get('dict'), complex_dict)

        # Object
        tmp = Container()
        container.set('container', tmp)
        self.assertEquals(container.get('container'), tmp)
        
    def test_load(self):
        container = Container()

        container.load(sys.path[0] + '/fixtures/config.yml')

        #container.dump()

        # Normal values
        self.assertEquals(container.get('foo'), 'bar')
        self.assertEquals(container.get('list'), ['one', 'two', 'three'])
        self.assertEquals(container.get('dict'), {'something': 'something else', 'whatever': ['list 1', 'list 2']})

        # Parameters expansion
        self.assertEquals(container.get('param1'), 'bar')
        self.assertEquals(container.get('param2'), '%unexisting')
        self.assertEquals(container.get('param3'), ['one', 'two', 'three'])
        self.assertEquals(container.get('param4'), ['bar', '%bar'])
        self.assertEquals(container.get('param5'), [['one', 'two', 'three'], ['bar', '%bar']])
        self.assertEquals(container.get('param6'), {'value1' : 'bar', 'value2' : ['one', 'two', 'three']})
        self.assertEquals(container.get('param7'), [[['one', 'two', 'three'], ['bar', '%bar']], {'value1' : 'bar', 'value2' : ['one', 'two', 'three']}])

        # Services expansion
        t1 = container.get('test1')
        t2 = container.get('test2')
        t3 = container.get('test3')
        
        self.assertTrue(isinstance(t1, TestClass1))
        self.assertTrue(isinstance(t2, TestClass2))
        self.assertTrue(isinstance(t3, TestClass3))
        
        self.assertEquals(t2.name, 'my_name')
        self.assertEquals(t3.class1, t1)
        self.assertEquals(t3.class2, t2)
        self.assertTrue(isinstance(t3.class1, TestClass1))
        self.assertTrue(isinstance(t3.class2, TestClass2))
        self.assertEquals(t3.class2.name, 'my_name')
        
        # Unexisting file
        self.assertRaises(ValueError, container.load, 'unexisting')

if __name__ == '__main__':
    unittest.main()