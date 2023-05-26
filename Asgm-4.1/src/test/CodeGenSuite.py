import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test(self):
        init = """main: function void () {
            printInteger(5);
        }"""
        expect = r"""5"""
        self.assertTrue(TestCodeGen.test(init, expect, 501))
