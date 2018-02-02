/* A Bison parser, made by GNU Bison 3.0.4.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

#ifndef YY_YY_P1_TAB_H_INCLUDED
# define YY_YY_P1_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    SEMICOLON = 258,
    CLASS = 259,
    PUBLIC = 260,
    STATIC = 261,
    VOID = 262,
    MAIN = 263,
    STRING = 264,
    EXTENDS = 265,
    SYSTEM_PRINT = 266,
    RETURN = 267,
    INTEGER = 268,
    BOOLEAN = 269,
    IF = 270,
    ELSE = 271,
    WHILE = 272,
    LENGTH = 273,
    AND = 274,
    OR = 275,
    EQUALS = 276,
    NE = 277,
    LT = 278,
    GT = 279,
    NOT = 280,
    PLUS = 281,
    MINUS = 282,
    MUL = 283,
    DIV = 284,
    DOT = 285,
    COMMA = 286,
    TRUE = 287,
    FALSE = 288,
    THIS = 289,
    NEW = 290,
    DEFINE = 291,
    ID = 292,
    NUM = 293,
    L_PAREN = 294,
    R_PAREN = 295,
    L_CURLY = 296,
    R_CURLY = 297,
    L_SQUARE = 298,
    R_SQUARE = 299
  };
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED

union YYSTYPE
{
#line 250 "P1.y" /* yacc.c:1909  */

	char *str;	// Used for returning the string

#line 103 "P1.tab.h" /* yacc.c:1909  */
};

typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_P1_TAB_H_INCLUDED  */
