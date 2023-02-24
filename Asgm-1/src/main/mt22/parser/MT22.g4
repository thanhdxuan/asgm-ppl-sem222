grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: decl EOF;

decl: vardecl | funcdecl;

vardecl: var_fullform;
// var_shortform: idlist COLON atomic_type;
//a: int = [1]
var_fullform: idlist ' '? COLON ' '? atomic_type ' '? '=' ' '? exprlist SEMI;


funcdecl: ;

idlist: (ID COMMA ' '?) idlist | ID;

// a,b,c: integer;
// a,b,c: integer = [1,2,3];
// a,b,c: integer = [1,3];

exprlist: exprprime | ;
exprprime: expr COMMA exprprime | expr;
expr: term_1 OP_ADD expr | term_1; //right - associative
term_1:  term_2 OP_MINUS term_2 | term_2; //non - associative
term_2: term_2 (OP_MUL | OP_DIV) term_3 | term_3; //left - associative
term_3: subexpr | callexpr | INTLIT | FLOATLIT | STRINGLIT;
subexpr: LB expr RB;
callexpr: ID LB exprlist RB;

arraylit: '{' exprlist'}';

//array type
dimension_list: (dms COMMA ' '?) dimension_list | dms;
dms: INTEGER;

array_type: ARRAY ' [' dimension_list ']' ' of ' atomic_type;
atomic_type: (BOOL | INT | FLOAT | STR);

//variables decle


BLOCK_COMMENT: '/*' .*? '*/' -> channel(HIDDEN);
LINE_COMMENT: '//' ~[\r\n]* -> channel(HIDDEN);

//keywords

AUTO: 'auto'; INT: 'integer';
VOID: 'void'; ARRAY: 'array'; BREAK: 'break';
FLOAT: 'float'; RETURN: 'return'; OUT: 'out'; BOOL: 'boolean';
FOR: 'for'; STR: 'string'; CONTINUE: 'continue';
DO: 'do'; FUNCT: 'function';
OF: 'of'; ELSE: 'else'; IF: 'if'; WHILE: 'while'; INHERIT: 'inherit';

//Operators
OP_SCOPE: '::';
OP_ADD: '+'; OP_MINUS: '-'; OP_MUL: '*'; OP_DIV: '/'; OP_MOD: '%'; OP_NOT: '!';
OP_AND: '&&'; OP_OR: '||'; OP_EQ: '=='; OP_INEQ: '!='; OP_LESS: '<'; OP_GREATER: '>';
OP_LESS_OR_EQ: '<='; OP_GREA_OR_EQ: '>=';

//Checkcommit
//Literals
BOOLLIT: 'true' | 'false';
FLOATLIT: (INTPART DECPART | INTPART DECPART? EXPPART) {self.text = self.text.replace("_", "")};
INTEGER: [1-9] [0-9]*;
INTLIT: INTPART {self.text = self.text.replace("_", "")};
fragment INTPART: '0' | [1-9] [0-9]* ('_'[0-9]+)* ;
fragment DECPART: '.' [0-9]+;
fragment EXPPART: [eE] [+-]? [0-9]+;
STRINGLIT: '"' ( '\\' [bfrnt'"\\] | ~[\n"])* '"' {self.text = self.text[1:-1]};



fragment STRPART: '"' ( '\\' [bfrnt'"\\] | ~[\n"])* '"';
//Separators
SEMI: ';'; COMMA: ','; LB: '('; RB: ')'; LP: '{'; RP: '}'; DOT: '.'; COLON: ':';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \b\t\r\n]+ -> skip; // skip spaces, tabs, newlines
ERROR_CHAR: . {raise ErrorToken(self.text)};
ILLEGAL_ESCAPE: '\\' (~[bfrnt'\\])* {raise IllegalEscape(self.text)};
UNCLOSE_STRING: '"' [.]* {raise UncloseString(self.text)};