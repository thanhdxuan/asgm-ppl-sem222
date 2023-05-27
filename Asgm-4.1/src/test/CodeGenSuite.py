import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test(self):
    #     init = """main: function void () {
    #         printInteger(5);
    #     }"""
    #     expect = r"""5"""
    #     self.assertTrue(TestCodeGen.test(init, expect, 501))
    # def test1(self):
    #     init = """main: function void () {
    #         a: integer = 1;
    #         b: float = 1.2;
    #         //c: string;
    #     }"""
    #     expect = r""""""
    #     self.assertTrue(TestCodeGen.test(init, expect, 502))
    # def test2(self):
    #     init = """hehe: integer;
    #     main: function void () {
    #         a: integer = 1;
    #         b: float = 1.2;
    #         //c: string;
    #     }"""
    #     expect = r""""""
    #     self.assertTrue(TestCodeGen.test(init, expect, 503))
    # def test3(self):
    #     init = """hehe: integer;
    #     foo: function void() {
    #         a: string = "dmm";
    #     }
    #     main: function void () {
    #         a: integer = 1;
    #         b: float = 1.2;
    #         //c: string;
    #     }"""
    #     expect = r""""""
    #     self.assertTrue(TestCodeGen.test(init, expect, 504))

    def test4(self):
        init = """hehe: string = "1223";
        foo: function void() {
            a: string = "dmm";
        }
        main: function void () {
            a: integer = 1;
            b: float = 1.2;
            //c: string;
        }"""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(init, expect, 505))