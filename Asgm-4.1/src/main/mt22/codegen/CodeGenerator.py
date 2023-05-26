from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


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
                Symbol("printInteger", MType([IntegerType()],
                       VoidType()), CName(self.libName)),
                Symbol("printString", MType(StringType(), VoidType()), CName(self.libName))
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
        
        staticDecl = self.env
        for x in ast.decls:
            if type(x) is FuncDecl:
                partype = [i.typ for i in x.params]
                staticDecl = [Symbol(x.name.lower(), MType(partype, x.return_type), CName(self.className))] + staticDecl
            else:
                newSym = self.visit(x, SubBody(None, None, isGlobal=True))
                staticDecl = [newSym] + staticDecl
        
        e = SubBody(None, staticDecl)
        [self.visit(x, e) for x in ast.decls if type(x) is FuncDecl]

        # generate default constructor
        # self.genMETHOD(FuncDecl(Id("<init>"), None, list(), None, BlockStmt(list())), c, Frame("<init>", VoidType))

        self.emit.emitEPILOG()
        return c

    # def visitClassDecl(self, ast, c):
    #     self.className = ast.classname.name
    #     self.emit = Emitter(self.path+"/" + self.className + ".j")
    #     self.emit.printout(self.emit.emitPROLOG(
    #         self.className, "java.lang.Object"))
    #     [self.visit(ele, SubBody(None, self.env))
    #      for ele in ast.memlist if type(ele) == MethodDecl]
    #     # generate default constructor
    #     self.genMETHOD(MethodDecl(Instance(), Id("<init>"), list(
    #     ), None, Block([], [])), c, Frame("<init>", VoidType()))
    #     self.emit.emitEPILOG()
    #     return c

    def genMETHOD(self, consdecl, o, frame):
        isInit = consdecl.return_type is None

        isMain = consdecl.name == "main" and len(
            consdecl.params) == 0 and type(consdecl.return_type) is VoidType
        
        return_type = VoidType() if isInit else consdecl.return_type
        
        methodName = "<init>" if isInit else consdecl.name
        intype = [ArrayType(0, StringType())] if isMain else list(
            map(lambda x: x.typ, consdecl.param))
        mtype = MType(intype, return_type)

        self.emit.printout(self.emit.emitMETHOD(
            methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        # if isInit:
        #     self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
        #         Id(self.className)), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(
                0, StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            local = reduce(lambda env, ele: SubBody(
                frame, [self.visit(ele, env)]+env.sym), consdecl.param, SubBody(frame, []))
            glenv = local.sym+glenv

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        # if isInit:
        #     self.emit.printout(self.emit.emitREADVAR(
        #         "this", ClassType(Id(self.className)), 0, frame))
        #     self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.body))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(return_type) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitFuncDecl(self, ast, o):
        frame = Frame(ast.name, ast.return_type)
        self.genMETHOD(ast, o.sym, frame)
        return Symbol(ast.name, MType([x.typ for x in ast.params], ast.return_type), CName(self.className))

    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = next(filter(lambda x: ast.name == x.name, nenv), None)
        cname = sym.value.value
        ctype = sym.mtype
        in_ = ("", list())
        for x in ast.args:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(
            cname + "/" + ast.name, ctype, frame))

    def visitIntegerLit(self, ast, o):
        return self.emit.emitPUSHICONST(ast.val, o.frame), IntegerType()
    def visitBinaryOp(self, ast, o):
        e1c, e1t = self.visit(ast.left, o)
        e2c, e2t = self.visit(ast.right, o)
        return e1c + e2c + self.emit.emitADDOP(ast.op, e1t, o.frame), e1t
