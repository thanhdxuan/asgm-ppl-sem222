class Type(ABC): pass
class IntType(Type): pass
class BoolType(Type): pass
class FloatType(Type): pass
class NoType(Type): pass
class Symbol:
    def __init__ (self, name, typ):
        self.name = name
        self.typ = typ
class StaticCheck(Visitor):
    #decl:List[VarDecl],stmts:List[Assign]
    def visitProgram(self,ctx:Program,o):
        o = [[]]
        for decl in ctx.decl:
            o = self.visit(decl, o)
        for stmt in ctx.stmts:
            self.visit(stmt, o)
    #name:str
    def visitVarDecl(self,ctx:VarDecl,o):
        for symbol in o[0]:
            if symbol.name == ctx.name:
                raise Redeclared(ctx)
        o[0] += [Symbol(ctx.name, NoType())]
        return o
    #decl:List[VarDecl],stmts:List[Stmt]
    def visitBlock(self, ctx:Block, o):
        env = [[]] + o
        for decl in ctx.decl:
            env = self.visit(decl, env)
        for stmt in ctx.stmts:
            self.visit(stmt, env)
    #lhs:Id,rhs:Exp
    def visitAssign(self,ctx:Assign,o):
        rhs_type = self.visit(ctx.rhs, o)
        lhs_type = self.visit(ctx.lhs, o)
        if type(lhs_type) is NoType and type(rhs_type) is NoType:
            raise TypeCannotBeInferred(ctx)
        if type(lhs_type) is NoType:
            self.setType(ctx.lhs.name, rhs_type, o)
            return
        if type(rhs_type) is NoType:
            self.setType(ctx.rhs.name, lhs_type, o)
            return
        if type(rhs_type) is not type(lhs_type):
            raise TypeMismatchInStatement(ctx)
    def setType(self, name, typ, env):
        for symbol_lst in env:
            for symbol in symbol_lst:
                if symbol.name == name:
                    symbol.typ = typ
                    return typ
    #op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b
    def visitBinOp(self,ctx:BinOp,o):
        op = ctx.op
        e1t = self.visit(ctx.e1, o)
        e2t = self.visit(ctx.e2, o)
        if op in ['+', '-', '*', '/']:
            if type(e1t) is NoType:
                e1t = self.setType(ctx.e1.name, IntType(), o)
            if type(e2t) is NoType:
                e2t = self.setType(ctx.e2.name, IntType(), o)
            if type(e1t) is not IntType or type(e2t) is not IntType:
                raise TypeMismatchInExpression(ctx)
            return IntType()
        elif op in ['+.', '-.', '*.', '/.']:
            if type(e1t) is NoType:
                e1t = self.setType(ctx.e1.name, FloatType(), o)
            if type(e2t) is NoType:
                e2t = self.setType(ctx.e2.name, FloatType(), o)
            if type(e1t) is not FloatType or type(e2t) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            return FloatType()
        elif op in ['>', '=']:
            if type(e1t) is NoType:
                e1t = self.setType(ctx.e1.name, IntType(), o)
            if type(e2t) is NoType:
                e2t = self.setType(ctx.e2.name, IntType(), o)
            if type(e1t) is not IntType or type(e2t) is not IntType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        elif op in ['>.', '=.']:
            if type(e1t) is NoType:
                e1t = self.setType(ctx.e1.name, FloatType(), o)
            if type(e2t) is NoType:
                e2t = self.setType(ctx.e2.name, FloatType(), o)
            if type(e1t) is not FloatType or type(e2t) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        elif op in ['&&', '||', '>b', '=b']:
            if type(e1t) is NoType:
                e1t = self.setType(ctx.e1.name, BoolType(), o)
            if type(e2t) is NoType:
                e2t = self.setType(ctx.e2.name, BoolType(), o)
            if type(e1t) is not BoolType or type(e2t) is not BoolType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
    #op:str,e:Exp #op is -,-., !,i2f, floor
    def visitUnOp(self,ctx:UnOp,o):
        op = ctx.op
        et = self.visit(ctx.e, o)
        if op == '-':
            if type(et) is NoType:
                et = self.setType(ctx.e.name, IntType(), o)
            if type(et) is not IntType:
                raise TypeMismatchInExpression(ctx)
            return IntType()
        if op == '-.':
            if type(et) is NoType:
                et = self.setType(ctx.e.name, FloatType(), o)
            if type(et) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            return FloatType()
        if op == '!':
            if type(et) is NoType:
                et = self.setType(ctx.e.name, BoolType(), o)
            if type(et) is not BoolType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        if op == 'i2f':
            if type(et) is NoType:
                et = self.setType(ctx.e.name, IntType(), o)
            if type(et) is not IntType:
                raise TypeMismatchInExpression(ctx)
            return FloatType()
        if op == 'floor':
            if type(et) is NoType:
                et = self.setType(ctx.e.name, FloatType(), o)
            if type(et) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            return IntType()

    def visitIntLit(self,ctx:IntLit,o):
        # print(ctx.val)
        return IntType()

    def visitFloatLit(self,ctx,o):
        return FloatType()

    def visitBoolLit(self,ctx,o):
        # print(ctx.val)
        return BoolType()
    #name:str
    def visitId(self,ctx,o):
        for symbol_lst in o:
            for symbol in symbol_lst:
                if symbol.name == ctx.name:
                    return symbol.typ
        raise UndeclaredIdentifier(ctx.name)
"""
var x, t
x = 3
##(x, int), (t, None)
{
    ##env = []
    var x;
    ## env =(y, None)
    x = 3.0
    t = x;
    ## env = (x, int), (t, None), (y, int)
    {
        var z;
        t = 3;
        ## env = (x, int), (t, int), (y, int), (z, None)
        y = t -. (i2f)(x)
    }
}
"""
