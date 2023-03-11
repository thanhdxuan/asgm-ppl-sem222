grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}
program: decl EOF;

// declarelist: decl declarelist | decl;

decl: (funcdecl | vardecl) decl | ;

funcdecl: ID COLON FUNCT func_return_type LB paramlist RB (INHERIT ID)? body;
body: block_stmt;


vardecl: var_shortform | var_fullform;
var_shortform: idlist COLON (atomic_type | AUTO | array_type) SEMI;
// var_fullform: idlist COLON (atomic_type | AUTO) OP_EQ nonempty_exprlist  SEMI;
var_fullform: helpper SEMI;
base: ID COLON atomic_type OP_EQ expr;
helpper: ID COMMA helpper COMMA expr | base;

// ( {$i<$n}? INT {$i=$i+1;} )*
// FIXME: a,b: array [2, 2, 3] of integer = {{3,2},{1,2}}, {{1,2},{1,2}};
//class A: private B {}
//[inherit]? [out]? <identifier>: <type>
paramlist: param COMMA paramlist | param;
param: INHERIT? OUT? ID COLON (atomic_type | AUTO) | ;



func_return_type: INT
						| VOID
						| FLOAT
						| BOOL
						| STR
						| AUTO
						| ARRAY
						;
//Arithmetic operators
LOGIC_OP: OP_AND
			| OP_OR;

RELATION_OP: OP_EQ_EQ
				| OP_INEQ
				| OP_LESS
				| OP_LESS_OR_EQ
				| OP_GREATER
				| OP_GREA_OR_EQ
				;
//function calls
// func_call: ID LB argslist RB SEMI;
// argslist: arg_prime | ;
// arg_prime: arg COMMA arg_prime | arg;
// arg: INTLIT | STRINGLIT | FLOATLIT | BOOLLIT | ID;

exprlist: exprprime | ;
exprprime: expr COMMA exprprime | expr;

//non-empty exprlist
nonempty_exprlist: expr COMMA nonempty_exprlist | expr;
//expression
expr: str_operands OP_STR_CONCAT str_operands | str_operands; //none - associative
str_operands: int_expr;
int_expr: int_term1 RELATION_OP int_term1 | int_term1;
int_term1: int_term1 LOGIC_OP int_term2 | int_term2;
int_term2: int_term2 (OP_ADD | OP_MINUS) int_term3 | int_term3;
int_term3: int_term3 (OP_MUL | OP_MOD | OP_DIV) int_term4 | int_term4;
int_term4: OP_NOT int_term4 | int_term5;

int_term5: OP_MINUS int_term5 | int_term6; // op_type: sign example: -4
int_term6: int_term7 LC nonempty_exprlist RC | int_term7;
int_term7: special_func_super | special_func_read | arraylit | INTLIT | FLOATLIT | STRINGLIT | BOOLLIT | ID | subexpr | callexpr;

subexpr: LB expr RB;

//special functions
special_func_callstmt: (special_func_read | special_func_print | special_func_super) SEMI;
special_func_read: (READ_INT | READ_FLOAT | READ_BOOL | READ_STR | PREVENT_DEFAUT) LB RB;
special_func_print: (PRINT_INT | PRINT_BOOL | PRINT_FLOAT | PRINT_STR) LB expr RB;
special_func_super: SUPER_FUNC LB exprlist RB;


callexpr: ID LB exprlist RB;


//statements
//FIXME - fix statements list
stmtslist: (vardecl | stmt) stmtslist | ;
stmt: assign_stmt
		| if_stmt 
		| for_stmt 
		| while_stmt 
		| do_while_stmt 
		| break_stmt 
		| continue_stmt 
		| return_stmt
		| block_stmt
		| special_func_callstmt
		| call_stmt
		;
assign_stmt: (ID | int_term6) OP_EQ expr SEMI;
//if-else
if_stmt: IF LB expr RB stmt (ELSE stmt)?;

//for
for_stmt: FOR LB (ID | int_term6) OP_EQ init_expr COMMA cond_expr COMMA update_expr RB stmt;
//FIXME - scalar var
// scalar_var: ID;
init_expr: expr; cond_expr: expr; update_expr: expr;

//while
while_stmt: WHILE LB cond_expr RB stmt;

//do-while
do_while_stmt: DO stmt WHILE LB cond_expr RB SEMI;

//break
break_stmt: BREAK SEMI;

//continue
continue_stmt: CONTINUE SEMI;

//return
return_stmt: RETURN expr? SEMI;

//call a function
call_stmt: ID LB exprlist RB SEMI;

//block statements
block_stmt: LP stmtslist RP;




arraylit: LP (exprlist | arraylit | ) RP;
//{{1,2,3},{7,8,7},{8,8,8}}

//array type

array_type: ARRAY LC dimension_list RC OF atomic_type;
dimension_list: (INTLIT COMMA) dimension_list | INTLIT;

atomic_type: BOOL
				| INT
				| FLOAT 
				| STR
				;



//variables decle


BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

//keywords

AUTO: 'auto'; 
INT: 'integer';
VOID: 'void'; 
ARRAY: 'array';
 BREAK: 'break';
FLOAT: 'float'; 
RETURN: 'return'; 
OUT: 'out'; 
BOOL: 'boolean';
FOR: 'for'; 
STR: 'string'; 
CONTINUE: 'continue';
DO: 'do'; 
FUNCT: 'function';
OF: 'of'; 
ELSE: 'else'; 
IF: 'if'; 
WHILE: 'while'; 
INHERIT: 'inherit';
READ_INT: 'readInteger';
PRINT_INT: 'printInteger';
READ_FLOAT: 'readFloat';
PRINT_FLOAT: 'writeFloat';
READ_BOOL: 'readBoolean';
PRINT_BOOL: 'printBoolean';
READ_STR: 'readString';
PRINT_STR: 'printString';
SUPER_FUNC: 'super';
PREVENT_DEFAUT: 'preventDefault';

//Operators
OP_STR_CONCAT: '::';
OP_ADD: '+'; 
OP_MINUS: '-'; 
OP_MUL: '*'; 
OP_DIV: '/'; 
OP_MOD: '%'; 
OP_NOT: '!';
OP_AND: '&&'; 
OP_OR: '||'; 
OP_EQ_EQ: '==';
OP_EQ: '=';
OP_INEQ: '!='; 
OP_LESS: '<'; 
OP_GREATER: '>';
OP_LESS_OR_EQ: '<='; 
OP_GREA_OR_EQ: '>=';

//Checkcommit
//Literals
BOOLLIT: 'true' | 'false';
idlist: (ID COMMA) idlist | ID;
ID: [a-zA-Z_][a-zA-Z0-9_]*;

FLOATLIT: (INTPART? DECPART EXPPART | INTPART DECPART? EXPPART | INTPART DECPART EXPPART?) {self.text = self.text.replace("_", "")};
INTLIT: INTPART {self.text = self.text.replace("_", "")};
fragment INTPART: '0' | [1-9] [0-9]* ('_'[0-9]+)* ;
fragment DECPART: '.' [0-9]*;
fragment EXPPART: [eE] [+-]? [0-9]+;
STRINGLIT: '"' ( '\\' [bfrnt'"\\] | ~[\n"])* '"' {self.text = self.text[1:-1]};


fragment STRPART: '"' ( '\\' [bfrnt'"\\] | ~[\n"])* '"';
//Separators
SEMI: ';'; 
COMMA: ','; 
LC: '[';
RC: ']';
LB: '('; 
RB: ')'; 
LP: '{'; 
RP: '}'; 
DOT: '.'; 
COLON: ':';

WS: [ \b\t\r\n]+ -> skip; // skip spaces, tabs, newlines
ERROR_CHAR: . {raise ErrorToken(self.text)};
ILLEGAL_ESCAPE: '\\' (~[bfrnt'\\])* {raise IllegalEscape(self.text)};
UNCLOSE_STRING: '"' [.]* {raise UncloseString(self.text)};