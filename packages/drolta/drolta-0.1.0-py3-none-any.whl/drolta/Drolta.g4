grammar Drolta;

// Parser Rules

prog: (prog_statement S_COL)* EOF;

prog_statement: alias_declaration | rule_declaration | query;

alias_declaration:
	ALIAS original = IDENTIFIER AS alias = IDENTIFIER;

rule_declaration: define_clause where_clause;

define_clause:
	DEFINE IDENTIFIER OPEN_PAR (VARIABLE (COMMA VARIABLE)*)? CLOSE_PAR;

query: find_clause where_clause post_processing_statements*;

find_clause: FIND (VARIABLE (COMMA VARIABLE)*)?;

where_clause: WHERE (where_statement (where_statement)*)?;

post_processing_statements:
	order_by_statement
	| group_by_statement
	| limit_statement;

order_by_statement: ORDER BY VARIABLE;

group_by_statement: GROUP BY VARIABLE;

limit_statement: LIMIT INT_LITERAL;

where_statement: filter_statement | predicate_statement;

filter_statement:
	OPEN_PAR left = VARIABLE op = comparison_operator right = atom CLOSE_PAR	# ComparisonFilter
	| OPEN_PAR left = VARIABLE IN atom_list										# InFilter
	| OPEN_PAR left = filter_statement AND right = filter_statement CLOSE_PAR	# AndFilter
	| OPEN_PAR left = filter_statement OR right = filter_statement CLOSE_PAR	# OrFilter
	| OPEN_PAR NOT filter_statement CLOSE_PAR									# NotFilter;

atom_list: BRACKET_L (atom (COMMA atom)*)? BRACKET_R;

comparison_operator: GT | GTE | LT | LTE | EQ | NEQ;

predicate_statement:
	PredicateName = IDENTIFIER OPEN_PAR (
		predicate_param (COMMA predicate_param)*
	)? CLOSE_PAR				# Predicate
	| NOT predicate_statement	# PredicateNot;

predicate_param: IDENTIFIER EQ atom;

atom:
	VARIABLE
	| INT_LITERAL
	| FLOAT_LITERAL
	| STRING_LITERAL
	| BOOLEAN_LITERAL
	| NULL				;

// LEXER RULES

S_COL: ';';
DOT: '.';
OPEN_PAR: '(';
CLOSE_PAR: ')';
BRACKET_L: '[';
BRACKET_R: ']';
DBL_COL: '::';
COMMA: ',';
FIND: 'FIND';
WHERE: 'WHERE';
OR: 'OR';
AND: 'AND';
NOT: 'NOT';
LIMIT: 'LIMIT';
BY: 'BY';
IN: 'IN';
ORDER: 'ORDER';
GROUP: 'GROUP';
USING: 'USING';
DEFINE: 'DEFINE';
ALIAS: 'ALIAS';
AS: 'AS';
EQ: '=';
NEQ: '!=';
LTE: '<=';
LT: '<';
GTE: '>=';
GT: '>';

VARIABLE: '?' [a-zA-Z_\u007F-\uFFFF] [a-zA-Z_0-9\u007F-\uFFFF]*;

IDENTIFIER: [a-zA-Z_\u007F-\uFFFF] [a-zA-Z_0-9\u007F-\uFFFF]*;

BOOLEAN_LITERAL: 'TRUE' | 'FALSE';

NULL: 'NULL';

INT_LITERAL: [-+]? [1-9][0-9]*;

FLOAT_LITERAL: [-+]? [0-9]* '.' [0-9]* [1-9];

STRING_LITERAL: '"' ( '\\"' | ~('"'))* '"';

SINGLE_LINE_COMMENT:
	'--' ~[\r\n]* (('\r'? '\n') | EOF) -> channel(HIDDEN);

MULTILINE_COMMENT: '/*' .*? '*/' -> channel(HIDDEN);

WHITESPACE: [ \u000B\t\r\n] -> channel(HIDDEN);

fragment HEX_DIGIT: [0-9A-F];
fragment DIGIT: [0-9];
