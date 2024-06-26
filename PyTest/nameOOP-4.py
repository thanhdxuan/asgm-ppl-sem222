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
        o = [{}]
        for decl in ctx.decl:
            o = self.visit(decl, o)
        for stmt in ctx.stmts:
            o = self.visit(stmt, o)
    #name:str
    def visitVarDecl(self,ctx:VarDecl,o):
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        o[0][ctx.name] = None
        return o
    #decl:List[VarDecl],stmts:List[Stmt]
    def visitBlock(self, ctx:Block, o):
        env = [{}] + o
        for decl in ctx.decl:
            env = self.visit(decl, env)
        for stmt in ctx.stmts:
            env = self.visit(stmt, env)
        return o[1:] #  o[0] is local environment
    #lhs:Id,rhs:Exp
    def visitAssign(self,ctx:Assign,o):
        rhs_type = self.visit(ctx.rhs, o)
        lhs_type = self.visit(ctx.lhs, o)
        if lhs_type is None:
            if rhs_type is None:
                raise TypeCannotBeInferred(ctx)
            o[ctx.lhs.name] = rhs_type
            return o
        else:
            if rhs_type is None:
                o[ctx.rhs.name] = lhs_type
                return o
        if type(lhs_type) is not type(rhs_type):
            raise TypeMismatchInStatement(ctx)
    #op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b
    def visitBinOp(self,ctx:BinOp,o):
        op = ctx.op
        e1t = self.visit(ctx.e1, o)
        e2t = self.visit(ctx.e2, o)

        if op in ['+', '-', '*', '/']:
            if e1t is None:
                o[ctx.e1.name] = IntType()
                e1t = IntType()
            if e2t is None:
                o[ctx.e2.name] = IntType()
                e2t = IntType()
            if type(e1t) is not IntType or type(e2t) is not IntType:
                raise TypeMismatchInExpression(ctx)
            return IntType()
        elif op in ['+.', '-.', '*.', '/.']:
            if e1t is None:
                o[ctx.e1.name] = FloatType()
                e1t = FloatType()
            if e2t is None:
                o[ctx.e2.name] = FloatType()
                e2t = FloatType()
            if type(e1t) is not FloatType or type(e2t) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            return FloatType()
        elif op in ['>', '=']:
            if e1t is None:
                o[ctx.e1.name] = IntType()
                e1t = IntType()
            if e2t is None:
                o[ctx.e2.name] = IntType()
                e2t = IntType()
            if type(e1t) is not IntType or type(e2t) is not IntType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        elif op in ['>.', '=.']:
            if e1t is None:
                o[ctx.e1.name] = FloatType()
                e1t = FloatType()
            if e2t is None:
                o[ctx.e2.name] = FloatType()
                e2t = FloatType()
            if type(e1t) is not FloatType or type(e2t) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        elif op in ['&&', '||', '>b', '=b']:
            if e1t is None:
                o[ctx.e1.name] = BoolType()
                e1t = BoolType()
            if e2t is None:
                o[ctx.e2.name] = BoolType()
                e2t = BoolType()
            if type(e1t) is not BoolType or type(e2t) is not BoolType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
    #op:str,e:Exp #op is -,-., !,i2f, floor
    def visitUnOp(self,ctx:UnOp,o):
        op = ctx.op
        et = self.visit(ctx.e, o)
        if op == '-':
            if et is None:
                o[ctx.e.name] = IntType()
                return IntType()
            if type(et) is not IntType:
                raise TypeMismatchInExpression(ctx)
            return IntType()
        if op == '-.':
            if et is None:
                o[ctx.e.name] = FloatType()
                return FloatType()
            if type(et) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            return FloatType()
        if op == '!':
            if et is None:
                setType(ctx.e.name, BoolType(), o)
            if type(et) is not BoolType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        if op == 'i2f':
            if et is None:
                setType(ctx.e.name, IntType(), o)
                return FloatType()
            if type(et) is not IntType:

                raise TypeMismatchInExpression(ctx)
            return FloatType()
        if op == 'floor':
            if et is None:
                setType(ctx.e.name, FloatType(), o)
                return IntType()
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
        for env in o:
            if ctx.name in env:
                return env[ctx.name]
        raise UndeclaredIdentifier(ctx.name)
    def setType(self, name, typ, o):
        for env in o:
            if name in env:
                env[name] = typ
                return
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
