grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: decl EOF;

decl: vardecl | funcdecl;

vardecl: var_shortform | var_fullform;
var_shortform: idlist COLON (atomic_type | AUTO) SEMI;
var_fullform: temp1=idlist COLON (atomic_type | AUTO) OP_EQ temp2=exprlist {$temp1.text.count(',') == $temp2.text.count(',')}? SEMI;

//class A: private B {}
funcdecl: ID COLON FUNCT func_return_type LB paramlist RB (INHERIT ID)? LP body RP;
//[inherit]? [out]? <identifier>: <type>
paramlist: param COMMA paramlist | param;
param: INHERIT? OUT? ID COLON (atomic_type | AUTO) |;

body: 'body';


func_return_type: INT
						| VOID
						| FLOAT
						| BOOL
						| STR
						| AUTO
						;
idlist: (ID COMMA) idlist | ID;
//Arithmetic operators
arthmetic_int_op: OP_MINUS
						| OP_ADD
						| OP_MUL
						| OP_MOD
						;
arthmetic_float_op: OP_MINUS
						| OP_ADD
						| OP_MUL
						;
bool_op: OP_NOT
			| OP_AND
			| OP_OR;
realational_int_op: OP_EQ_EQ
							| OP_INEQ
							| OP_LESS
							| OP_LESS_OR_EQ
							| OP_GREATER
							| OP_GREA_OR_EQ
							;
realational_float_op: OP_LESS
							| OP_LESS_OR_EQ
							| OP_GREATER
							| OP_GREA_OR_EQ
							;
realational_bool_op: OP_EQ_EQ
							| OP_INEQ
							;
			
index_op: ID '[' exprlist ']';
//function calls
func_call: ID LB argslist RB;
argslist: arg_prime | ;
arg_prime: arg COMMA arg_prime | arg;
arg: INTLIT | STRINGLIT | FLOATLIT | BOOLLIT | ID;

exprlist: exprprime | ;
exprprime: expr COMMA exprprime | expr;


expr: ;
//expression
str_expr: str_expr OP_STR_CONCAT str_expr | str_operands; //none - associative
str_operands: STRINGLIT | ID;

int_expr: int_expr realational_int_op int_expr | int_term1;
int_term1: ;

term_1:  term_2 OP_MINUS term_2 | term_2; //non - associative
term_2: term_2 (OP_MUL | OP_DIV) term_3 | term_3; //left - associative
term_3: subexpr | callexpr | INTLIT | FLOATLIT | STRINGLIT;
subexpr: LB expr RB;
callexpr: ID LB exprlist RB;

arraylit: '{' exprlist'}';

//array type
dimension_list: (dms COMMA) dimension_list | dms;
dms: INTLIT;

array_type: ARRAY '[' dimension_list ']' OF atomic_type;

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