import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test(self):
        init = """main: function void () {
            printInteger(5);
            printString("hehe");
        }"""
        expect = """5\nhehe\n"""
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
        """test - funcall"""
        init = """hehe: string = "1223";
        foo: function string() {
            a: string = "Hello";
            return a;
        }
        main: function void () {
            a: integer = 1;
            b: float = 1.2;
            printString(foo());
        }"""
        expect = """Hello\n"""
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
        expect = """5\n"""
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
        expect = """7\n"""
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
        expect = """8\n"""
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
        expect = """720\n"""
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
        expect = """0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n"""
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
        expect = """0\n2\n4\n6\n8\n"""
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
        expect = """0\n2\n4\n6\n8\n"""
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
        expect = """101\n"""
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
        expect = """1\n2\n3\n4\n5\n"""
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
        expect = """1\n2\n3\n4\n5\n6\n"""
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
        expect = """1\n2\n3\n4\n5\n7\n8\n9\n10\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 522))
    def test24(self):
        """Test array declare - local"""
        init = """arr: array [2] of integer = {3, 4};
        main: function void () {
            i: array [2] of string = {"heheh", "jaja"};
            printString(i[1]);
        }"""
        expect = """jaja\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 524))

    def test25(self):
        """Test multi dimensions array declare - local"""
        init = """main: function void () {
            i: array [3, 2, 1] of integer = { {{7}, {8}}, {{9}, {10}}, {{11}, {12}}};
        }"""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(init, expect, 525))

    def test26(self):
        """Test multi dimensions array declare - local"""
        init = """main: function void () {
            i: array [3, 2] of string = { {"ehhe", "ehhe"}, {"ehhe", "ehhe"}, {"ehhe", "ehhe"}};
            b: array [3] of boolean = {true, false, true};
        }"""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(init, expect, 526))
    def test27(self):
        """Test array cell"""
        init = """main: function void () {
            arr: array [3] of integer = {1, 2, 3};
            a: integer;
            a = arr[2];
            printInteger(a);
        }"""
        expect = """3\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 527))
    def test28(self):
        """Test array cell"""
        init = """main: function void () {
            arr: array [3] of integer = {1, 2, 3};
            printInteger(arr[1]);
        }"""
        expect = """2\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 528))

    def test29(self):
        """Test array cell"""
        init = """main: function void () {
            arr: array [6] of integer = {1, 2, 3, 4, 5, 6};
            i: integer;
            for (i = 0, i < 6, i + 1) {
                printInteger(arr[i]);
            }
        }"""
        expect = """1\n2\n3\n4\n5\n6\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 529))

    def test30(self):
        """Test array cell"""
        init = """main: function void () {
            arr: array [6] of integer = {1, 2, 3, 4, 5, 6};
            i: integer;
            /*for (i = 0, i < 6, i + 1) {
                arr[i] = -1;
            }
            for (i = 0, i < 6, i + 1) {
                printInteger(arr[i]);
            }*/
            arr[2] = -1;
            printInteger(arr[2]);
        }"""
        expect = """-1\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 530))

    def test31(self):
        """Test array cell"""
        init = """main: function void () {
            arr: array [6] of integer = {1, 2, 3, 4, 5, 6};
            i: integer;
            /*for (i = 0, i < 6, i + 1) {
                arr[i] = -1;
            }
            for (i = 0, i < 6, i + 1) {
                printInteger(arr[i]);
            }*/
            arr[2] = -100;
            printInteger(arr[2]);
        }"""
        expect = """-100\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 531))

    def test32(self):
        """Test array cell"""
        init = """main: function void () {
            arr: array [6] of integer = {1, 2, 3, 4, 5, 6};
            i: integer;
            for (i = 0, i < 6, i + 1) {
                arr[i] = -1;
            }
            for (i = 0, i < 6, i + 1) {
                printInteger(arr[i]);
            }
        }"""
        expect = """-1\n-1\n-1\n-1\n-1\n-1\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 532))

    def test33(self):
        """Test array cell"""
        init = """arr: array [6] of integer = {1, 2, 3, 4, 5, 6};
        main: function void () {
            i: integer;
            for (i = 0, i < 6, i + 1) {
                arr[i] = -1;
            }
            for (i = 0, i < 6, i + 1) {
                printInteger(arr[i]);
            }
        }"""
        expect = """-1\n-1\n-1\n-1\n-1\n-1\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 533))

    def test34(self):
        """Test array cell"""
        init = """arr: array [6] of integer = {1, 2, 3, 4, 5, 6};
        main: function void () {
            i: integer;
            /*for (i = 0, i < 6, i + 1) {
                arr[i] = -1;
            }*/
            for (i = 0, i < 6, i + 1) {
                printInteger(arr[i]);
            }
        }"""
        expect = """1\n2\n3\n4\n5\n6\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 534))

    def test_new(self):
        """Test print function"""
        init = """main: function void () {
            printFloat(5.2);
        }"""
        expect = """5.2\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 601))



    def test_new_1(self):
        init = """main: function void () {
            printBoolean(true);
        }"""
        expect = """true\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 602))

    def test_new_2(self):
        init = """main: function void () {
            printBoolean(true);
            printBoolean(false);
        }"""
        expect = """true\nfalse\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 603))

    def test_new_3(self):
        """Test print function"""
        init = """main: function void () {
            printFloat(5.2 / 2);
        }"""
        expect = """2.6\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 604))


    def test_new_4(self):
        """Test print function"""
        init = """main: function void () {
            printFloat(5.2 * 2);
        }"""
        expect = """10.4\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 605))

    def test_new_5(self):
        """Test print function"""
        init = """main: function void () {
            printFloat(5.2 - 0.2);
        }"""
        expect = """5.0\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 606))

    def test_new_6(self):
        """Test print function"""
        init = """main: function void () {
            printBoolean(!true);
        }"""
        expect = """false\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 607))

    def test_new_7(self):
        """Test print function"""
        init = """main: function void () {
            printBoolean(!!true);
        }"""
        expect = """true\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 608))
    def test_new_8(self):
        """Test print function"""
        init = """main: function void () {
            printBoolean(true || false);
        }"""
        expect = """true\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 609))

    def test_new_9(self):
        """Test print function"""
        init = """main: function void () {
            printBoolean(true && false);
        }"""
        expect = """false\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 610))

    def test_new_10(self):
        """Test print function"""
        init = """main: function void () {
            a: integer = 1;
            printFloat(a + 0.5);
        }"""
        expect = """1.5\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 611))

    def test_new_11(self):
        """Test print function"""
        init = """main: function void () {
            a: integer = 1;
            printFloat(a + 2 + 2.5);
        }"""
        expect = """5.5\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 612))

    def test_new_12(self):
        """Test print function"""
        init = """main: function void () {
            a: integer = 1;
            printFloat(a + 2 + 2.5 * 2);
        }"""
        expect = """8.0\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 613))

    def test_new_13(self):
        """Test print function"""
        init = """main: function void () {
            printString("Toi la " :: "Thanh!");
        }"""
        expect = """Toi la Thanh!\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 614))

    def test_new_14(self):
        """Test print function"""
        init = """main: function void () {
            name: string = "Thanh";
            printString("Toi la " :: (name :: "!"));
        }"""
        expect = """Toi la Thanh!\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 615))

    def test_new_15(self):
        """test - funcall"""
        init = """hehe: string = "1223";
        sum: function integer(a: integer, b: integer) {
            return a + b;
        }
        main: function void () {
            res: integer;
            res = sum(2, 3);
            printInteger(res);
        }"""
        expect = """5\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 616))

    def test_new_16(self):
        """test - funcall"""
        init = """
        sum: function integer(a: array [5] of integer) {
            i: integer;
            s: integer = 0;
            for (i = 0, i < 5, i + 1) {
                s = s + a[i];
            }
            return s;
        }
        main: function void () {
            arr: array [5] of integer = {1, 2, 3, 4, 5};
            s: integer;
            s = sum(arr);
            printInteger(s);
        }"""
        expect = """15\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 617))

    def test_new_17(self):
        """test - funcall"""
        init = """
        sum: function integer(a: array [5] of integer) {
            i: integer;
            s: integer = 0;
            for (i = 0, i < 5, i + 1) {
                s = s + a[i];
            }
            return s;
        }
        main: function void () {
            arr: array [5] of integer = {1, 2, 3, 4, 5};
            s: integer;
            s = sum(arr) + 10;
            printInteger(s);
        }"""
        expect = """25\n"""
        self.assertTrue(TestCodeGen.test(init, expect, 618))