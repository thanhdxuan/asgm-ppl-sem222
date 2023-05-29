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
    def test1(self):
        init = """main: function void () {
            a: integer = 1;
            b: float = 1.2;
            //c: string;
        }"""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(init, expect, 502))
    def test2(self):
        init = """hehe: integer;
        main: function void () {
            a: integer = 1;
            b: float = 1.2;
            //c: string;
        }"""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(init, expect, 503))
    def test3(self):
        init = """hehe: integer;
        foo: function void() {
            a: string = "dmm";
        }
        main: function void () {
            a: integer = 1;
            b: float = 1.2;
            //c: string;
        }"""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(init, expect, 504))

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
    def test5(self):
        init = """hehe: string = "1223";
        foo: function void(a: integer, b: string, c: float) {
        }
        main: function void () {
            a: integer = 1;
            b: float = 1.2;
            foo(1, "123", 1.2);
            //c: string;
        }"""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(init, expect, 506))
    def test6(self):
        """Test id"""
        init = """hehe: string = "1223";
        foo: function void(a: integer, b: string, c: float) {
        }
        main: function void () {
            a: integer = 1;
            b: float = 1.2;
            foo(a, "123", b);
        }"""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(init, expect, 507))
    def test7(self):
        """Test conversation"""
        init = """hehe: string = "1223";
        foo: function void(a: integer, b: string, c: float) {
        }
        main: function void () {
            a: integer = 1;
            b: float = 1.2;
            foo(a, "123", 1);
        }"""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(init, expect, 508))
    def test8(self):
        """Test conversation"""
        init = """hehe: string = "1223";
        bar: function integer() {
            return 1;
        }
        foo: function void(a: integer, b: string, c: float) {
        }
        main: function void () {
            a: integer = 1;
            b: float = 1.2;
            foo(a, "123", bar());
        }"""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(init, expect, 509))
    def test9(self):
        """Test conversation"""
        init = """hehe: string = "1223";
        bar: function float() {
            return 1;
        }
        foo: function void(a: integer, b: string, c: float) {
        }
        main: function void () {
            a: integer = 1;
            b: float = 1.2;
            foo(a, "123", bar());
        }"""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(init, expect, 510))
    def test10(self):
        """Test expr"""
        init = """hehe: string = "1223";
        bar: function float() {
            return 1;
        }
        foo: function void(a: integer, b: string, c: float) {
        }
        main: function void () {
            a: integer = 1;
            b: float = (1.2 + 1) * 2;
            c: boolean = true;
            foo(a, "123", bar());
        }"""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(init, expect, 511))

    def test11(self):
        """Test if statement"""
        init = """
        bar: function integer() {
            return 1;
        }
        main: function void () {
            if (bar() == 1) printInteger(5);
        }"""
        expect = r"""5"""
        self.assertTrue(TestCodeGen.test(init, expect, 512))
    def test12(self):
        """Test if statement"""
        init = """
        bar: function integer() {
            return 1;
        }
        main: function void () {
            if (bar() > 1.0) printInteger(5);
            else printInteger(7);
        }"""
        expect = r"""7"""
        self.assertTrue(TestCodeGen.test(init, expect, 513))

    def test13(self):
        """Test block stmt"""
        init = """
        bar: function integer() {
            return 1;
        }
        main: function void () {
            if (1 != 1) {
                printInteger(5);
            }
            else {
                a: integer = 8;
                printInteger(a);
            }
        }"""
        expect = r"""8"""
        self.assertTrue(TestCodeGen.test(init, expect, 514))
    def test14(self):
        """Test assign stmt"""
        init = """str: integer = 10;
        bar: function integer() {
            return 1;
        }
        main: function void () {
            if (1 != 1) {
                printInteger(5);
            }
            else {
                a: integer = 8;
                a = a * 9 * str;
                printInteger(a);
            }
        }"""
        expect = r"""720"""
        self.assertTrue(TestCodeGen.test(init, expect, 515))
    
    def test15(self):
        """Test while stmt"""
        init = """str: integer = 10;
        bar: function integer() {
            return 1;
        }
        main: function void () {
            i: integer = 0;
            while(i < 10) {
                printInteger(i);
                i = i + 1;
            }
        }"""
        expect = r"""0123456789"""
        self.assertTrue(TestCodeGen.test(init, expect, 516))

    def test16(self):
        """Test for stmt"""
        init = """str: integer = 10;
        bar: function integer() {
            return 1;
        }
        main: function void () {
            i: integer;
            for(i = 0, i < 10, i + 1) {
                if (i % 2 == 0)
                    printInteger(i);
            }
        }"""
        expect = r"""02468"""
        self.assertTrue(TestCodeGen.test(init, expect, 517))

    def test17(self):
        """Test for stmt"""
        init = """str: integer = 10;
        bar: function integer() {
            return 1;
        }
        main: function void () {
            i: integer;
            for(i = 0, i < 10, i + 1) {
                if (i % 2 == 0)
                    printInteger(i);
            }
        }"""
        expect = r"""02468"""
        self.assertTrue(TestCodeGen.test(init, expect, 518))

    def test18(self):
        """Test do while stmt"""
        init = """str: integer = 10;
        bar: function integer() {
            return 1;
        }
        main: function void () {
            i: integer;
            do {
                i = 100;
                i = i + 1;
            }
            while(i > 2000);
            printInteger(i);
        }"""
        expect = r"""101"""
        self.assertTrue(TestCodeGen.test(init, expect, 519))

    def test19(self):
        """Test do while stmt"""
        init = """str: integer = 10;
        bar: function integer() {
            return 1;
        }
        main: function void () {
            i: integer = 0;
            do {
                i = i + 1;
                printInteger(i);
            }
            while(i < 5);
        }"""
        expect = r"""12345"""
        self.assertTrue(TestCodeGen.test(init, expect, 520))

    def test20(self):
        """Test do while stmt - break"""
        init = """str: integer = 10;
        bar: function integer() {
            return 1;
        }
        main: function void () {
            i: integer = 0;
            do {
                i = i + 1;
                printInteger(i);
                if (i == 6) break;
            }
            while(i < 100);
        }"""
        expect = r"""123456"""
        self.assertTrue(TestCodeGen.test(init, expect, 521))
    def test21(self):
        """Test do while stmt - continue"""
        init = """str: integer = 10;
        bar: function integer() {
            return 1;
        }
        main: function void () {
            i: integer = 0;
            do {
                i = i + 1;
                if (i == 6) continue;
                printInteger(i);
            }
            while(i < 10);
        }"""
        expect = r"""1234578910"""
        self.assertTrue(TestCodeGen.test(init, expect, 522))
#FIXME - AST Error
    # def test22(self):
    #     """Test do while stmt - continue"""
    #     init = Program([FuncDecl(
    #         "main", 
    #         VoidType(), 
    #         list(), 
    #         None, 
    #         BlockStmt([
    #             VarDecl("i", IntegerType(), IntegerLit(0)),
    #             DoWhileStmt(BinExpr('<', Id('i'), IntegerLit(10)), 
    #                         BlockStmt([
    #                             AssignStmt(Id('i'), BinExpr('+', Id('i'), IntegerLit(1))), 
    #                             IfStmt(
    #                                 BinExpr('||', 
    #                                         BinExpr('==', Id('i'), IntegerLit(6)), 
    #                                         BinExpr('==', Id('i'), IntegerLit(8))), 
    #                                 ContinueStmt()), 
    #                             CallStmt('printInteger', [Id('i')])]))]))])
    #     # init = """str: integer = 10;
    #     # bar: function integer() {
    #     #     return 1;
    #     # }
    #     # main: function void () {
    #     #     i: integer = 0;
    #     #     do {
    #     #         i = i + 1;
    #     #         if (i == 6 || i == 8) continue;
    #     #         printInteger(i);
    #     #     }
    #     #     while(i < 10);
    #     # }"""
    #     expect = r"""123457910"""
    #     self.assertTrue(TestCodeGen.test(init, expect, 523))