grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: EOF;

//keywords
KW_AUTO: 'auto'; KW_FALSE: 'false'; KW_INT: 'integer';
KW_VOID: 'void'; KW_ARRAY: 'array'; KW_BREAK: 'break';
KW_FLOAT: 'float'; KW_RETURN: 'return'; KW_OUT: 'out'; KW_BOOL: 'boolean';
KW_FOR: 'for'; KW_STR: 'string'; KW_CONTINUE: 'continue';
KW_DO: 'do'; KW_FUNCT: 'function'; KW_TRUE: 'true';
KW_OF: 'of'; KW_ELSE: 'else'; KW_IF: 'if'; KW_WHILE: 'while'; KW_INHERIT: 'inherit';

//Operators
OP_SCOPE: '::';
OP_ADD: '+'; OP_MINUS: '-'; OP_MUL: '*'; OP_DIV: '/'; OP_MOD: '%'; OP_NOT: '!';
OP_AND: '&&'; OP_OR: '||'; OP_EQ: '=='; OP_INEQ: '!='; OP_LESS: '<'; OP_GREATER: '>';
OP_LESS_OR_EQ: '<='; OP_GREA_OR_EQ: '>=';

//Separators
SEMI: ';'; COMMA: ','; LB: '('; RB: ')'; LP: '{'; RP: '}'; DOT: '.';
//Checkcommit
//Literals
FLOATLIT: INTPART DECPART;
// INTLIT: INTPART {self.text = self.text.replace("_", "")}; 
fragment INTPART: '0' | [1-9] [0-9]* ('_'[0-9]+)* {self.text = self.text.replace("_", "")};
fragment DECPART: [0-9]+;
fragment EXPPART: [eE] [+-]? [0-9]+;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \b\t\r\n]+ -> skip; // skip spaces, tabs, newlines
ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;