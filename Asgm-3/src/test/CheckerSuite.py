import unittest
from TestUtils import TestChecker
from abc import ABC
from Visitor import Visitor
from StaticError import * 
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """x: integer;
        x: float;
        """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 3000))
    def test_short_vardecl_1(self):
        input = """x: integer;
        y: float;
        z: function void(k: float) {
            k: float;
            x = x + k;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3001))