%{
	#include <stdio.h>
	#include <string.h>
	#include "P1.tab.h"

	void yyerror(char *);
	int yyparse();
%}

%%
\/\/.* 					{/*printf("%s\n", yytext);*/}			// Single line comments  This has to be on the top, as \n and space will get matched otherwise
\/\*(.*\n*)*\*\/ 		{/*printf("%s", yytext);*/}			// Multi-Line comments
[ \t\n]					{;}						// \r represents carriage return, \f represents formfeed
\;						{return SEMICOLON;}
"class"					{return CLASS;}
"public"				{return PUBLIC;}
"static"				{return STATIC;}
"void"					{return VOID;}
"main" 					{return MAIN;}
"String"				{return STRING;}
"System.out.println"	{return SYSTEM_PRINT;}
"extends"				{return EXTENDS;}
"return"				{return RETURN;}
"int"					{return INTEGER;}
"boolean"				{return BOOLEAN;}
"if"					{return IF;}
"else"					{return ELSE;}
"while"					{return WHILE;}
".length"				{return LENGTH;}		// Check if there can be conflict with "."
"&&"					{return AND;}
"||"					{return OR;}
\=						{return EQUALS;}
"!="					{return NE;}
\<						{return LT;}
\>						{return GT;}
\!						{return NOT;}
\+						{return PLUS;}
\-						{return MINUS;}
\*						{return MUL;}
\/						{return DIV;}
\.						{return DOT;}
\,						{return COMMA;}
"true"					{return TRUE;}
"false"					{return FALSE;}
"this"					{return THIS;}
"new"					{return NEW;}
"#define"				{return DEFINE;}
[A-Za-z][A-Za-z0-9_]* 	{yylval.str = strdup(yytext); return ID;} 	// printf("ID:\n"); printf("%s\n", yytext); 
[0-9]+					{yylval.str = strdup(yytext); return NUM;}
"("						{return L_PAREN;}
")"						{return R_PAREN;}
"{"						{return L_CURLY;}
"}"						{return R_CURLY;}
"["						{return L_SQUARE;}
"]"						{return R_SQUARE;}
%% 
