from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *


# class SomeUtils:
#     @staticmethod
#     def retriveType(typ):
#         if type(typ) is ArrayType: return Arra

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

class ClassType(Type):
    def __init__(self, cname):
        self.cname = cname

    def __str__(self):
        return "Class({0})".format(str(self.cname))

    def accept(self, v, param):
        return None

class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + self.name + "," + str(self.mtype) + ")"


class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("readInteger", MType(list(), IntegerType()), CName(self.libName)),
                Symbol("printInteger", MType([IntegerType()], VoidType()), CName(self.libName)),
                Symbol("readFloat", MType(list(), FloatType()), CName(self.libName)),
                Symbol("printFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("readBoolean", MType(list(), BooleanType()), CName(self.libName)),
                Symbol("printBoolean", MType([BooleanType()], VoidType()), CName(self.libName)),
                Symbol("readString", MType(list(), StringType()), CName(self.libName)),
                Symbol("printString", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("super", MType(list(), VoidType()), CName(self.libName)),
                Symbol("preventDefault", MType(list(), VoidType()), CName(self.libName))
                ]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)


class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value


class CodeGenVisitor(Visitor):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.className = "MT22Class"
        self.path = path
        self.emit = Emitter(self.path + "/" + self.className + ".j")
    def visitProgram(self, ast, c):
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        # generate default constructor
        
        staticDecl = self.env
        for x in ast.decls:
            if type(x) is FuncDecl:
                partype = [i.typ for i in x.params]
                staticDecl = [Symbol(x.name.lower(), MType(partype, x.return_type), CName(self.className))] + staticDecl
            else:
                newSym = self.visit(x, None)
                staticDecl = [newSym] + staticDecl
        
        self.genMETHOD(FuncDecl("<init>", None, list(), None, BlockStmt(list())), c, Frame("<init>", VoidType))
        e = SubBody(None, staticDecl)
        [self.visit(x, e) for x in ast.decls if type(x) is FuncDecl]
        
        self.genMETHOD(FuncDecl("<clinit>", None, list(), None, BlockStmt(list())), staticDecl, Frame("<clinit>", VoidType))


        self.emit.emitEPILOG()
        return c


    def genMETHOD(self, consdecl, o, frame):
        isInit = consdecl.return_type is None and consdecl.name == "<init>"
        isClassInit = consdecl.return_type is None and consdecl.name == "<clinit>"

        isMain = str(consdecl.name) == "main" and len(consdecl.params) == 0 and type(consdecl.return_type) is VoidType
        
        return_type = VoidType() if isInit or isClassInit else consdecl.return_type
        
        methodName = "<init>" if isInit else consdecl.name
        methodName = "<clinit>" if isClassInit else consdecl.name
        intype = [ArrayType(0, StringType())] if isMain else list(
            map(lambda x: x.typ, consdecl.params))
        mtype = MType(intype, return_type)

        # start method
        code = self.emit.emitMETHOD(methodName, mtype, not isInit, frame)
        self.emit.printout(code)

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            idx = frame.getNewIndex()
            typ = ClassType(Id(self.className))
            code = self.emit.emitVAR(idx, "this", typ, frame.getStartLabel(), frame.getEndLabel(), frame)
            self.emit.printout(code)
        elif isMain:
            idx = frame.getNewIndex()
            typ = ArrayType(0, StringType())
            code = self.emit.emitVAR(idx, "args", typ, frame.getStartLabel(), frame.getEndLabel(), frame)
            self.emit.printout(code)
        # elif not isClassInit:
        #     local = reduce(lambda env, ele: SubBody(frame, [self.visit(ele, env)] + env.sym), consdecl.params, SubBody(frame, []))
        #     glenv = local.sym + glenv

        
        body = consdecl.body
        startFuncLabel = frame.getStartLabel()
        code = self.emit.emitLABEL(startFuncLabel, frame)
        self.emit.printout(code)

        arrayParams = []
        arrayDecl = []
        varList = SubBody(frame, glenv)
        for decl in consdecl.params:
            varList = self.visit(decl, varList)
            if type(decl.typ) is ArrayType:
                arrayParams.append(varList.sym[0])
        for decl in body.body:
            if type(decl) is VarDecl and type(decl.typ) is ArrayType:
                varList = self.visit(decl, varList)
                arrayDecl.append(varList.sym[0])
            
        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR(
                "this", ClassType(Id(self.className)), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        if isClassInit:
            for symbol in o:
                if type(symbol.mtype) is not MType and symbol.value.init is not None:
                    self.emit.printout(self.visit(symbol.value, frame))

        for symbol in arrayParams:
            idx = symbol.value.value
            typ = symbol.mtype.typ
            self.emit.printout(self.emit.initArrayParams(idx, typ))
        
        for symbol in arrayDecl: #handle array decl
            idx = symbol.value.value
            typ = symbol.mtype.typ
            dimensions = symbol.mtype.dimensions
            self.emit.printout(self.emit.initLocalArraysVars())

        
        # list(map(lambda x: self.visit(x, varList), body.body)) #visit statements
        for stmt in body.body:
            if type(stmt) is VarDecl:
                varList = self.visit(stmt, varList)
            else:
                self.visit(stmt, varList)
        ##########


        endFuncLabel = frame.getEndLabel()
        code = self.emit.emitLABEL(endFuncLabel, frame)
        self.emit.printout(code)
        if type(return_type) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitFuncDecl(self, ast, o):
        frame = Frame(ast.name, ast.return_type)
        self.genMETHOD(ast, o.sym, frame)
        return Symbol(ast.name, MType([x.typ for x in ast.params], ast.return_type), CName(self.className))

    
    def visitVarDecl(self, ast, o):
        name = ast.name
        typ = ast.typ
        init = ast.init
        if o is None: # global
            code = self.emit.emitATTRIBUTE(name, typ, False, "")
            self.emit.printout(code)
            return Symbol(name, typ, ast)

        elif isinstance(o, Frame): # handle init of global
            ic, it = self.visit(ast.init, SubBody(o, None))
            self.emit.printout(ic)
            return self.emit.emitPUTSTATIC(self.className + "/" + ast.name, ast.typ, o)

        # local
        env = o
        idx = o.frame.getNewIndex()
        startLabel = o.frame.getStartLabel()
        endLabel = o.frame.getEndLabel()
        code = self.emit.emitVAR(idx, name, typ, startLabel, endLabel, o.frame)
        self.emit.printout(code)


        if init is not None:
            code, typ = self.visit(init, SubBody(o.frame, None))
            self.emit.printout(code)
            code = self.emit.emitWRITEVAR(name, typ, idx, o.frame)
            self.emit.printout(code)
        return SubBody(o.frame, [Symbol(name, typ, Index(idx))] + env.sym)

    def visitParamDecl(self, ast, o):
        name = ast.name
        typ = ast.typ
        out = ast.out
        env = o
        idx = o.frame.getNewIndex()
        startLabel = o.frame.getStartLabel()
        endLabel = o.frame.getEndLabel()
        code = self.emit.emitVAR(idx, name, typ, startLabel, endLabel, o.frame)
        self.emit.printout(code)
        return SubBody(o.frame, [Symbol(name, typ)] + env.sym)

#NOTE --- Statements
    def visitCallStmt(self, ast, o):
        sym = next(filter(lambda x: ast.name == x.name, o.sym), None)
        cname = sym.value.value
        ctype = sym.mtype
        in_c = ""
        in_t = []
        pos = 0
        for x in ast.args:
            ac, at = self.visit(x, Access(o.frame, o.sym, False, True))
            in_c += ac
            in_t.append(at)
            if type(at) is IntegerType and type(ctype.partype[pos]) is FloatType:
                in_c += self.emit.emitI2F(o.frame)
            if type(at) is ArrayType:
                pass
            pos += 1
        self.emit.printout(in_c)
        self.emit.printout(self.emit.emitINVOKESTATIC(
            cname + "/" + ast.name, ctype, o.frame))
    
    def visitReturnStmt(self, ast, o):
        if not type(o.frame.returnType) is VoidType:
            ec, et = self.visit(ast.expr, Access(o.frame, o.sym, False))
            self.emit.printout(ec)
            if type(et) is IntegerType and type(o.frame.returnType) is FloatType:
                self.emit.printout(self.emit.emitI2F(o.frame))
        code = self.emit.emitRETURN(o.frame.returnType, o.frame)
        self.emit.printout(code)

#NOTE --- Expressions

    def visitIntegerLit(self, ast, o):
        return self.emit.emitPUSHICONST(ast.val, o.frame), IntegerType()
    def visitStringLit(self, ast, o):
        return self.emit.emitPUSHCONST(ast.val, StringType(), o.frame), StringType()
    def visitFloatLit(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.val), o.frame), FloatType()
    def visitBooleanLit(self, ast, o):
        return self.emit.emitPUSHICONST(str(ast.val), o.frame), BooleanType()
    
    
    def visitArrayCell(self, ast, o):
        pass
    def visitArrayLit(self, ast, o):
        pass
    def visitBinExpr(self, ast, o): # op: str, left: Expr, right: Expr
        e1c, e1t = self.visit(ast.left, o)
        e2c, e2t = self.visit(ast.right, o)
        op = ast.op

        if op in ['+', '-', '*', '/']:
            if type(e1t) is type(e2t):
                rt = e1t
            elif type(e1t) is FloatType and type(e2t) is IntegerType:
                e1c += self.emit.emitI2F(o.frame)
                rt = FloatType()
            elif type(e1t) is IntegerLit and type(e2t) is FloatType:
                e2c += self.emit.emitI2F(o.frame)
                rt = FloatType()
            if op in ['+', '-']:
                opcode = self.emit.emitADDOP(op, rt, o.frame)
            else:
                opcode = self.emit.emitMULOP(op, rt, o.frame)
            code = e1c + e2c + opcode
        if op in ['&&', '||', '==', '!=', '<', '>', '<=', '>=']:
            rt = BooleanType()
            opcode = self.emit.emitREOP(op, rt, o.frame)
            code = e1c + e2c + opcode
        if op in ['::']:
            rt = StringType()
            flag = False
            s1 = ""
            for c in e1c:
                if c == '"':
                    flag = True
                if flag is True and c != '"':
                    s1 += c
                if flag is True and c == '"': break
            
            flag1 = False
            s2 = ""
            for c in e2c:
                if flag1 is False and c == '"':
                    flag1 = True
                if flag1 is True and c != '"':
                    s2 += c
                if flag1 is True and c == '"': break
            opcode = self.emit.emitPUSHCONST(s1 + s2, StringType(), o.frame)
            code = opcode
        return code
    def visitUnExpr(self, ast, o): # op: str, val: Expr
        ec, et = self.visit(ast.val, o)
        op = ast.op
        if op == '!':
            rt = BooleanType()
        else:
            rt = et
        return ec, rt
    def visitFuncCall(self, ast, o):
        sym = next(filter(lambda x: ast.name == x.name, o.sym), None)
        cname = sym.value.value
        ctype = sym.mtype
        in_c = ""

        pos = 0
        for x in ast.args:
            ac, at = self.visit(x, Access(o.frame, o.sym, False, True))
            in_c += ac
            if type(at) is IntegerType and type(ctype.partype[pos]) is FloatType:
                in_c += self.emit.emitI2F(o.frame)
            if type(at) is ArrayType:
                pass
            pos += 1
        in_c += self.emit.emitINVOKESTATIC(cname + "/" + ast.name, ctype, o.frame)
        return in_c, ctype.rettype
    def visitId(self, ast, o):
        sym = list(filter(lambda x: x.name == ast.name, o.sym))[0]
        code = ""
        if o.isLeft is True: #write
            if type(sym.value) is not Index: #class
                code += self.emit.emitPUTSTATIC(self.className + '/' + sym.name, sym.mtype, o.frame)
            else:
                code += self.emit.emitWRITEVAR(sym.name, sym.typ, sym.value.vale, o.frame)
        else: #read
            if type(sym.value) is not Index:
                code += self.emit.emitGETSTATIC(self.className + '/' + sym.name, sym.mtype, o.frame)
            else:
                code += self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o.frame)
        return code, sym.mtype