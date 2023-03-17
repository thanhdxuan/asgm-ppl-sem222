from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program([])
    
        # Visit a parse tree produced by MT22Parser#paramlist.
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param.
    def visitParam(self, ctx:MT22Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_return_type.
    def visitFunc_return_type(self, ctx:MT22Parser.Func_return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprprime.
    def visitExprprime(self, ctx:MT22Parser.ExprprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#nonempty_exprlist.
    def visitNonempty_exprlist(self, ctx:MT22Parser.Nonempty_exprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#str_operands.
    def visitStr_operands(self, ctx:MT22Parser.Str_operandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_expr.
    def visitInt_expr(self, ctx:MT22Parser.Int_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_term1.
    def visitInt_term1(self, ctx:MT22Parser.Int_term1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_term2.
    def visitInt_term2(self, ctx:MT22Parser.Int_term2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_term3.
    def visitInt_term3(self, ctx:MT22Parser.Int_term3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_term4.
    def visitInt_term4(self, ctx:MT22Parser.Int_term4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_term5.
    def visitInt_term5(self, ctx:MT22Parser.Int_term5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_term6.
    def visitInt_term6(self, ctx:MT22Parser.Int_term6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_term7.
    def visitInt_term7(self, ctx:MT22Parser.Int_term7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#subexpr.
    def visitSubexpr(self, ctx:MT22Parser.SubexprContext):
        return self.visitChildren(ctx)


    # special_func_callstmt: (special_func_read | special_func_print | special_func_super) SEMI
    def visitSpecial_func_callstmt(self, ctx:MT22Parser.Special_func_callstmtContext):
        if ctx.special_func_read():
            return self.visit(ctx.special_func_read())
        elif self.visit(ctx.special_func_print()):
            return self.visit(ctx.special_func_print())
        return self.visit(ctx.special_func_super())

    # special_func_read: (READ_INT | READ_FLOAT | READ_BOOL | READ_STR | PREVENT_DEFAUT) LB RB
    def visitSpecial_func_read(self, ctx:MT22Parser.Special_func_readContext):
        fucname = None
        if ctx.READ_INT():
            fucname = ctx.READ_INT().getText()
        elif ctx.READ_FLOAT():
            fucname = ctx.READ_FLOAT().getText()
        elif ctx.READ_BOOL():
            fucname = ctx.READ_BOOL().getText()
        elif ctx.READ_STR():
            fucname = ctx.READ_STR().getText()
        else:
            fucname = ctx.PREVENT_DEFAUT().getText()
        exprlist = self.visit(ctx.expr())
        return FuncCall(fucname, exprlist)

    # special_func_print: (PRINT_INT | PRINT_BOOL | PRINT_FLOAT | PRINT_STR) LB expr RB;
    def visitSpecial_func_print(self, ctx:MT22Parser.Special_func_printContext):
        fucname = None
        if ctx.PRINT_INT():
            fucname = ctx.PRINT_INT().getText()
        elif ctx.PRINT_BOOL():
            fucname = ctx.PRINT_BOOL().getText()
        elif ctx.PRINT_FLOAT():
            fucname = ctx.PRINT_BOOL().getText()
        else:
            fucname = ctx.PRINT_STR().getText()
        exprlist = self.visit(ctx.expr())
        return FuncCall(fucname, exprlist)

    # special_func_super: SUPER_FUNC LB exprlist RB
    def visitSpecial_func_super(self, ctx:MT22Parser.Special_func_superContext):
        fucname = ctx.SUPER_FUNC().getText()
        exprlist = self.visit(ctx.exprlist())
        return FuncCall(fucname, exprlist)

    # callexpr: ID LB exprlist RB
    def visitCallexpr(self, ctx:MT22Parser.CallexprContext):
        fucname = ctx.ID().getText()
        exprlist = self.visit(ctx.exprlist())
        return FuncCall(fucname, exprlist)


    # Visit a parse tree produced by MT22Parser#stmtslist.
    def visitStmtslist(self, ctx:MT22Parser.StmtslistContext):
        return self.visitChildren(ctx)


    # stmtprime: stmts stmtprime | stmts
    def visitStmtprime(self, ctx:MT22Parser.StmtprimeContext):
        if ctx.stmtprime():
            return 
    
    # stmts: vardecl | stmt
    def visitStmts(self, ctx:MT22Parser.StmtsContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        return self.visit(ctx.stmt())


    # stmt: assign_stmt
    # 		| if_stmt 
    # 		| for_stmt 
    # 		| while_stmt 
    # 		| do_while_stmt 
    # 		| break_stmt 
    # 		| continue_stmt 
    # 		| return_stmt
    # 		| block_stmt
    # 		| special_func_callstmt
    # 		| call_stmt
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        if ctx.assign_stmt():
            return self.visit(ctx.assign_stmt())
        elif ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        elif ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        elif ctx.while_stmt():
            return self.visit(ctx.while_stmt())
        elif ctx.do_while_stmt():
            return self.visit(ctx.do_while_stmt())
        elif ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        elif ctx.continue_stmt():
            return self.visit(ctx.continue_stmt())
        elif ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        elif ctx.block_stmt():
            return self.visit(ctx.block_stmt())
        elif ctx.special_func_callstmt():
            return self.visit(ctx.special_func_callstmt())
        else: return self.visit(ctx.call_stmt())

    # assign_stmt: ID OP_EQ expr SEMI 
          #| int_term6 OP_EQ expr SEMI
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        if ctx.ID():
            lhs = Id(ctx.ID().getText())
            rhs = self.visit(ctx.expr())
            return AssignStmt(lhs, rhs)
        lhs = self.visit(ctx.int_term6())
        rhs = self.visit(ctx.expr())
        return AssignStmt(lhs, rhs)

    # if_stmt: IF LB expr RB stmt
    #    | IF LB expr RB stmt ELSE stmt;

    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        cond = self.visit(ctx.expr())
        tstmt = self.visit(ctx.stmt(0))
        fstmt = None
        if ctx.ELSE():
            fstmt = self.visit(ctx.stmt(1))
        return IfStmt(cond, tstmt, fstmt)            


    # for_stmt: FOR LB init_expr COMMA cond_expr COMMA update_expr RB stmt
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        init = self.visit(ctx.init_expr())
        cond = self.visit(ctx.cond_expr())
        upd = self.visit(ctx.update_expr())
        stmts = self.visit(ctx.stmt())
        return ForStmt(init, cond, upd, stmts)

    #init_expr: ID OP_EQ expr 
    #      | int_term6 OP_EQ expr;
    def visitInit_expr(self, ctx:MT22Parser.Init_exprContext):
        if ctx.ID():
            lhs = Id(ctx.ID().getText())
            rhs = self.visit(ctx.expr())
            return AssignStmt(lhs, rhs)
        lhs = self.visit(ctx.int_term6())
        rhs = self.visit(ctx.expr())
        return AssignStmt(lhs, rhs)

    # cond_expr: expr
    def visitCond_expr(self, ctx:MT22Parser.Cond_exprContext):
        return self.visit(ctx.expr())

    # update_expr: expr;
    def visitUpdate_expr(self, ctx:MT22Parser.Update_exprContext):
        return self.visit(ctx.expr());

    # while_stmt: WHILE LB cond_expr RB stmt;
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        stmt = self.visit(ctx.stmt())
        expr = self.visit(ctx.cond_expr())
        return WhileStmt(expr, stmt)


    # do_while_stmt: DO block_stmt WHILE LB cond_expr RB SEMI;
    def visitDo_while_stmt(self, ctx:MT22Parser.Do_while_stmtContext):
        blockstmt = self.visit(ctx.block_stmt())
        expr = self.visit(ctx.cond_expr())
        return DoWhileStmt(expr, blockstmt)

    # break_stmt: BREAK SEMI;
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return BreakStmt()

    # continue_stmt: CONTINUE SEMI;
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return ContinueStmt()

    # return_stmt: RETURN SEMI | RETURN expr SEMI;
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        if ctx.getChildCount() == 2:
            return ReturnStmt()
        expr = self.visit(ctx.expr())
        return ReturnStmt(expr)


    # call_stmt: ID LB exprlist RB SEMI;
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        return CallStmt(ctx.ID().getText(), self.visit(ctx.exprlist()))

    # block_stmt: LP stmtslist RP;
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return BlockStmt(self.visit(ctx.stmtslist()))
    
    # arraylit: LP exprlist RP
    #     | LP arraylit RP
    #     | LP RP;
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        if ctx.arraylit():
            return ArrayLit(self.visit(ctx.arraylit()))
        elif ctx.exprlist():
            return ArrayLit(self.visit(ctx.exprlist()))
        else: return ArrayLit([])
    
    # array_type: ARRAY LC dimension_list RC OF atomic_type;
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        dimensions = self.visit(ctx.dimension_list())
        typ = self.visit(ctx.atomic_type())
        return ArrayType(dimensions, typ)

    # dimension_list: (INTLIT COMMA) dimension_list | INTLIT;
    def visitDimension_list(self, ctx:MT22Parser.Dimension_listContext):
        if ctx.getChildCount() == 1:
            return [IntegerLit(int(ctx.INTLIT().getText()))]
        return [IntegerLit(int(ctx.INTLIT().getText()))] + self.visit(ctx.dimension_list())
    
    # idlist: (ID COMMA) idlist | ID;
    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        return [Id(ctx.ID().getText())] + self.visit(ctx.idlist())
    
    # atomic_type: BOOL
	#			| INT
	#			| FLOAT 
	#			| STR
	#			;
    def visitAtomic_type(self, ctx: MT22Parser.Atomic_typeContext):
        if ctx.BOOL():
            return BooleanType()
        elif ctx.INT():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        else: return StringType()
    
