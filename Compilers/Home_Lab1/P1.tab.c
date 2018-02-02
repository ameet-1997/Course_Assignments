/* A Bison parser, made by GNU Bison 3.0.4.  */

/* Bison implementation for Yacc-like parsers in C

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

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output.  */
#define YYBISON 1

/* Bison version.  */
#define YYBISON_VERSION "3.0.4"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Push parsers.  */
#define YYPUSH 0

/* Pull parsers.  */
#define YYPULL 1




/* Copy the first part of user declarations.  */
#line 1 "P1.y" /* yacc.c:339  */

	#include <stdio.h>
	#include <string.h>
	#include <stdlib.h>
	#include <limits.h>

	extern int yylex();
	extern int yyerror(char* s);

	typedef struct macro_table_{
		char *dec;
		char *sub;
		char **args;
		int num_of_args;
		int macro_type;
	}macro_table;

	int total_macros = 0;

	macro_table defined[5000];

	int get_num_of_args(char* args) 					// Functions to get the total number of arguments
	{	
		if(!args)
		{
			return 0;
		}

		int i=0;
		int counter = 0;
		while(args[i] != '\0')
		{
			if(args[i] == ',')
			{
				counter++;
			}
			i++;
		}
		return counter+1;
	}

	char** get_args(char* args, int total) 		// Function to get individual arguments from comma seperated arguments
	{	
		if(!args)
		{
			return NULL;
		}

		char** final_arguments = (char**) malloc(sizeof(char*)*total);

		int first = 0, second = 0;

		int i=0;
		for(i=0;i<total;++i)
		{
			if(second != 0)
			{
				first = second+1;
			}

			second = first;
			while((args[second] != ',')&&(args[second]!='\0'))
			{
				second++;
			}

			final_arguments[i] = (char*) malloc((second-first+1)*sizeof(char));
			int j=0;
			for(j=first;j<second;++j)
			{
				final_arguments[i][j-first] = args[j];
			}
			final_arguments[i][second-first] = '\0';
		}

		return final_arguments;
	}

	void add_to_table(char* dec, char* sub, char* args, int macro_type) 		// Function to add an entry to the macro table
	{
		int i=0;
		int flag = 0;

		// printf("In add to table\nThe strings are: %s :: %s", dec, sub);
		for(i=0;i<total_macros;++i)
		{
			if(strcmp(defined[i].dec, dec) == 0)
			{
				flag = 1;
				break;
			}
		}

		if(flag == 1) 	// If entry already exists
		{
			printf("// Failed to parse macrojava code.");
			exit(0);
		}
		else
		{
			defined[total_macros].dec = dec;
			defined[total_macros].sub = sub;
			defined[total_macros].num_of_args = get_num_of_args(args);
			defined[total_macros].args = get_args(args, defined[total_macros].num_of_args);
			defined[total_macros].macro_type = macro_type;

			// printf("Printing strings\n");
			// for(i=0;i<defined[total_macros].num_of_args;++i)
			// {
			// 	printf("%s\n", defined[total_macros].args[i]);
			// }
			// printf("%d arguments\n", defined[total_macros].num_of_args);
			total_macros++;
		}
	}

	char* replace_macro(char* dec, char *args, int macro_type)
	{	

		// printf("Inside replace function\n");
		int total = get_num_of_args(args);
		char** final_arguments = get_args(args, total);
		char* answer;
		// printf("Total number of arguments are %d -- %d\n", total, total_macros);
		// printf("The arguments are: %s\n", args);
		if(total == 0)
		{
			int i=0;
			int flag = 0;
			for(i=0;i<total_macros;++i)
			{
				if(((strcmp(dec, defined[i].dec) == 0)&&(!defined[i].args))&&(defined[i].macro_type == macro_type))
				{
					answer = (char*) malloc((strlen(defined[i].sub)+5)*sizeof(char));
					strcpy(answer, defined[i].sub);
					flag = 1;
					break;
				}
			}

			if(flag)
			{
				return answer;
			}
			else 				// If entry wasn't found in the table
			{
				printf("// Failed to parse macrojava code.");
				exit(0);
				return NULL;
			}
		}
		else
		{
			int zz = 0;
			int index = 0;
			int flag = 0;
			for(zz=0;zz<total_macros;++zz)
			{
				if(((strcmp(dec, defined[zz].dec) == 0)&&(total == defined[zz].num_of_args))&&(defined[zz].macro_type == macro_type))
				{
					index = zz;
					flag = 1;
					// printf("Matched %s\n",dec);
					// printf("Substituting with %s\n", defined[zz].sub);
					break;
				}
			}

			if(flag == 0) 		// If entry wasn't found in the table
			{
				printf("// Failed to parse macrojava code.");
				exit(0);
				return NULL;				
			}
			else
			{
				char* temp_answer = (char*) malloc(5000*sizeof(char));
				int total_memory = 0;
				int till = strlen(defined[index].sub);
				char* storage = (char*) malloc((till+10)*sizeof(char));
				int counter = 0;
				strcpy(temp_answer,"");
				strcpy(storage,"");
				char* string_array = defined[index].sub;
				int current = 1;
				// printf("Substituting with %s\n", defined[index].sub);

				// printf("The argument is: %s\n", final_arguments[0]);

				while(counter < till)
				{	
					current = 1;
					strcpy(storage, "");

					// if(storage[0] == '\0')
					// {
					// 	printf("Correct Initialization\n");
					// }
					while((counter < till)&&(((string_array[counter]>='a')&&(string_array[counter] <= 'z'))||((string_array[counter]>='A')&&(string_array[counter] <= 'Z'))||((string_array[counter]>='0')&&(string_array[counter] <= '9'))||string_array[counter] == '_'))
					{
						storage[current] = '\0';
						storage[current-1] = string_array[counter];
						current++;
						counter++;
					}

					if(storage[0] == '\0')
					{
						storage[1] = '\0';
						storage[0] = string_array[counter];
						counter++;
					}

					// printf("Value of storage after iteration: %s\n",storage);

					int i=0;
					int flag2 = 0;
					for(i=0;i<defined[index].num_of_args;++i)
					{
						if(strcmp(defined[index].args[i], storage) == 0)
						{
							strcat(temp_answer, final_arguments[i]);
							total_memory += (strlen(final_arguments[i])+1);
							flag2 = 1;
							break;
						}
					}

					if(flag2 == 0)
					{
						strcat(temp_answer, storage);
						total_memory += strlen(storage)+1;
					}

				}

				//------------------------------------------------------------------------------------------------------
				// Change it to answer = (char*) malloc((strlen(temp_answer)+20)*sizeof(char));
				answer = (char*) malloc((total_memory+100)*sizeof(char)); 		
				strcpy(answer, temp_answer);
				free(temp_answer);
				return answer;

			}
		}
	}


#line 315 "P1.tab.c" /* yacc.c:339  */

# ifndef YY_NULLPTR
#  if defined __cplusplus && 201103L <= __cplusplus
#   define YY_NULLPTR nullptr
#  else
#   define YY_NULLPTR 0
#  endif
# endif

/* Enabling verbose error messages.  */
#ifdef YYERROR_VERBOSE
# undef YYERROR_VERBOSE
# define YYERROR_VERBOSE 1
#else
# define YYERROR_VERBOSE 0
#endif

/* In a future release of Bison, this section will be replaced
   by #include "P1.tab.h".  */
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
#line 250 "P1.y" /* yacc.c:355  */

	char *str;	// Used for returning the string

#line 404 "P1.tab.c" /* yacc.c:355  */
};

typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_P1_TAB_H_INCLUDED  */

/* Copy the second part of user declarations.  */

#line 421 "P1.tab.c" /* yacc.c:358  */

#ifdef short
# undef short
#endif

#ifdef YYTYPE_UINT8
typedef YYTYPE_UINT8 yytype_uint8;
#else
typedef unsigned char yytype_uint8;
#endif

#ifdef YYTYPE_INT8
typedef YYTYPE_INT8 yytype_int8;
#else
typedef signed char yytype_int8;
#endif

#ifdef YYTYPE_UINT16
typedef YYTYPE_UINT16 yytype_uint16;
#else
typedef unsigned short int yytype_uint16;
#endif

#ifdef YYTYPE_INT16
typedef YYTYPE_INT16 yytype_int16;
#else
typedef short int yytype_int16;
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif ! defined YYSIZE_T
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned int
# endif
#endif

#define YYSIZE_MAXIMUM ((YYSIZE_T) -1)

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(Msgid) dgettext ("bison-runtime", Msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(Msgid) Msgid
# endif
#endif

#ifndef YY_ATTRIBUTE
# if (defined __GNUC__                                               \
      && (2 < __GNUC__ || (__GNUC__ == 2 && 96 <= __GNUC_MINOR__)))  \
     || defined __SUNPRO_C && 0x5110 <= __SUNPRO_C
#  define YY_ATTRIBUTE(Spec) __attribute__(Spec)
# else
#  define YY_ATTRIBUTE(Spec) /* empty */
# endif
#endif

#ifndef YY_ATTRIBUTE_PURE
# define YY_ATTRIBUTE_PURE   YY_ATTRIBUTE ((__pure__))
#endif

#ifndef YY_ATTRIBUTE_UNUSED
# define YY_ATTRIBUTE_UNUSED YY_ATTRIBUTE ((__unused__))
#endif

#if !defined _Noreturn \
     && (!defined __STDC_VERSION__ || __STDC_VERSION__ < 201112)
# if defined _MSC_VER && 1200 <= _MSC_VER
#  define _Noreturn __declspec (noreturn)
# else
#  define _Noreturn YY_ATTRIBUTE ((__noreturn__))
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YYUSE(E) ((void) (E))
#else
# define YYUSE(E) /* empty */
#endif

#if defined __GNUC__ && 407 <= __GNUC__ * 100 + __GNUC_MINOR__
/* Suppress an incorrect diagnostic about yylval being uninitialized.  */
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN \
    _Pragma ("GCC diagnostic push") \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")\
    _Pragma ("GCC diagnostic ignored \"-Wmaybe-uninitialized\"")
# define YY_IGNORE_MAYBE_UNINITIALIZED_END \
    _Pragma ("GCC diagnostic pop")
#else
# define YY_INITIAL_VALUE(Value) Value
#endif
#ifndef YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_END
#endif
#ifndef YY_INITIAL_VALUE
# define YY_INITIAL_VALUE(Value) /* Nothing. */
#endif


#if ! defined yyoverflow || YYERROR_VERBOSE

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined EXIT_SUCCESS
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
      /* Use EXIT_SUCCESS as a witness for stdlib.h.  */
#     ifndef EXIT_SUCCESS
#      define EXIT_SUCCESS 0
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's 'empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (0)
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined EXIT_SUCCESS \
       && ! ((defined YYMALLOC || defined malloc) \
             && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef EXIT_SUCCESS
#    define EXIT_SUCCESS 0
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined EXIT_SUCCESS
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined EXIT_SUCCESS
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* ! defined yyoverflow || YYERROR_VERBOSE */


#if (! defined yyoverflow \
     && (! defined __cplusplus \
         || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yytype_int16 yyss_alloc;
  YYSTYPE yyvs_alloc;
};

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (sizeof (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (sizeof (yytype_int16) + sizeof (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

# define YYCOPY_NEEDED 1

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack_alloc, Stack)                           \
    do                                                                  \
      {                                                                 \
        YYSIZE_T yynewbytes;                                            \
        YYCOPY (&yyptr->Stack_alloc, Stack, yysize);                    \
        Stack = &yyptr->Stack_alloc;                                    \
        yynewbytes = yystacksize * sizeof (*Stack) + YYSTACK_GAP_MAXIMUM; \
        yyptr += yynewbytes / sizeof (*yyptr);                          \
      }                                                                 \
    while (0)

#endif

#if defined YYCOPY_NEEDED && YYCOPY_NEEDED
/* Copy COUNT objects from SRC to DST.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(Dst, Src, Count) \
      __builtin_memcpy (Dst, Src, (Count) * sizeof (*(Src)))
#  else
#   define YYCOPY(Dst, Src, Count)              \
      do                                        \
        {                                       \
          YYSIZE_T yyi;                         \
          for (yyi = 0; yyi < (Count); yyi++)   \
            (Dst)[yyi] = (Src)[yyi];            \
        }                                       \
      while (0)
#  endif
# endif
#endif /* !YYCOPY_NEEDED */

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  4
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   228

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  45
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  24
/* YYNRULES -- Number of rules.  */
#define YYNRULES  70
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  195

/* YYTRANSLATE[YYX] -- Symbol number corresponding to YYX as returned
   by yylex, with out-of-bounds checking.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   299

#define YYTRANSLATE(YYX)                                                \
  ((unsigned int) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[TOKEN-NUM] -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex, without out-of-bounds checking.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44
};

#if YYDEBUG
  /* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_uint16 yyrline[] =
{
       0,   267,   267,   270,   275,   276,   279,   282,   286,   292,
     297,   304,   306,   313,   322,   326,   334,   339,   342,   347,
     350,   355,   358,   359,   360,   361,   364,   365,   366,   367,
     368,   369,   370,   371,   372,   375,   376,   379,   380,   381,
     382,   383,   384,   385,   386,   387,   388,   389,   390,   391,
     392,   393,   396,   397,   398,   399,   400,   401,   402,   403,
     404,   407,   408,   411,   417,   423,   429,   436,   437,   440,
     443
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || 0
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "SEMICOLON", "CLASS", "PUBLIC", "STATIC",
  "VOID", "MAIN", "STRING", "EXTENDS", "SYSTEM_PRINT", "RETURN", "INTEGER",
  "BOOLEAN", "IF", "ELSE", "WHILE", "LENGTH", "AND", "OR", "EQUALS", "NE",
  "LT", "GT", "NOT", "PLUS", "MINUS", "MUL", "DIV", "DOT", "COMMA", "TRUE",
  "FALSE", "THIS", "NEW", "DEFINE", "ID", "NUM", "L_PAREN", "R_PAREN",
  "L_CURLY", "R_CURLY", "L_SQUARE", "R_SQUARE", "$accept", "goal",
  "program", "macros", "types", "mainclass", "typedeclaration",
  "classtypes", "methods", "methoddeclaration", "method_arguments",
  "argument_list", "statement_list", "type", "statement",
  "expression_comma", "expression", "primaryexpression", "macrodefinition",
  "macrodefstatement", "macrodefexpression", "Identifier_comma",
  "Identifier", "number", YY_NULLPTR
};
#endif

# ifdef YYPRINT
/* YYTOKNUM[NUM] -- (External) token number corresponding to the
   (internal) symbol number NUM (which must be that of a token).  */
static const yytype_uint16 yytoknum[] =
{
       0,   256,   257,   258,   259,   260,   261,   262,   263,   264,
     265,   266,   267,   268,   269,   270,   271,   272,   273,   274,
     275,   276,   277,   278,   279,   280,   281,   282,   283,   284,
     285,   286,   287,   288,   289,   290,   291,   292,   293,   294,
     295,   296,   297,   298,   299
};
# endif

#define YYPACT_NINF -105

#define yypact_value_is_default(Yystate) \
  (!!((Yystate) == (-105)))

#define YYTABLE_NINF -1

#define yytable_value_is_error(Yytable_value) \
  0

  /* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
     STATE-NUM.  */
static const yytype_int16 yypact[] =
{
    -105,     3,  -105,     6,  -105,   -30,   -30,    18,  -105,  -105,
    -105,  -105,   -15,   -10,   -30,  -105,    18,    35,   -22,    15,
    -105,    45,   -25,    10,   -30,  -105,    47,   178,    42,   -30,
      23,    33,     7,    68,   178,  -105,  -105,  -105,    -9,  -105,
     178,    37,    97,    36,  -105,    50,    51,    56,    42,    63,
      42,    89,    10,    19,  -105,    48,    64,  -105,    70,   101,
     -30,  -105,    74,  -105,    66,    75,    78,  -105,  -105,   178,
     178,   178,   108,   178,   178,   178,   178,   -30,   178,   128,
     178,   178,   178,    94,  -105,  -105,   178,   146,   178,  -105,
     178,    42,     7,   -30,    87,  -105,  -105,   134,   129,   178,
      99,  -105,  -105,  -105,  -105,  -105,   178,  -105,  -105,  -105,
    -105,   102,   100,  -105,   112,   106,   109,   110,  -105,   145,
     148,   112,   113,   114,   116,   122,   135,  -105,  -105,   132,
     133,  -105,  -105,   167,  -105,   178,   136,   149,    42,    42,
    -105,  -105,   142,   166,  -105,  -105,  -105,    48,   144,  -105,
    -105,   112,   112,  -105,  -105,   173,  -105,   187,   178,   151,
     -30,   -30,   153,  -105,    42,  -105,   191,   154,   177,   157,
    -105,  -105,  -105,  -105,    48,  -105,   168,    67,   -30,   203,
     206,    89,   177,   180,   178,  -105,   178,   217,   181,   182,
     219,  -105,   183,   184,  -105
};

  /* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
     Performed when YYTABLE does not specify something else to do.  Zero
     means the default is an error.  */
static const yytype_uint8 yydefact[] =
{
       4,     0,     2,     0,     1,     0,     0,     7,     5,    62,
      61,    69,     0,     0,     0,     3,     7,     0,     0,     0,
       6,     0,     0,    68,     0,    11,     0,     0,    21,     0,
       0,     0,    14,     0,     0,    53,    54,    56,     0,    70,
       0,     0,    47,    55,    52,     0,     0,     0,    21,     0,
      21,     0,    68,     0,    11,     0,    24,    23,     0,    14,
       0,    25,     0,    59,     0,     0,     0,    66,    46,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    64,    20,     0,     0,     0,    67,
       0,    21,    14,     0,     0,     9,    13,     0,     0,     0,
       0,    60,    37,    55,    38,    39,     0,    41,    42,    43,
      44,     0,     0,    51,    36,     0,     0,     0,    26,     0,
       0,    36,     0,     0,     0,     0,     0,    22,    12,     0,
       0,    58,    40,     0,    45,     0,     0,     0,    21,    21,
      28,    34,     0,     0,    65,    63,    10,    17,     0,    57,
      49,    36,    36,    50,    27,    30,    32,     0,     0,     0,
       0,     0,     0,    35,    21,    33,     0,     0,    19,     0,
      48,    31,    29,    11,     0,    16,     0,    21,     0,     0,
       0,    25,    19,     0,     0,    18,     0,     0,     0,     0,
       0,    15,     0,     0,     8
};

  /* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -105,  -105,  -105,  -105,   207,  -105,  -105,   -52,   -54,  -105,
    -105,    46,   -42,   -44,  -105,  -104,    12,   -39,  -105,  -105,
    -105,   175,    -5,  -105
};

  /* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,     1,     2,     3,    15,     7,    16,    32,    58,    59,
     159,   175,    49,    60,    50,   136,    41,    42,     8,     9,
      10,    30,    43,    44
};

  /* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
     positive, shift that token.  If negative, reduce the rule whose
     number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_uint8 yytable[] =
{
      12,    13,    92,     4,    64,    96,    83,    11,    85,    19,
       5,    93,    55,    23,    27,    11,    28,   142,    22,    31,
      56,    57,    14,    51,    52,    24,    17,    61,    11,    18,
     102,   104,   105,    65,   107,   108,   109,   110,   125,   112,
      21,    29,     6,    51,    11,    51,    63,   162,   163,   124,
      61,    26,    66,    45,    33,    97,    25,    46,    90,    47,
      91,    56,    57,    53,   103,   103,   103,   132,   103,   103,
     103,   103,   111,   103,    54,    79,    62,    67,    45,    11,
      56,    57,    46,    48,    47,    11,    51,    61,   126,    80,
      81,   114,   115,   116,   117,    82,   155,   156,   119,   121,
     122,   103,   123,   160,    11,    84,    55,    94,    48,    99,
      86,   130,    95,    98,   100,    68,    69,    70,   101,    71,
      72,   177,   171,    73,    74,    75,    76,    77,    87,   106,
     178,   127,    88,    51,    51,   180,   118,   128,   129,   131,
      78,   133,    61,   135,   134,   151,   137,   152,   140,   138,
     139,   141,   154,    34,   144,   168,   169,   143,   145,    51,
      35,    36,    37,    38,   146,    11,    39,    40,   113,    61,
     166,    34,   181,   182,   147,   148,   153,   149,    35,    36,
      37,    38,   157,    11,    39,    40,   120,   158,   161,   164,
     165,   167,    34,   170,   172,   173,   187,   176,   188,    35,
      36,    37,    38,    34,    11,    39,    40,   150,   174,   179,
      35,    36,    37,    38,   183,    11,    39,    40,   184,   186,
     189,   190,   192,    20,   191,   193,   194,    89,   185
};

static const yytype_uint8 yycheck[] =
{
       5,     6,    54,     0,    13,    59,    48,    37,    50,    14,
       4,    55,     5,    18,    39,    37,    41,   121,    40,    24,
      13,    14,     4,    28,    29,    10,    41,    32,    37,    39,
      69,    70,    71,    38,    73,    74,    75,    76,    92,    78,
       5,    31,    36,    48,    37,    50,    34,   151,   152,    91,
      55,     6,    40,    11,     7,    60,    41,    15,    39,    17,
      41,    13,    14,    40,    69,    70,    71,   106,    73,    74,
      75,    76,    77,    78,    41,    39,     8,    40,    11,    37,
      13,    14,    15,    41,    17,    37,    91,    92,    93,    39,
      39,    79,    80,    81,    82,    39,   138,   139,    86,    87,
      88,   106,    90,   147,    37,    42,     5,    43,    41,    43,
      21,    99,    42,    39,    39,    18,    19,    20,    40,    22,
      23,   173,   164,    26,    27,    28,    29,    30,    39,    21,
     174,    44,    43,   138,   139,   177,    42,     3,     9,    40,
      43,    39,   147,    31,    44,   133,    40,   135,     3,    40,
      40,     3,     3,    25,    40,   160,   161,    44,    42,   164,
      32,    33,    34,    35,    42,    37,    38,    39,    40,   174,
     158,    25,   177,   178,    39,    43,    40,    44,    32,    33,
      34,    35,    40,    37,    38,    39,    40,    21,    44,    16,
       3,    40,    25,    40,     3,    41,   184,    40,   186,    32,
      33,    34,    35,    25,    37,    38,    39,    40,    31,    41,
      32,    33,    34,    35,    11,    37,    38,    39,    12,    39,
       3,    40,     3,    16,    42,    42,    42,    52,   182
};

  /* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
     symbol of state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,    46,    47,    48,     0,     4,    36,    50,    63,    64,
      65,    37,    67,    67,     4,    49,    51,    41,    39,    67,
      49,     5,    40,    67,    10,    41,     6,    39,    41,    31,
      66,    67,    52,     7,    25,    32,    33,    34,    35,    38,
      39,    61,    62,    67,    68,    11,    15,    17,    41,    57,
      59,    67,    67,    40,    41,     5,    13,    14,    53,    54,
      58,    67,     8,    61,    13,    67,    61,    40,    18,    19,
      20,    22,    23,    26,    27,    28,    29,    30,    43,    39,
      39,    39,    39,    57,    42,    57,    21,    39,    43,    66,
      39,    41,    52,    58,    43,    42,    53,    67,    39,    43,
      39,    40,    62,    67,    62,    62,    21,    62,    62,    62,
      62,    67,    62,    40,    61,    61,    61,    61,    42,    61,
      40,    61,    61,    61,    57,    53,    67,    44,     3,     9,
      61,    40,    62,    39,    44,    31,    60,    40,    40,    40,
       3,     3,    60,    44,    40,    42,    42,    39,    43,    44,
      40,    61,    61,    40,     3,    57,    57,    40,    21,    55,
      58,    44,    60,    60,    16,     3,    61,    40,    67,    67,
      40,    57,     3,    41,    31,    56,    40,    52,    58,    41,
      57,    67,    67,    11,    12,    56,    39,    61,    61,     3,
      40,    42,     3,    42,    42
};

  /* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint8 yyr1[] =
{
       0,    45,    46,    47,    48,    48,    49,    49,    50,    51,
      51,    52,    52,    53,    53,    54,    55,    55,    56,    56,
      57,    57,    58,    58,    58,    58,    59,    59,    59,    59,
      59,    59,    59,    59,    59,    60,    60,    61,    61,    61,
      61,    61,    61,    61,    61,    61,    61,    61,    61,    61,
      61,    61,    62,    62,    62,    62,    62,    62,    62,    62,
      62,    63,    63,    64,    64,    65,    65,    66,    66,    67,
      68
};

  /* YYR2[YYN] -- Number of symbols on the right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     1,     3,     0,     2,     2,     0,    21,     6,
       8,     0,     4,     2,     0,    13,     3,     0,     4,     0,
       2,     0,     3,     1,     1,     1,     3,     5,     4,     7,
       5,     7,     5,     6,     4,     3,     0,     3,     3,     3,
       4,     3,     3,     3,     3,     4,     2,     1,     7,     5,
       5,     3,     1,     1,     1,     1,     1,     5,     4,     2,
       3,     1,     1,     9,     7,     9,     7,     3,     0,     1,
       1
};


#define yyerrok         (yyerrstatus = 0)
#define yyclearin       (yychar = YYEMPTY)
#define YYEMPTY         (-2)
#define YYEOF           0

#define YYACCEPT        goto yyacceptlab
#define YYABORT         goto yyabortlab
#define YYERROR         goto yyerrorlab


#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)                                  \
do                                                              \
  if (yychar == YYEMPTY)                                        \
    {                                                           \
      yychar = (Token);                                         \
      yylval = (Value);                                         \
      YYPOPSTACK (yylen);                                       \
      yystate = *yyssp;                                         \
      goto yybackup;                                            \
    }                                                           \
  else                                                          \
    {                                                           \
      yyerror (YY_("syntax error: cannot back up")); \
      YYERROR;                                                  \
    }                                                           \
while (0)

/* Error token number */
#define YYTERROR        1
#define YYERRCODE       256



/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)                        \
do {                                            \
  if (yydebug)                                  \
    YYFPRINTF Args;                             \
} while (0)

/* This macro is provided for backward compatibility. */
#ifndef YY_LOCATION_PRINT
# define YY_LOCATION_PRINT(File, Loc) ((void) 0)
#endif


# define YY_SYMBOL_PRINT(Title, Type, Value, Location)                    \
do {                                                                      \
  if (yydebug)                                                            \
    {                                                                     \
      YYFPRINTF (stderr, "%s ", Title);                                   \
      yy_symbol_print (stderr,                                            \
                  Type, Value); \
      YYFPRINTF (stderr, "\n");                                           \
    }                                                                     \
} while (0)


/*----------------------------------------.
| Print this symbol's value on YYOUTPUT.  |
`----------------------------------------*/

static void
yy_symbol_value_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
{
  FILE *yyo = yyoutput;
  YYUSE (yyo);
  if (!yyvaluep)
    return;
# ifdef YYPRINT
  if (yytype < YYNTOKENS)
    YYPRINT (yyoutput, yytoknum[yytype], *yyvaluep);
# endif
  YYUSE (yytype);
}


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

static void
yy_symbol_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
{
  YYFPRINTF (yyoutput, "%s %s (",
             yytype < YYNTOKENS ? "token" : "nterm", yytname[yytype]);

  yy_symbol_value_print (yyoutput, yytype, yyvaluep);
  YYFPRINTF (yyoutput, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

static void
yy_stack_print (yytype_int16 *yybottom, yytype_int16 *yytop)
{
  YYFPRINTF (stderr, "Stack now");
  for (; yybottom <= yytop; yybottom++)
    {
      int yybot = *yybottom;
      YYFPRINTF (stderr, " %d", yybot);
    }
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)                            \
do {                                                            \
  if (yydebug)                                                  \
    yy_stack_print ((Bottom), (Top));                           \
} while (0)


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

static void
yy_reduce_print (yytype_int16 *yyssp, YYSTYPE *yyvsp, int yyrule)
{
  unsigned long int yylno = yyrline[yyrule];
  int yynrhs = yyr2[yyrule];
  int yyi;
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %lu):\n",
             yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      YYFPRINTF (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr,
                       yystos[yyssp[yyi + 1 - yynrhs]],
                       &(yyvsp[(yyi + 1) - (yynrhs)])
                                              );
      YYFPRINTF (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)          \
do {                                    \
  if (yydebug)                          \
    yy_reduce_print (yyssp, yyvsp, Rule); \
} while (0)

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args)
# define YY_SYMBOL_PRINT(Title, Type, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif


#if YYERROR_VERBOSE

# ifndef yystrlen
#  if defined __GLIBC__ && defined _STRING_H
#   define yystrlen strlen
#  else
/* Return the length of YYSTR.  */
static YYSIZE_T
yystrlen (const char *yystr)
{
  YYSIZE_T yylen;
  for (yylen = 0; yystr[yylen]; yylen++)
    continue;
  return yylen;
}
#  endif
# endif

# ifndef yystpcpy
#  if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#   define yystpcpy stpcpy
#  else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
static char *
yystpcpy (char *yydest, const char *yysrc)
{
  char *yyd = yydest;
  const char *yys = yysrc;

  while ((*yyd++ = *yys++) != '\0')
    continue;

  return yyd - 1;
}
#  endif
# endif

# ifndef yytnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for yyerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from yytname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYSIZE_T
yytnamerr (char *yyres, const char *yystr)
{
  if (*yystr == '"')
    {
      YYSIZE_T yyn = 0;
      char const *yyp = yystr;

      for (;;)
        switch (*++yyp)
          {
          case '\'':
          case ',':
            goto do_not_strip_quotes;

          case '\\':
            if (*++yyp != '\\')
              goto do_not_strip_quotes;
            /* Fall through.  */
          default:
            if (yyres)
              yyres[yyn] = *yyp;
            yyn++;
            break;

          case '"':
            if (yyres)
              yyres[yyn] = '\0';
            return yyn;
          }
    do_not_strip_quotes: ;
    }

  if (! yyres)
    return yystrlen (yystr);

  return yystpcpy (yyres, yystr) - yyres;
}
# endif

/* Copy into *YYMSG, which is of size *YYMSG_ALLOC, an error message
   about the unexpected token YYTOKEN for the state stack whose top is
   YYSSP.

   Return 0 if *YYMSG was successfully written.  Return 1 if *YYMSG is
   not large enough to hold the message.  In that case, also set
   *YYMSG_ALLOC to the required number of bytes.  Return 2 if the
   required number of bytes is too large to store.  */
static int
yysyntax_error (YYSIZE_T *yymsg_alloc, char **yymsg,
                yytype_int16 *yyssp, int yytoken)
{
  YYSIZE_T yysize0 = yytnamerr (YY_NULLPTR, yytname[yytoken]);
  YYSIZE_T yysize = yysize0;
  enum { YYERROR_VERBOSE_ARGS_MAXIMUM = 5 };
  /* Internationalized format string. */
  const char *yyformat = YY_NULLPTR;
  /* Arguments of yyformat. */
  char const *yyarg[YYERROR_VERBOSE_ARGS_MAXIMUM];
  /* Number of reported tokens (one for the "unexpected", one per
     "expected"). */
  int yycount = 0;

  /* There are many possibilities here to consider:
     - If this state is a consistent state with a default action, then
       the only way this function was invoked is if the default action
       is an error action.  In that case, don't check for expected
       tokens because there are none.
     - The only way there can be no lookahead present (in yychar) is if
       this state is a consistent state with a default action.  Thus,
       detecting the absence of a lookahead is sufficient to determine
       that there is no unexpected or expected token to report.  In that
       case, just report a simple "syntax error".
     - Don't assume there isn't a lookahead just because this state is a
       consistent state with a default action.  There might have been a
       previous inconsistent state, consistent state with a non-default
       action, or user semantic action that manipulated yychar.
     - Of course, the expected token list depends on states to have
       correct lookahead information, and it depends on the parser not
       to perform extra reductions after fetching a lookahead from the
       scanner and before detecting a syntax error.  Thus, state merging
       (from LALR or IELR) and default reductions corrupt the expected
       token list.  However, the list is correct for canonical LR with
       one exception: it will still contain any token that will not be
       accepted due to an error action in a later state.
  */
  if (yytoken != YYEMPTY)
    {
      int yyn = yypact[*yyssp];
      yyarg[yycount++] = yytname[yytoken];
      if (!yypact_value_is_default (yyn))
        {
          /* Start YYX at -YYN if negative to avoid negative indexes in
             YYCHECK.  In other words, skip the first -YYN actions for
             this state because they are default actions.  */
          int yyxbegin = yyn < 0 ? -yyn : 0;
          /* Stay within bounds of both yycheck and yytname.  */
          int yychecklim = YYLAST - yyn + 1;
          int yyxend = yychecklim < YYNTOKENS ? yychecklim : YYNTOKENS;
          int yyx;

          for (yyx = yyxbegin; yyx < yyxend; ++yyx)
            if (yycheck[yyx + yyn] == yyx && yyx != YYTERROR
                && !yytable_value_is_error (yytable[yyx + yyn]))
              {
                if (yycount == YYERROR_VERBOSE_ARGS_MAXIMUM)
                  {
                    yycount = 1;
                    yysize = yysize0;
                    break;
                  }
                yyarg[yycount++] = yytname[yyx];
                {
                  YYSIZE_T yysize1 = yysize + yytnamerr (YY_NULLPTR, yytname[yyx]);
                  if (! (yysize <= yysize1
                         && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
                    return 2;
                  yysize = yysize1;
                }
              }
        }
    }

  switch (yycount)
    {
# define YYCASE_(N, S)                      \
      case N:                               \
        yyformat = S;                       \
      break
      YYCASE_(0, YY_("syntax error"));
      YYCASE_(1, YY_("syntax error, unexpected %s"));
      YYCASE_(2, YY_("syntax error, unexpected %s, expecting %s"));
      YYCASE_(3, YY_("syntax error, unexpected %s, expecting %s or %s"));
      YYCASE_(4, YY_("syntax error, unexpected %s, expecting %s or %s or %s"));
      YYCASE_(5, YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s"));
# undef YYCASE_
    }

  {
    YYSIZE_T yysize1 = yysize + yystrlen (yyformat);
    if (! (yysize <= yysize1 && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
      return 2;
    yysize = yysize1;
  }

  if (*yymsg_alloc < yysize)
    {
      *yymsg_alloc = 2 * yysize;
      if (! (yysize <= *yymsg_alloc
             && *yymsg_alloc <= YYSTACK_ALLOC_MAXIMUM))
        *yymsg_alloc = YYSTACK_ALLOC_MAXIMUM;
      return 1;
    }

  /* Avoid sprintf, as that infringes on the user's name space.
     Don't have undefined behavior even if the translation
     produced a string with the wrong number of "%s"s.  */
  {
    char *yyp = *yymsg;
    int yyi = 0;
    while ((*yyp = *yyformat) != '\0')
      if (*yyp == '%' && yyformat[1] == 's' && yyi < yycount)
        {
          yyp += yytnamerr (yyp, yyarg[yyi++]);
          yyformat += 2;
        }
      else
        {
          yyp++;
          yyformat++;
        }
  }
  return 0;
}
#endif /* YYERROR_VERBOSE */

/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

static void
yydestruct (const char *yymsg, int yytype, YYSTYPE *yyvaluep)
{
  YYUSE (yyvaluep);
  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yytype, yyvaluep, yylocationp);

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YYUSE (yytype);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}




/* The lookahead symbol.  */
int yychar;

/* The semantic value of the lookahead symbol.  */
YYSTYPE yylval;
/* Number of syntax errors so far.  */
int yynerrs;


/*----------.
| yyparse.  |
`----------*/

int
yyparse (void)
{
    int yystate;
    /* Number of tokens to shift before error messages enabled.  */
    int yyerrstatus;

    /* The stacks and their tools:
       'yyss': related to states.
       'yyvs': related to semantic values.

       Refer to the stacks through separate pointers, to allow yyoverflow
       to reallocate them elsewhere.  */

    /* The state stack.  */
    yytype_int16 yyssa[YYINITDEPTH];
    yytype_int16 *yyss;
    yytype_int16 *yyssp;

    /* The semantic value stack.  */
    YYSTYPE yyvsa[YYINITDEPTH];
    YYSTYPE *yyvs;
    YYSTYPE *yyvsp;

    YYSIZE_T yystacksize;

  int yyn;
  int yyresult;
  /* Lookahead token as an internal (translated) token number.  */
  int yytoken = 0;
  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;

#if YYERROR_VERBOSE
  /* Buffer for error messages, and its allocated size.  */
  char yymsgbuf[128];
  char *yymsg = yymsgbuf;
  YYSIZE_T yymsg_alloc = sizeof yymsgbuf;
#endif

#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N))

  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  yyssp = yyss = yyssa;
  yyvsp = yyvs = yyvsa;
  yystacksize = YYINITDEPTH;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yystate = 0;
  yyerrstatus = 0;
  yynerrs = 0;
  yychar = YYEMPTY; /* Cause a token to be read.  */
  goto yysetstate;

/*------------------------------------------------------------.
| yynewstate -- Push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
 yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;

 yysetstate:
  *yyssp = yystate;

  if (yyss + yystacksize - 1 <= yyssp)
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYSIZE_T yysize = yyssp - yyss + 1;

#ifdef yyoverflow
      {
        /* Give user a chance to reallocate the stack.  Use copies of
           these so that the &'s don't force the real ones into
           memory.  */
        YYSTYPE *yyvs1 = yyvs;
        yytype_int16 *yyss1 = yyss;

        /* Each stack pointer address is followed by the size of the
           data in use in that stack, in bytes.  This used to be a
           conditional around just the two extra args, but that might
           be undefined if yyoverflow is a macro.  */
        yyoverflow (YY_("memory exhausted"),
                    &yyss1, yysize * sizeof (*yyssp),
                    &yyvs1, yysize * sizeof (*yyvsp),
                    &yystacksize);

        yyss = yyss1;
        yyvs = yyvs1;
      }
#else /* no yyoverflow */
# ifndef YYSTACK_RELOCATE
      goto yyexhaustedlab;
# else
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
        goto yyexhaustedlab;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
        yystacksize = YYMAXDEPTH;

      {
        yytype_int16 *yyss1 = yyss;
        union yyalloc *yyptr =
          (union yyalloc *) YYSTACK_ALLOC (YYSTACK_BYTES (yystacksize));
        if (! yyptr)
          goto yyexhaustedlab;
        YYSTACK_RELOCATE (yyss_alloc, yyss);
        YYSTACK_RELOCATE (yyvs_alloc, yyvs);
#  undef YYSTACK_RELOCATE
        if (yyss1 != yyssa)
          YYSTACK_FREE (yyss1);
      }
# endif
#endif /* no yyoverflow */

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;

      YYDPRINTF ((stderr, "Stack size increased to %lu\n",
                  (unsigned long int) yystacksize));

      if (yyss + yystacksize - 1 <= yyssp)
        YYABORT;
    }

  YYDPRINTF ((stderr, "Entering state %d\n", yystate));

  if (yystate == YYFINAL)
    YYACCEPT;

  goto yybackup;

/*-----------.
| yybackup.  |
`-----------*/
yybackup:

  /* Do appropriate processing given the current state.  Read a
     lookahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to lookahead token.  */
  yyn = yypact[yystate];
  if (yypact_value_is_default (yyn))
    goto yydefault;

  /* Not known => get a lookahead token if don't already have one.  */

  /* YYCHAR is either YYEMPTY or YYEOF or a valid lookahead symbol.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token: "));
      yychar = yylex ();
    }

  if (yychar <= YYEOF)
    {
      yychar = yytoken = YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yytable_value_is_error (yyn))
        goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the lookahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);

  /* Discard the shifted token.  */
  yychar = YYEMPTY;

  yystate = yyn;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END

  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- Do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     '$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];


  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
        case 2:
#line 267 "P1.y" /* yacc.c:1646  */
    {printf("%s",(yyvsp[0].str));}
#line 1630 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 3:
#line 270 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc((strlen((yyvsp[-1].str))+strlen((yyvsp[0].str))+10)*sizeof(char));
										 (yyval.str) = strcpy((yyval.str), (yyvsp[-1].str)); (yyval.str) = strcat((yyval.str), (yyvsp[0].str));
										 free((yyvsp[-1].str)); free((yyvsp[0].str));}
#line 1638 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 4:
#line 275 "P1.y" /* yacc.c:1646  */
    {;}
#line 1644 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 5:
#line 276 "P1.y" /* yacc.c:1646  */
    {;}
#line 1650 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 6:
#line 279 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc((strlen((yyvsp[-1].str))+strlen((yyvsp[0].str))+10)*sizeof(char));
								 strcpy((yyval.str), (yyvsp[-1].str)); strcat((yyval.str), (yyvsp[0].str));
								 free((yyvsp[-1].str)); free((yyvsp[0].str));}
#line 1658 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 7:
#line 282 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc(sizeof(char));
	   							 (yyval.str)[0] = '\0';}
#line 1665 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 8:
#line 286 "P1.y" /* yacc.c:1646  */
    {
	(yyval.str) = (char*) malloc((100 + strlen((yyvsp[-19].str))+ strlen((yyvsp[-9].str))+ strlen((yyvsp[-4].str)))*sizeof(char));
	strcpy((yyval.str),"class "); strcat((yyval.str), (yyvsp[-19].str)); strcat((yyval.str), "{\n public static void main(String[] "); strcat((yyval.str), (yyvsp[-9].str)); strcat((yyval.str), "){System.out.println( "); strcat((yyval.str), (yyvsp[-4].str)); strcat((yyval.str), ");\n}\n}");
	free((yyvsp[-19].str)); free((yyvsp[-9].str)); free((yyvsp[-4].str));  /*printf("Exiting Main Class without problems\n");*/}
#line 1674 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 9:
#line 292 "P1.y" /* yacc.c:1646  */
    {// Class declarations
					(yyval.str) = (char*) malloc((30+strlen((yyvsp[-4].str))+strlen((yyvsp[-2].str))+strlen((yyvsp[-1].str)))*sizeof(char));
					strcpy((yyval.str), "class "); strcat((yyval.str), (yyvsp[-4].str)); strcat((yyval.str), "{\n"); strcat((yyval.str), (yyvsp[-2].str)); strcat((yyval.str), "\n"); strcat((yyval.str), (yyvsp[-1].str)); strcat((yyval.str), "\n}");
					free((yyvsp[-4].str)); free((yyvsp[-2].str)); free((yyvsp[-1].str));
}
#line 1684 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 10:
#line 297 "P1.y" /* yacc.c:1646  */
    {
					(yyval.str) = (char*) malloc((30+strlen((yyvsp[-6].str))+strlen((yyvsp[-4].str))+strlen((yyvsp[-2].str))+strlen((yyvsp[-1].str)))*sizeof(char));
					strcpy((yyval.str), "class "); strcat((yyval.str), (yyvsp[-6].str)); strcat((yyval.str), " extends "); strcat((yyval.str), (yyvsp[-4].str)); strcat((yyval.str), "{\n"); strcat((yyval.str), (yyvsp[-2].str)); strcat((yyval.str), "\n"); strcat((yyval.str), (yyvsp[-1].str)); strcat((yyval.str), "\n}");
					free((yyvsp[-6].str)); free((yyvsp[-4].str)); free((yyvsp[-2].str)); free((yyvsp[-1].str));
}
#line 1694 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 11:
#line 304 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc(sizeof(char));	// Types declared in the class and methods
			 		(yyval.str)[0] = '\0';}
#line 1701 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 12:
#line 306 "P1.y" /* yacc.c:1646  */
    {
													(yyval.str) = (char*) malloc((strlen((yyvsp[-3].str))+strlen((yyvsp[-2].str))+strlen((yyvsp[-1].str))+10)*sizeof(char));
													strcpy((yyval.str), (yyvsp[-3].str)); strcat((yyval.str), (yyvsp[-2].str)); strcat((yyval.str), " "); strcat((yyval.str), (yyvsp[-1].str)); strcat((yyval.str),";");
													free((yyvsp[-3].str)); free((yyvsp[-2].str)); free((yyvsp[-1].str));
}
#line 1711 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 13:
#line 313 "P1.y" /* yacc.c:1646  */
    {	
										//printf("Content of first string--Part1: %s\n", $1);
										(yyval.str) = (char*) malloc((strlen((yyvsp[-1].str))+strlen((yyvsp[0].str))+10)*sizeof(char));
										//printf("Content of first string--Part2: %s\n", $1);
										strcpy((yyval.str), (yyvsp[-1].str)); strcat((yyval.str), (yyvsp[0].str));
										//printf("Inside methods block\n");
										// printf("Content of first:%s", $1);
										//free($2); //free($2);
}
#line 1725 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 14:
#line 322 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc(2*sizeof(char));
			 		strcpy((yyval.str),""); }
#line 1732 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 15:
#line 326 "P1.y" /* yacc.c:1646  */
    {
							(yyval.str) = (char*) malloc((strlen((yyvsp[-11].str))+strlen((yyvsp[-10].str))+strlen((yyvsp[-8].str))+strlen((yyvsp[-5].str))+strlen((yyvsp[-4].str))+strlen((yyvsp[-2].str))+50)*sizeof(char));
							strcpy((yyval.str), "public "); strcat((yyval.str), (yyvsp[-11].str)); strcat((yyval.str)," "); strcat((yyval.str), (yyvsp[-10].str)); strcat((yyval.str), "("); strcat((yyval.str), (yyvsp[-8].str)); strcat((yyval.str), "){\n"); strcat((yyval.str), (yyvsp[-5].str)); strcat((yyval.str), "\n"); strcat((yyval.str), (yyvsp[-4].str)); strcat((yyval.str), "\n"); strcat((yyval.str), "return "); strcat((yyval.str), (yyvsp[-2].str)); strcat((yyval.str), ";\n}\n");
							free((yyvsp[-11].str)); free((yyvsp[-10].str)); free((yyvsp[-8].str)); free((yyvsp[-5].str)); free((yyvsp[-4].str)); free((yyvsp[-2].str));
							//printf("Contents of the method are: %s\n", $$);
}
#line 1743 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 16:
#line 334 "P1.y" /* yacc.c:1646  */
    {// Arguments that the method takes
					(yyval.str) = (char*) malloc((strlen((yyvsp[-2].str))+strlen((yyvsp[-1].str))+strlen((yyvsp[0].str))+10)*sizeof(char));
					strcpy((yyval.str), (yyvsp[-2].str)); strcat((yyval.str)," "); strcat((yyval.str), (yyvsp[-1].str)); strcat((yyval.str), (yyvsp[0].str));
					free((yyvsp[-2].str)); free((yyvsp[-1].str)); free((yyvsp[0].str));
}
#line 1753 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 17:
#line 339 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc(sizeof(char));(yyval.str)[0] = '\0';}
#line 1759 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 18:
#line 342 "P1.y" /* yacc.c:1646  */
    {// If there are multiple comma seperated arguments
					(yyval.str) = (char*) malloc((strlen((yyvsp[-2].str))+strlen((yyvsp[-1].str))+strlen((yyvsp[0].str))+10)*sizeof(char));
					strcpy((yyval.str), ", "); strcat((yyval.str), (yyvsp[-2].str)); strcat((yyval.str)," "); strcat((yyval.str), (yyvsp[-1].str)); strcat((yyval.str), (yyvsp[0].str));
					free((yyvsp[-2].str)); free((yyvsp[-1].str)); free((yyvsp[0].str));
}
#line 1769 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 19:
#line 347 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc(sizeof(char));(yyval.str)[0] = '\0';}
#line 1775 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 20:
#line 350 "P1.y" /* yacc.c:1646  */
    {
					(yyval.str) = (char*) malloc((strlen((yyvsp[-1].str))+strlen((yyvsp[0].str))+10)*sizeof(char));
					strcpy((yyval.str), (yyvsp[-1].str));	strcat((yyval.str), (yyvsp[0].str));	
					free((yyvsp[-1].str)); free((yyvsp[0].str));
}
#line 1785 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 21:
#line 355 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc(sizeof(char));(yyval.str)[0] = '\0';}
#line 1791 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 22:
#line 358 "P1.y" /* yacc.c:1646  */
    {	(yyval.str) = (char*) malloc(sizeof(char)*10); strcpy((yyval.str), "int[] ");	}
#line 1797 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 23:
#line 359 "P1.y" /* yacc.c:1646  */
    {	(yyval.str) = (char*) malloc(sizeof(char)*10); strcpy((yyval.str), "boolean ");	}
#line 1803 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 24:
#line 360 "P1.y" /* yacc.c:1646  */
    {	(yyval.str) = (char*) malloc(sizeof(char)*10); strcpy((yyval.str), "int ");	}
#line 1809 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 25:
#line 361 "P1.y" /* yacc.c:1646  */
    {	(yyval.str) = (char*) malloc(sizeof(char)*(strlen((yyvsp[0].str))+10)); strcpy((yyval.str), (yyvsp[0].str)); free((yyvsp[0].str));	}
#line 1815 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 26:
#line 364 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char *) malloc((strlen((yyvsp[-1].str))+10)*sizeof(char)); strcpy((yyval.str),"{\n "); strcat((yyval.str),(yyvsp[-1].str)); strcat((yyval.str), " }\n"); free((yyvsp[-1].str)); }
#line 1821 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 27:
#line 365 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char *) malloc((strlen((yyvsp[-2].str))+35)*sizeof(char)); strcpy((yyval.str), "System.out.println("); strcat((yyval.str),(yyvsp[-2].str)); strcat((yyval.str),");\n"); free((yyvsp[-2].str)); }
#line 1827 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 28:
#line 366 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc((strlen((yyvsp[-3].str))+strlen((yyvsp[-1].str))+15)*sizeof(char)); strcpy((yyval.str), (yyvsp[-3].str)); strcat((yyval.str), " = "); strcat((yyval.str),(yyvsp[-1].str)); strcat((yyval.str), ";\n"); free((yyvsp[-3].str)); free((yyvsp[-1].str)); }
#line 1833 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 29:
#line 367 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc((strlen((yyvsp[-6].str))+strlen((yyvsp[-4].str))+strlen((yyvsp[-1].str))+15)*sizeof(char));  strcpy((yyval.str), (yyvsp[-6].str)); strcat((yyval.str),"["); strcat((yyval.str), (yyvsp[-4].str)); strcat((yyval.str),"] = "); strcat((yyval.str), (yyvsp[-1].str));  strcat((yyval.str), ";\n"); free((yyvsp[-6].str)); free((yyvsp[-4].str)); free((yyvsp[-1].str)); }
#line 1839 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 30:
#line 368 "P1.y" /* yacc.c:1646  */
    { (yyval.str) = (char*) malloc((strlen((yyvsp[-2].str))+strlen((yyvsp[0].str))+20)*sizeof(char)); strcpy((yyval.str), "if("); strcat((yyval.str), (yyvsp[-2].str)); strcat((yyval.str), ")"); strcat((yyval.str), (yyvsp[0].str)); free((yyvsp[-2].str)); free((yyvsp[0].str)); }
#line 1845 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 31:
#line 369 "P1.y" /* yacc.c:1646  */
    { (yyval.str) = (char*) malloc((strlen((yyvsp[-4].str))+strlen((yyvsp[-2].str))+strlen((yyvsp[0].str))+25)*sizeof(char)); strcpy((yyval.str), "if("); strcat((yyval.str), (yyvsp[-4].str)); strcat((yyval.str), ")"); strcat((yyval.str), (yyvsp[-2].str)); /*strcat($$, "\n");*/ strcat((yyval.str), "else "); strcat((yyval.str), (yyvsp[0].str)); free((yyvsp[-4].str)); free((yyvsp[-2].str)); free((yyvsp[0].str));}
#line 1851 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 32:
#line 370 "P1.y" /* yacc.c:1646  */
    { (yyval.str) = (char*) malloc((strlen((yyvsp[-2].str))+strlen((yyvsp[0].str))+20)*sizeof(char)); strcpy((yyval.str), "while("); strcat((yyval.str), (yyvsp[-2].str)); strcat((yyval.str), ")"); strcat((yyval.str), (yyvsp[0].str)); free((yyvsp[-2].str)); free((yyvsp[0].str));}
#line 1857 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 33:
#line 371 "P1.y" /* yacc.c:1646  */
    { /*printf("In statement macro\n");*/ char* temp = (char*) malloc((strlen((yyvsp[-3].str))+strlen((yyvsp[-2].str))+15)*sizeof(char)); strcpy(temp, (yyvsp[-3].str)); strcat(temp, (yyvsp[-2].str)); (yyval.str) = replace_macro((yyvsp[-5].str), temp, 1); /*strcat($$, ";\n");*/ free((yyvsp[-3].str)); free((yyvsp[-2].str)); free(temp);}
#line 1863 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 34:
#line 372 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = replace_macro((yyvsp[-3].str), NULL, 1);  strcat((yyval.str),";\n");}
#line 1869 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 35:
#line 375 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc((strlen((yyvsp[-1].str))+strlen((yyvsp[0].str))+10)); strcpy((yyval.str), ", "); strcat((yyval.str), (yyvsp[-1].str)); strcat((yyval.str), (yyvsp[0].str)); free((yyvsp[-1].str)); free((yyvsp[0].str));}
#line 1875 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 36:
#line 376 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc(sizeof(char)); (yyval.str)[0] = '\0';}
#line 1881 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 37:
#line 379 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc(strlen((yyvsp[-2].str))+strlen((yyvsp[0].str))+10); strcpy((yyval.str), (yyvsp[-2].str)); strcat((yyval.str), "&&"); strcat((yyval.str), (yyvsp[0].str)); free((yyvsp[-2].str)); free((yyvsp[0].str));}
#line 1887 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 38:
#line 380 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc(strlen((yyvsp[-2].str))+strlen((yyvsp[0].str))+10); strcpy((yyval.str), (yyvsp[-2].str)); strcat((yyval.str), "||"); strcat((yyval.str), (yyvsp[0].str)); free((yyvsp[-2].str)); free((yyvsp[0].str));}
#line 1893 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 39:
#line 381 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc(strlen((yyvsp[-2].str))+strlen((yyvsp[0].str))+10); strcpy((yyval.str), (yyvsp[-2].str)); strcat((yyval.str), "!="); strcat((yyval.str), (yyvsp[0].str)); free((yyvsp[-2].str)); free((yyvsp[0].str));}
#line 1899 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 40:
#line 382 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc(strlen((yyvsp[-3].str))+strlen((yyvsp[0].str))+10); strcpy((yyval.str), (yyvsp[-3].str)); strcat((yyval.str), "<="); strcat((yyval.str), (yyvsp[0].str)); free((yyvsp[-3].str)); free((yyvsp[0].str));}
#line 1905 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 41:
#line 383 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc(strlen((yyvsp[-2].str))+strlen((yyvsp[0].str))+10); strcpy((yyval.str), (yyvsp[-2].str)); strcat((yyval.str), "+"); strcat((yyval.str), (yyvsp[0].str)); free((yyvsp[-2].str)); free((yyvsp[0].str));}
#line 1911 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 42:
#line 384 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc(strlen((yyvsp[-2].str))+strlen((yyvsp[0].str))+10); strcpy((yyval.str), (yyvsp[-2].str)); strcat((yyval.str), "-"); strcat((yyval.str), (yyvsp[0].str)); free((yyvsp[-2].str)); free((yyvsp[0].str));}
#line 1917 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 43:
#line 385 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc(strlen((yyvsp[-2].str))+strlen((yyvsp[0].str))+10); strcpy((yyval.str), (yyvsp[-2].str)); strcat((yyval.str), "*"); strcat((yyval.str), (yyvsp[0].str)); free((yyvsp[-2].str)); free((yyvsp[0].str));}
#line 1923 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 44:
#line 386 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc(strlen((yyvsp[-2].str))+strlen((yyvsp[0].str))+10); strcpy((yyval.str), (yyvsp[-2].str)); strcat((yyval.str), "/"); strcat((yyval.str), (yyvsp[0].str)); free((yyvsp[-2].str)); free((yyvsp[0].str));}
#line 1929 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 45:
#line 387 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc(strlen((yyvsp[-3].str))+strlen((yyvsp[-1].str))+15); strcpy((yyval.str), (yyvsp[-3].str)); strcat((yyval.str), "["); strcat((yyval.str), (yyvsp[-1].str)); strcat((yyval.str), "]"); free((yyvsp[-3].str)); free((yyvsp[-1].str));}
#line 1935 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 46:
#line 388 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc((strlen((yyvsp[-1].str))+15)*(sizeof(char))); strcpy((yyval.str), (yyvsp[-1].str)); strcat((yyval.str), ".length"); free((yyvsp[-1].str));}
#line 1941 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 47:
#line 389 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc((strlen((yyvsp[0].str))+10)*(sizeof(char))); strcpy((yyval.str), (yyvsp[0].str)); free((yyvsp[0].str));}
#line 1947 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 48:
#line 390 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc((strlen((yyvsp[-6].str))+strlen((yyvsp[-4].str))+strlen((yyvsp[-2].str))+strlen((yyvsp[-1].str))+20)*sizeof(char)); strcpy((yyval.str), (yyvsp[-6].str)); strcat((yyval.str), "."); strcat((yyval.str), (yyvsp[-4].str)); strcat((yyval.str), "("); strcat((yyval.str), (yyvsp[-2].str)); strcat((yyval.str), (yyvsp[-1].str)); strcat((yyval.str),")"); free((yyvsp[-6].str)); free((yyvsp[-4].str));  free((yyvsp[-2].str));  free((yyvsp[-1].str));}
#line 1953 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 49:
#line 391 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc((strlen((yyvsp[-4].str))+strlen((yyvsp[-2].str))+20)*sizeof(char)); strcpy((yyval.str), (yyvsp[-4].str)); strcat((yyval.str), "."); strcat((yyval.str), (yyvsp[-2].str)); strcat((yyval.str), "()"); free((yyvsp[-4].str)); free((yyvsp[-2].str));}
#line 1959 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 50:
#line 392 "P1.y" /* yacc.c:1646  */
    { /*printf("In the right place\n");*/ char *temp = (char*) malloc((strlen((yyvsp[-2].str))+strlen((yyvsp[-1].str))+10)*sizeof(char)); /*strcpy(temp, "(");*/ strcpy(temp, (yyvsp[-2].str)); strcat(temp, (yyvsp[-1].str)); /*strcat(temp, ")");*/ (yyval.str) = replace_macro((yyvsp[-4].str), temp, 0); free((yyvsp[-2].str)); free((yyvsp[-1].str)); free(temp);}
#line 1965 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 51:
#line 393 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = replace_macro((yyvsp[-2].str), NULL, 0);}
#line 1971 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 52:
#line 396 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc((strlen((yyvsp[0].str))+10)*sizeof(char)); strcpy((yyval.str), (yyvsp[0].str)); free((yyvsp[0].str));}
#line 1977 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 53:
#line 397 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc(10*sizeof(char)); strcpy((yyval.str), "true ");}
#line 1983 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 54:
#line 398 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc(10*sizeof(char)); strcpy((yyval.str), "false ");}
#line 1989 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 55:
#line 399 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc((strlen((yyvsp[0].str))+10)*sizeof(char)); strcpy((yyval.str), (yyvsp[0].str)); free((yyvsp[0].str));}
#line 1995 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 56:
#line 400 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc(10*sizeof(char)); strcpy((yyval.str), "this");}
#line 2001 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 57:
#line 401 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc((strlen((yyvsp[-1].str))+20)*sizeof(char)); strcpy((yyval.str), "new int["); strcat((yyval.str), (yyvsp[-1].str)); strcat((yyval.str), "]"); free((yyvsp[-1].str));}
#line 2007 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 58:
#line 402 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc((strlen((yyvsp[-2].str))+15)*sizeof(char)); strcpy((yyval.str), "new "); strcat((yyval.str), (yyvsp[-2].str)); strcat((yyval.str), "()"); free((yyvsp[-2].str));}
#line 2013 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 59:
#line 403 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc((strlen((yyvsp[0].str))+5)*sizeof(char)); (yyval.str) = strcpy((yyval.str), "!"); strcat((yyval.str), (yyvsp[0].str)); free((yyvsp[0].str));}
#line 2019 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 60:
#line 404 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc((strlen((yyvsp[-1].str))+10)*sizeof(char)); strcpy((yyval.str),"("); strcat((yyval.str), (yyvsp[-1].str)); strcat((yyval.str), ")"); free((yyvsp[-1].str));}
#line 2025 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 63:
#line 411 "P1.y" /* yacc.c:1646  */
    {
						char *temp = (char*) malloc((strlen((yyvsp[-5].str))+strlen((yyvsp[-4].str))+10)*sizeof(char)); strcpy(temp, (yyvsp[-5].str)); strcat(temp, (yyvsp[-4].str));
						char *stat =  (char*) malloc((strlen((yyvsp[-1].str))+10)*sizeof(char)); strcpy(stat, "{"); strcat(stat, (yyvsp[-1].str)); strcat(stat,"}");
						char *dec = (char*) malloc(strlen((yyvsp[-7].str))+10); strcpy(dec, (yyvsp[-7].str));
						free((yyvsp[-5].str)); free((yyvsp[-4].str)); free((yyvsp[-1].str)); add_to_table(dec, stat, temp, 1); free((yyvsp[-7].str));
}
#line 2036 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 64:
#line 417 "P1.y" /* yacc.c:1646  */
    {
						char *temp = (char*) malloc((strlen((yyvsp[-1].str))+10)*sizeof(char)); strcpy(temp,"{"); strcat(temp,(yyvsp[-1].str)); strcat(temp, "}"); free((yyvsp[-1].str)); 
						char *dec = (char*) malloc(strlen((yyvsp[-5].str))+10); strcpy(dec, (yyvsp[-5].str)); add_to_table(dec, temp, NULL, 1); free((yyvsp[-5].str));
}
#line 2045 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 65:
#line 423 "P1.y" /* yacc.c:1646  */
    {
						char *temp = (char*) malloc((strlen((yyvsp[-5].str))+strlen((yyvsp[-4].str))+10)*sizeof(char)); strcpy(temp, (yyvsp[-5].str)); strcat(temp, (yyvsp[-4].str));
						char *stat =  (char*) malloc((strlen((yyvsp[-1].str))+10)*sizeof(char)); strcpy(stat, "("); strcat(stat, (yyvsp[-1].str)); strcat(stat,")");
						char *dec = (char*) malloc(strlen((yyvsp[-7].str))+10); strcpy(dec, (yyvsp[-7].str));
						free((yyvsp[-5].str)); free((yyvsp[-4].str)); free((yyvsp[-1].str)); add_to_table(dec, stat, temp, 0); free((yyvsp[-7].str)); //printf("part-1\n");
}
#line 2056 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 66:
#line 429 "P1.y" /* yacc.c:1646  */
    {
						char *temp = (char*) malloc((strlen((yyvsp[-1].str))+10)*sizeof(char)); strcpy(temp,"("); strcat(temp,(yyvsp[-1].str)); strcat(temp, ")"); free((yyvsp[-1].str)); 
						char *dec = (char*) malloc(strlen((yyvsp[-5].str))+10); strcpy(dec, (yyvsp[-5].str));
						add_to_table(dec, temp, NULL, 0);	free((yyvsp[-5].str));
}
#line 2066 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 67:
#line 436 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc((strlen((yyvsp[-1].str))+strlen((yyvsp[0].str))+5)*sizeof(char)); strcpy((yyval.str), ","); strcat((yyval.str), (yyvsp[-1].str)); strcat((yyval.str),(yyvsp[0].str)); free((yyvsp[-1].str)); free((yyvsp[0].str));}
#line 2072 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 68:
#line 437 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc(2*sizeof(char)); (yyval.str)[0] = '\0';}
#line 2078 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 69:
#line 440 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc((strlen((yyvsp[0].str))+5)*sizeof(char)); strcpy((yyval.str), (yyvsp[0].str));}
#line 2084 "P1.tab.c" /* yacc.c:1646  */
    break;

  case 70:
#line 443 "P1.y" /* yacc.c:1646  */
    {(yyval.str) = (char*) malloc((strlen((yyvsp[0].str))+5)*sizeof(char)); strcpy((yyval.str), (yyvsp[0].str)); strcat((yyval.str), " ");}
#line 2090 "P1.tab.c" /* yacc.c:1646  */
    break;


#line 2094 "P1.tab.c" /* yacc.c:1646  */
      default: break;
    }
  /* User semantic actions sometimes alter yychar, and that requires
     that yytoken be updated with the new translation.  We take the
     approach of translating immediately before every use of yytoken.
     One alternative is translating here after every semantic action,
     but that translation would be missed if the semantic action invokes
     YYABORT, YYACCEPT, or YYERROR immediately after altering yychar or
     if it invokes YYBACKUP.  In the case of YYABORT or YYACCEPT, an
     incorrect destructor might then be invoked immediately.  In the
     case of YYERROR or YYBACKUP, subsequent parser actions might lead
     to an incorrect destructor call or verbose syntax error message
     before the lookahead is translated.  */
  YY_SYMBOL_PRINT ("-> $$ =", yyr1[yyn], &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);

  *++yyvsp = yyval;

  /* Now 'shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */

  yyn = yyr1[yyn];

  yystate = yypgoto[yyn - YYNTOKENS] + *yyssp;
  if (0 <= yystate && yystate <= YYLAST && yycheck[yystate] == *yyssp)
    yystate = yytable[yystate];
  else
    yystate = yydefgoto[yyn - YYNTOKENS];

  goto yynewstate;


/*--------------------------------------.
| yyerrlab -- here on detecting error.  |
`--------------------------------------*/
yyerrlab:
  /* Make sure we have latest lookahead translation.  See comments at
     user semantic actions for why this is necessary.  */
  yytoken = yychar == YYEMPTY ? YYEMPTY : YYTRANSLATE (yychar);

  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
#if ! YYERROR_VERBOSE
      yyerror (YY_("syntax error"));
#else
# define YYSYNTAX_ERROR yysyntax_error (&yymsg_alloc, &yymsg, \
                                        yyssp, yytoken)
      {
        char const *yymsgp = YY_("syntax error");
        int yysyntax_error_status;
        yysyntax_error_status = YYSYNTAX_ERROR;
        if (yysyntax_error_status == 0)
          yymsgp = yymsg;
        else if (yysyntax_error_status == 1)
          {
            if (yymsg != yymsgbuf)
              YYSTACK_FREE (yymsg);
            yymsg = (char *) YYSTACK_ALLOC (yymsg_alloc);
            if (!yymsg)
              {
                yymsg = yymsgbuf;
                yymsg_alloc = sizeof yymsgbuf;
                yysyntax_error_status = 2;
              }
            else
              {
                yysyntax_error_status = YYSYNTAX_ERROR;
                yymsgp = yymsg;
              }
          }
        yyerror (yymsgp);
        if (yysyntax_error_status == 2)
          goto yyexhaustedlab;
      }
# undef YYSYNTAX_ERROR
#endif
    }



  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse lookahead token after an
         error, discard it.  */

      if (yychar <= YYEOF)
        {
          /* Return failure if at end of input.  */
          if (yychar == YYEOF)
            YYABORT;
        }
      else
        {
          yydestruct ("Error: discarding",
                      yytoken, &yylval);
          yychar = YYEMPTY;
        }
    }

  /* Else will try to reuse lookahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:

  /* Pacify compilers like GCC when the user code never invokes
     YYERROR and the label yyerrorlab therefore never appears in user
     code.  */
  if (/*CONSTCOND*/ 0)
     goto yyerrorlab;

  /* Do not reclaim the symbols of the rule whose action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;      /* Each real token shifted decrements this.  */

  for (;;)
    {
      yyn = yypact[yystate];
      if (!yypact_value_is_default (yyn))
        {
          yyn += YYTERROR;
          if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYTERROR)
            {
              yyn = yytable[yyn];
              if (0 < yyn)
                break;
            }
        }

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
        YYABORT;


      yydestruct ("Error: popping",
                  yystos[yystate], yyvsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", yystos[yyn], yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturn;

/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturn;

#if !defined yyoverflow || YYERROR_VERBOSE
/*-------------------------------------------------.
| yyexhaustedlab -- memory exhaustion comes here.  |
`-------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  /* Fall through.  */
#endif

yyreturn:
  if (yychar != YYEMPTY)
    {
      /* Make sure we have latest lookahead translation.  See comments at
         user semantic actions for why this is necessary.  */
      yytoken = YYTRANSLATE (yychar);
      yydestruct ("Cleanup: discarding lookahead",
                  yytoken, &yylval);
    }
  /* Do not reclaim the symbols of the rule whose action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
                  yystos[*yyssp], yyvsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif
#if YYERROR_VERBOSE
  if (yymsg != yymsgbuf)
    YYSTACK_FREE (yymsg);
#endif
  return yyresult;
}
#line 447 "P1.y" /* yacc.c:1906  */

int yywrap() {return 1;}
int yyerror(char* s) {fprintf(stderr,"// Failed to parse macrojava code.");}
int main()
{
	yyparse();
	exit(0);
	return 0;
}
