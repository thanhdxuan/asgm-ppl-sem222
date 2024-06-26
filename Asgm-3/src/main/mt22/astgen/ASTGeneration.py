from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    # program: decl EOF;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        decl = self.visit(ctx.decl())
        return Program(decl)
    
    # decl: (funcdecl | vardecl) decl | ;
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        if ctx.getChildCount() == 0:
            return []
        decl = None
        if ctx.funcdecl():
            decl = self.visit(ctx.funcdecl())
        else:
            decl = self.visit(ctx.vardecl())
        return decl + self.visit(ctx.decl())

    # funcdecl: ID COLON FUNCT func_return_type LB paramlist RB (INHERIT ID)? body;
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        name = ctx.ID(0).getText()
        typ = self.visit(ctx.func_return_type())
        paramlst = self.visit(ctx.paramlist())
        inherit_id = None
        if ctx.INHERIT():
            inherit_id = ctx.ID(1).getText()
        body = self.visit(ctx.body())
        return [FuncDecl(name, typ, paramlst, inherit_id, body)]
    # body: block_stmt;
    def visitBody(self, ctx:MT22Parser.BodyContext):
        return self.visit(ctx.block_stmt())

    # vardecl: var_shortform | var_fullform;
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visit(ctx.getChild(0))
    # var_shortform: idlist COLON (atomic_type | AUTO | array_type) SEMI;
    def visitVar_shortform(self, ctx:MT22Parser.Var_shortformContext):
        ids = self.visit(ctx.idlist()) #['x', 'y',...] 
        typ = None #Type()
        if ctx.atomic_type():
            typ = self.visit(ctx.atomic_type())
        elif ctx.AUTO():
            typ = AutoType()
        else: #array
            typ = self.visit(ctx.array_type())
        return [VarDecl(name, typ) for name in ids]


    # var_fullform: helpper SEMI;
    def visitVar_fullform(self, ctx:MT22Parser.Var_fullformContext):
        lst = self.visit(ctx.helpper())
        typ = lst[2] # Type
        namelst = lst[0] # [a, b, c]
        exprlst = lst[1] # [1, 2, 3] => [VarDecl(a, Type, 1)]

        return [VarDecl(namelst[i], typ, exprlst[i]) for i in range(len(namelst))]
        # a, b, c: integer = 1, 2, 3
        # [[a, 3], [b, 2], [c, int, 1]]

    # base: ID COLON (atomic_type | array_type | AUTO) OP_EQ expr;
    def visitBase(self, ctx:MT22Parser.BaseContext):
        name = ctx.ID().getText()
        typ = None #Type()
        if ctx.atomic_type():
            typ = self.visit(ctx.atomic_type())
        elif ctx.AUTO():
            typ = AutoType()
        else:
            typ = self.visit(ctx.array_type())
        expr = self.visit(ctx.expr())
        return [[name], [expr], typ]

    # helpper: ID COMMA helpper COMMA expr | base;
    def visitHelpper(self, ctx:MT22Parser.HelpperContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.base())
        name = ctx.ID().getText() #'x','y','z',...
        expr = self.visit(ctx.expr())
        helpper = self.visit(ctx.helpper()) #[[name], [expr], typ]
        helpper[0] = [name] + helpper[0]
        helpper[1] = helpper[1] + [expr]
        return helpper
        # a, .. , expr
    # param: INHERIT? OUT? ID COLON param_typ;
    def visitParam(self, ctx:MT22Parser.ParamContext):
        inherit = False
        out = False
        name = ctx.ID().getText()
        if ctx.INHERIT():
            inherit = True
        if ctx.OUT():
            out = True
        typ = self.visit(ctx.param_typ())
        return ParamDecl(name, typ, out, inherit)

    # param_typ: atomic_type | AUTO | array_type;
    def visitParam_typ(self, ctx:MT22Parser.Param_typContext):
        if ctx.atomic_type():
            return self.visit(ctx.atomic_type())
        elif ctx.AUTO():
            return AutoType()
        else:
            return self.visit(ctx.array_type())

    # paramlist: paramprime | ;
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        return self.visit(ctx.paramprime()) if ctx.paramprime() else []

    # paramprime: param COMMA paramprime | param;
    def visitParamprime(self, ctx:MT22Parser.ParamprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.param())]
        return [self.visit(ctx.param())] + self.visit(ctx.paramprime())
    #   func_return_type: atomic_type
    #               | AUTO
    #               | array_type
    #               | VOID
    #   						;
    def visitFunc_return_type(self, ctx:MT22Parser.Func_return_typeContext):
        if ctx.atomic_type():
            return self.visit(ctx.atomic_type())
        elif ctx.VOID():
            return VoidType()
        elif ctx.AUTO():
            return AutoType()
        else:
            return self.visit(ctx.array_type())
    #logic_op: OP_AND
    #			| OP_OR;
    def visitLogic_op(self, ctx:MT22Parser.Logic_opContext):
        return ctx.getChild(0).getText()

    #relation_op: OP_EQ_EQ
    #				| OP_INEQ
    #				| OP_LESS
    #				| OP_LESS_OR_EQ
    #				| OP_GREATER
    #				| OP_GREA_OR_EQ
    def visitRelation_op(self, ctx:MT22Parser.Relation_opContext):
        op = ctx.getChild(0)
        return op.getText()

    # exprlist: exprprime | ;
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        if ctx.exprprime():
            return self.visit(ctx.exprprime())
        return []

    # exprprime: expr COMMA exprprime | expr;
    def visitExprprime(self, ctx:MT22Parser.ExprprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.exprprime())

    # nonempty_exprlist: expr COMMA nonempty_exprlist | expr;
    def visitNonempty_exprlist(self, ctx:MT22Parser.Nonempty_exprlistContext):
        if ctx.COMMA():
            return [self.visit(ctx.expr())] + self.visit(ctx.nonempty_exprlist())
        return [self.visit(ctx.expr())]

    # expr: str_operands OP_STR_CONCAT str_operands | str_operands; //none - associative
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.str_operands(0))
        op = ctx.OP_STR_CONCAT().getText()
        left = self.visit(ctx.str_operands(0))
        right = self.visit(ctx.str_operands(1))
        return BinExpr(op, left, right)
    # str_operands: int_expr
    def visitStr_operands(self, ctx:MT22Parser.Str_operandsContext):
        return self.visit(ctx.int_expr())


    # int_expr: int_term1 relation_op int_term1 | int_term1;
    def visitInt_expr(self, ctx:MT22Parser.Int_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.int_term1(0))
        op = self.visit(ctx.relation_op())
        left = self.visit(ctx.int_term1(0))
        right = self.visit(ctx.int_term1(1))
        return BinExpr(op, left, right)

    # int_term1: int_term1 logic_op int_term2 | int_term2;
    def visitInt_term1(self, ctx:MT22Parser.Int_term1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.int_term2())
        op = self.visit(ctx.logic_op())
        left = self.visit(ctx.int_term1())
        right = self.visit(ctx.int_term2())
        return BinExpr(op, left, right)

    # int_term2: int_term2 (OP_ADD | OP_MINUS) int_term3 | int_term3;
    def visitInt_term2(self, ctx:MT22Parser.Int_term2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.int_term3())
        op = None
        if ctx.OP_ADD():
            op = ctx.OP_ADD().getText()
        else:
            op = ctx.OP_MINUS().getText()
        left = self.visit(ctx.int_term2())
        right = self.visit(ctx.int_term3())
        return BinExpr(op, left, right)

    # int_term3: int_term3 (OP_MUL | OP_MOD | OP_DIV) int_term4 | int_term4;
    def visitInt_term3(self, ctx:MT22Parser.Int_term3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.int_term4())
        op = None
        if ctx.OP_MUL():
            op = ctx.OP_MUL().getText()
        elif ctx.OP_MOD():
            op = ctx.OP_MOD().getText()
        else:
            op = ctx.OP_DIV().getText()
        left = self.visit(ctx.int_term3())
        right = self.visit(ctx.int_term4())
        return BinExpr(op, left, right)


    # int_term4: OP_NOT int_term4 | int_term5;
    def visitInt_term4(self, ctx:MT22Parser.Int_term4Context):
        if ctx.OP_NOT():
            op = ctx.OP_NOT().getText()
            val = self.visit(ctx.int_term4())
            return UnExpr(op, val)
        return self.visit(ctx.int_term5())

    # int_term5: OP_MINUS int_term5 | int_term6; 
    def visitInt_term5(self, ctx:MT22Parser.Int_term5Context):
        if ctx.OP_MINUS():
            op = ctx.OP_MINUS().getText()
            val = self.visit(ctx.int_term5())
            return UnExpr(op, val)
        return self.visit(ctx.int_term6())

    # int_term6: ID LC nonempty_exprlist RC | int_term7; //index operator
    def visitInt_term6(self, ctx:MT22Parser.Int_term6Context): #index operators - array cell
        if ctx.LC():
            name = ctx.ID().getText()
            expr = self.visit(ctx.nonempty_exprlist())
            return ArrayCell(name, expr)
        return self.visit(ctx.int_term7())
            

    # int_term7: special_func_super_expr | special_func_read_expr | special_func_print_expr
    #           | arraylit | INTLIT | FLOATLIT | STRINGLIT 
    #           | BOOLLIT | ID | subexpr | callexpr;
    def visitInt_term7(self, ctx:MT22Parser.Int_term7Context):
        if ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            fstr = ctx.FLOATLIT().getText()
            if fstr[0] == '.':
                fstr = '0' + fstr
            return FloatLit(float(fstr))
        elif ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        elif ctx.BOOLLIT():
            return BooleanLit(ctx.BOOLLIT().getText() == "true")
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.subexpr():
            return self.visit(ctx.subexpr())
        elif ctx.callexpr():
            return self.visit(ctx.callexpr())
        elif ctx.arraylit():
            return self.visit(ctx.arraylit())
        elif ctx.special_func_super_expr():
            return self.visit(ctx.special_func_super_expr())
        elif ctx.special_func_read_expr():
            return self.visit(ctx.special_func_read_expr())
        else:
            return self.visit(ctx.special_func_print_expr())

    # subexpr: LB expr RB
    def visitSubexpr(self, ctx:MT22Parser.SubexprContext):
        return self.visit(ctx.expr())

    def visitSpecial_func_read_expr(self, ctx:MT22Parser.Special_func_read_exprContext):
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
        return FuncCall(fucname, [])

    # special_func_print: (PRINT_INT | PRINT_BOOL | PRINT_FLOAT | PRINT_STR) LB expr RB;
    def visitSpecial_func_print_expr(self, ctx:MT22Parser.Special_func_print_exprContext):
        fucname = None
        if ctx.PRINT_INT():
            fucname = ctx.PRINT_INT().getText()
        elif ctx.PRINT_BOOL():
            fucname = ctx.PRINT_BOOL().getText()
        elif ctx.PRINT_FLOAT():
            fucname = ctx.PRINT_FLOAT().getText()
        else:
            fucname = ctx.PRINT_STR().getText()
        exprlist = [self.visit(ctx.expr())]
        return FuncCall(fucname, exprlist)

    # special_func_super: SUPER_FUNC LB exprlist RB
    def visitSpecial_func_super_expr(self, ctx:MT22Parser.Special_func_super_exprContext):
        fucname = ctx.SUPER_FUNC().getText()
        exprlist = self.visit(ctx.exprlist())
        return FuncCall(fucname, exprlist)

    # special_func_callstmt: (specialfunc_read | specialfunc_print | specialfunc_super) SEMI
    def visitSpecial_func_callstmt(self, ctx:MT22Parser.Special_func_callstmtContext):
        if ctx.specialfunc_read():
            return self.visit(ctx.specialfunc_read())
        elif ctx.specialfunc_print():
            return self.visit(ctx.specialfunc_print())
        else:
            return self.visit(ctx.specialfunc_super())

    # special_func_read: (READ_INT | READ_FLOAT | READ_BOOL | READ_STR | PREVENT_DEFAUT) LB RB
    def visitSpecialfunc_read(self, ctx:MT22Parser.Specialfunc_readContext):
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
        return CallStmt(fucname, [])

    # special_func_print: (PRINT_INT | PRINT_BOOL | PRINT_FLOAT | PRINT_STR) LB expr RB;
    def visitSpecialfunc_print(self, ctx:MT22Parser.Specialfunc_printContext):
        fucname = ctx.getChild(0).getText()
        # if ctx.PRINT_INT():
        #     fucname = ctx.PRINT_INT().getText()
        # elif ctx.PRINT_BOOL():
        #     fucname = ctx.PRINT_BOOL().getText()
        # elif ctx.PRINT_FLOAT():
        #     fucname = ctx.PRINT_FLOAT().getText()
        # else:
        #     fucname = ctx.PRINT_STR().getText()
        exprlist = [self.visit(ctx.expr())]
        return CallStmt(fucname, exprlist)

    # special_func_super: SUPER_FUNC LB exprlist RB
    def visitSpecialfunc_super(self, ctx:MT22Parser.Specialfunc_superContext):
        fucname = ctx.SUPER_FUNC().getText()
        exprlist = self.visit(ctx.exprlist())
        return CallStmt(fucname, exprlist)

    # callexpr: ID LB exprlist RB
    def visitCallexpr(self, ctx:MT22Parser.CallexprContext):
        fucname = ctx.ID().getText()
        exprlist = self.visit(ctx.exprlist())
        return FuncCall(fucname, exprlist)


    # stmtslist: stmtprime | ;
    def visitStmtslist(self, ctx:MT22Parser.StmtslistContext):
        if ctx.stmtprime():
            return self.visit(ctx.stmtprime())
        return []

    # stmtprime: stmts stmtprime | stmts
    def visitStmtprime(self, ctx:MT22Parser.StmtprimeContext):
        if ctx.stmtprime():
            return self.visit(ctx.stmts()) + self.visit(ctx.stmtprime())
        return self.visit(ctx.stmts())
    
    # stmts: vardecl | stmt
    def visitStmts(self, ctx:MT22Parser.StmtsContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl()) #[Vardecl(..)]
        return [self.visit(ctx.stmt())] #[Stmt(..)]


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
        else:
            return self.visit(ctx.call_stmt())

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
            return [int(ctx.INTLIT().getText())]
        return [int(ctx.INTLIT().getText())] + self.visit(ctx.dimension_list())
    
    # idlist: (ID COMMA) idlist | ID;
    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [ctx.ID().getText()]
        return [ctx.ID().getText()] + self.visit(ctx.idlist())
    
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
    
