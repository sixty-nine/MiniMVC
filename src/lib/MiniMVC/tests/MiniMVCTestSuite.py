#!/usr/bin/python
import unittest

from ContainerTestCase import ContainerTestCase, TestClass1, TestClass2, TestClass3
from ObjectFactoryTestCase import ObjectFactoryTestCase
from ServiceTestCase import ServiceTestCase

if __name__ == '__main__':

    suite = unittest.TestSuite()

    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ContainerTestCase))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ObjectFactoryTestCase))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ServiceTestCase))

    unittest.TextTestRunner(verbosity=2).run(suite)