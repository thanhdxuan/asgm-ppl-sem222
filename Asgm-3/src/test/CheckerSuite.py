import unittest
from TestUtils import TestChecker
from abc import ABC
from Visitor import Visitor
from StaticError import * 
from AST import *

class CheckerSuite(unittest.TestCase):
    # def test_short_vardecl(self):
    #     input = """x: integer;
    #     x: float;
    #     """
    #     expect = "Redeclared Variable: x"
    #     self.assertTrue(TestChecker.test(input, expect, 3000))
    # def test_short_vardecl_1(self):
    #     input = """
    #     x: integer = "12";
    #     y: float = 1.5;
    #     z: function void() {
    #     }
    #     """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(x, IntegerType, StringLit(12))"
    #     self.assertTrue(TestChecker.test(input, expect, 3001))
    # def test_short_vardecl_2(self):
    #     input = """
    #     x: integer = 12;
    #     y: auto;
    #     z: function void() {
    #     }
    #     """
    #     expect = "Invalid Variable: y"
    #     self.assertTrue(TestChecker.test(input, expect, 3002))
    # def test_short_vardecl_3(self):
    #     input = """
    #     x: integer = 1.2;
    #     y: auto;
    #     z: function void() {
    #     }
    #     """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(x, IntegerType, FloatLit(1.2))"
    #     self.assertTrue(TestChecker.test(input, expect, 3003))
    # def test_short_vardecl_4(self):
    #     input = """
    #     x: integer = 1;
    
    #     y: function void() {
    #         x: auto = 1.5;
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 3004))
    # def test_short_vardecl_5(self):
    #     input = """
    #     x: integer = 1;
    #     z: function void() inherit z {
    #         x: auto = 1.5;
    #     }
    #     y: function void() {
    #         x: auto = 1.5;
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 3005))

    # def test_short_vardecl_6(self):
    #     input = """
    #     x: integer = 1;
    #     z: function void() inherit z {
    #         super(1);
    #         x: auto = 1.5;
    #     }
    #     y: function void() {
    #         x: auto = 1.5;
    #     }
    #     """
    #     expect = "Invalid statement in function: z"
    #     self.assertTrue(TestChecker.test(input, expect, 3006))
    # def test_inherit_1(self):
    #     input = """
    #     x: integer = 1;
    #     z: function void() inherit y {
    #         x: auto = 1.5;
    #     }
    #     y: function void(a: string, b: integer) {
    #         x: auto = 1.5;
    #     }
    #     """
    #     expect = "Invalid statement in function: z"
    #     self.assertTrue(TestChecker.test(input, expect, 3007))
    # def test_inherit_2(self):
    #     input = """
    #     x: integer = 1;
    #     z: function void() inherit y {
    #         preventDefault();
    #         x: auto = 1.5;
    #     }
    #     y: function void(a: string, b: integer) {
    #         x: auto = 1.5;
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 3008))
    # def test_inherit_3(self):
    #     input = """
    #     x: integer = 1;
    #     z: function void() inherit y {
    #         super(1, 2);
    #         x: auto = 1.5;
    #     }
    #     y: function void(a: string, b: integer) {
    #         x: auto = 1.5;
    #     }
    #     """
    #     expect = "Type mismatch in expression: IntegerLit(1)"
    #     self.assertTrue(TestChecker.test(input, expect, 3009))
    # def test_inherit_4(self):
    #     input = """
    #     x: integer = 1;
    #     z: function void() inherit y {
    #         super("a", 2);
    #         x: auto = 1.5;
    #     }
    #     y: function void(a: string, b: integer) {
    #         x: auto = 1.5;
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 3010))
    # def test_inherit_5(self):
    #     """len(arg) > len(param)"""
    #     input = """
    #     x: integer = 1;
    #     z: function void() inherit y {
    #         super(1,2,3);
    #         x: auto = 1.5;
    #     }
    #     y: function void(a: string, b: integer) {
    #         x: auto = 1.5;
    #     }
    #     """
    #     expect = "Type mismatch in expression: IntegerLit(3)"
    #     self.assertTrue(TestChecker.test(input, expect, 3011))
    # def test_inherit_6(self):
    #     """len(arg) < len(param)"""
    #     input = """
    #     x: integer = 1;
    #     z: function void() inherit y {
    #         super(1);
    #         x: auto = 1.5;
    #     }
    #     y: function void(a: string, b: integer) {
    #         x: auto = 1.5;
    #     }
    #     """
    #     expect = "Type mismatch in expression: "
    #     self.assertTrue(TestChecker.test(input, expect, 3012))
    # def test_inherit_7(self):
    #     """check redeclared inherit"""
    #     input = """
    #     x: integer = 1;
    #     z: function void(b: float) inherit y {
    #         super("a", 2);
    #         x: auto = 1.5;
    #     }
    #     y: function void(inherit a: string, inherit b: integer) {
    #         x: auto = 1.5;
    #     }
    #     """
    #     expect = "Invalid Parameter: b"
    #     self.assertTrue(TestChecker.test(input, expect, 3013))
    # def test_inherit_8(self):
    #     """check redeclared inherit"""
    #     input = """
    #     x: integer = 1;
    #     z: function void(k: float) inherit y {
    #         super("a", 2);
    #         x: auto = 1.5;
    #     }
    #     y: function void(inherit a: string, b: string, inherit a: integer) {
    #         x: auto = 1.5;
    #     }
    #     """
    #     expect = "Redeclared Parameter: a"
    #     self.assertTrue(TestChecker.test(input, expect, 3014))

    # def test_inherit_9(self):
    #     """check redeclared inherit"""
    #     input = """
    #     x: integer = 1;
    #     z: function void(k: float) inherit y {
    #         super("a", 2);
    #         x: auto = 1.5;
    #     }
    #     y: function void(inherit a: string, b: string, inherit a: integer) {
    #         x: auto = 1.5;
    #     }
    #     """
    #     expect = "Redeclared Parameter: a"
    #     self.assertTrue(TestChecker.test(input, expect, 3015))
    def test_inherit_10(self):
        """check redeclared inherit"""
        input = """
        inc : function void (out n : integer, a:float) inherit foo{
            
        }
        foo : function auto (inherit m: float, n: integer){
            
        }
        """
        expect = "Invalid statement in function: inc"
        self.assertTrue(TestChecker.test(input, expect, 3016))
    def test_inherit_11(self):
        """check redeclared inherit"""
        input = """
        inc : function void (out n : integer, a:float) inherit foo{
            super();
        }
        foo : function auto (inherit m: float, n: integer){
            
        }
        """
        expect = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input, expect, 3017))