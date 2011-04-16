#!/usr/bin/python
import sys, unittest

sys.path.append(sys.path[0] + '/../' )
from Service import Service

class TestClass1:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        
class ServiceTestCase(unittest.TestCase):

    def test_init(self):
        s = Service('TestClass1', ['my_param1', 'my_param2'])
        
    def test_dependencies(self):
        s = Service('TestClass1', ['my_param1', 'my_param2'])
        self.assertEquals([], s.dependencies)
        
        s = Service('TestClass1', ['@my_param1', 'my_param2'])
        self.assertEquals(['my_param1'], s.dependencies)

        s = Service('TestClass1', ['@my_param1', '@my_param2'])
        self.assertEquals(['my_param1', 'my_param2'], s.dependencies)
        
if __name__ == '__main__':
    unittest.main()