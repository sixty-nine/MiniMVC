#!/usr/bin/python
import unittest

from ContainerTest import ContainerTestCase, TestClass1, TestClass2, TestClass3


if __name__ == '__main__':

    suite = unittest.TestSuite()

    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ContainerTestCase))

    unittest.TextTestRunner(verbosity=2).run(suite)