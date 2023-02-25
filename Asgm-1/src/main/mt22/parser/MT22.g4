grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: decl EOF;

decl: vardecllist | funcdecllist | ;

vardecllist: vardecl vardecllist | vardecl;
funcdecllist: funcdecl funcdecllist | funcdecl;

vardecl: var_shortform | var_fullform;
var_shortform: idlist COLON (atomic_type | AUTO | array_type) SEMI;
var_fullform: temp1=idlist COLON (atomic_type | AUTO) OP_EQ temp2=exprlist {$temp1.text.count(',') == $temp2.text.count(',')}? SEMI;

//class A: private B {}
funcdecl: ID COLON FUNCT func_return_type LB paramlist RB (INHERIT ID)? body;
//[inherit]? [out]? <identifier>: <type>
paramlist: param COMMA paramlist | param;
param: INHERIT? OUT? ID COLON (atomic_type | AUTO) |;

body: block_stmt;


func_return_type: INT
						| VOID
						| FLOAT
						| BOOL
						| STR
						| AUTO
						;
idlist: (ID COMMA) idlist | ID;
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
func_call: ID LB argslist RB;
argslist: arg_prime | ;
arg_prime: arg COMMA arg_prime | arg;
arg: INTLIT | STRINGLIT | FLOATLIT | BOOLLIT | ID;

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
int_term6: int_term7 '[' nonempty_exprlist ']' | int_term7;
int_term7: INTLIT | FLOATLIT | STRINGLIT | ID | subexpr | callexpr;

subexpr: LB expr RB;
callexpr: ID LB exprlist RB;


//statements
//FIXME - fix statements list
stmtslist: stmt stmtslist | ;
stmt: assign_stmt
		| if_stmt 
		| for_stmt 
		| while_stmt 
		| do_while_stmt 
		| break_stmt 
		| continue_stmt 
		| return_stmt
		| block_stmt
		| call_stmt
		;
assign_stmt: (ID | int_term6) OP_EQ expr SEMI;
//if-else
if_stmt: IF LB expr RB stmt (ELSE stmtslist)?;

//for
for_stmt: FOR LB scalar_var OP_EQ init_expr COMMA cond_expr COMMA update_expr RB stmt;
//FIXME - scalar var
scalar_var: ID;
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
return_stmt: RETURN expr SEMI;

//call a function
call_stmt: ID LB exprlist RB SEMI;

//block statements
block_stmt: LP (vardecl | stmtslist) RP;



arraylit: '{' exprlist'}';

//array type

array_type: ARRAY '[' dimension_list ']' OF atomic_type;
dimension_list: (dms COMMA) dimension_list | dms;
dms: INTLIT;

atomic_type: BOOL
				| INT
				| FLOAT 
				| STR
				;



//variables decle


BLOCK_COMMENT: '/*' .*? '*/' -> channel(HIDDEN);
LINE_COMMENT: '//' ~[\r\n]* -> channel(HIDDEN);

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
ID: [a-zA-Z_][a-zA-Z0-9_]*;

FLOATLIT: (INTPART DECPART | INTPART DECPART? EXPPART) {self.text = self.text.replace("_", "")};
INTLIT: INTPART {self.text = self.text.replace("_", "")};
fragment INTPART: '0' | [1-9] [0-9]* ('_'[0-9]+)* ;
fragment DECPART: '.' [0-9]+;
fragment EXPPART: [eE] [+-]? [0-9]+;
STRINGLIT: '"' ( '\\' [bfrnt'"\\] | ~[\n"])* '"' {self.text = self.text[1:-1]};



fragment STRPART: '"' ( '\\' [bfrnt'"\\] | ~[\n"])* '"';
//Separators
SEMI: ';'; 
COMMA: ','; 
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