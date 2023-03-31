class Symbol:
    def __init__ (self, name, assign):
        self.name = name
        self.assign = assign
class StaticCheck(Visitor):
    # local: List[VarDecl], body: List[Assign]
    def visitProgram(self, ctx, o):
        o = []
        for decl in ctx.decls:
            o = self.visit(decl, o)
    def visitBlock(self,ctx:Block,o):
        for decl in ctx.local:
            o += self.visit(decl, o)
        for assign in ctx.body:
            o += self.visit(assign, o)
    # name:Id
    def visitVarDecl(self,ctx:VarDecl,o):
        return o + [Symbol(ctx.name, False)]
    def visitNumLit(self, ctx, o): pass
    def visitBoolLit(self, ctx, o): pass
    # lhs: Id, rhs: Exp
    def visitAssign(self, ctx, o):
        rhs = self.visit(ctx.rhs, o)
        lhs = self.visit(ctx.lhs, o)
        self.setAssign(ctx.lhs.name, True, o)
    def setAssign(self, name, assign, o):
        for symbol in o:
            if symbol.name == name:
                symbol.assign = assign
                return
    #name:str
    def visitId(self,ctx,o):
        isAfter = False
        for decl in o:
            if decl.name == ctx.name:
                isAfter = True
                continue
            if isAfter and decl.assign is True:
                raise UnassignedVariable(Id(ctx.name))
# b = (c = 3)
