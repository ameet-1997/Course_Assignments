%{
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

%}

%union{
	char *str;	// Used for returning the string
}

%token<str> SEMICOLON CLASS PUBLIC STATIC VOID MAIN STRING EXTENDS SYSTEM_PRINT RETURN INTEGER BOOLEAN IF ELSE WHILE LENGTH AND 
%token<str> OR EQUALS NE LT GT NOT PLUS MINUS MUL DIV DOT COMMA TRUE FALSE THIS NEW DEFINE ID NUM L_PAREN R_PAREN L_CURLY R_CURLY 
%token<str> L_SQUARE R_SQUARE

%type <str> goal program macros mainclass types macrodefinition typedeclaration classtypes methods methoddeclaration
%type <str> method_arguments argument_list statement_list type statement expression_comma expression primaryexpression 
%type <str> macrodefstatement macrodefexpression Identifier_comma Identifier number

// No macors, macrodeclaration and macrodefinition

%start goal

%%
goal: program							{printf("%s",$1);} 		// Print the whole program
;

program: macros mainclass types 		{$$ = (char*) malloc((strlen($2)+strlen($3)+10)*sizeof(char));
										 $$ = strcpy($$, $2); $$ = strcat($$, $3);
										 free($2); free($3);}	// Concatenate the two strings
;

macros: 					{;}  			// Make grammar left recursive to remove shift reduce conflict
		| 	macros macrodefinition 	{;}	// (macrodefinition)* 	epsilon production
;

types: typedeclaration types 	{$$ = (char*) malloc((strlen($1)+strlen($2)+10)*sizeof(char));
								 strcpy($$, $1); strcat($$, $2);
								 free($1); free($2);}	// (typedelaration)*
	   | 						{$$ = (char*) malloc(sizeof(char));
	   							 $$[0] = '\0';} 		// return the null string	
; 			

mainclass: CLASS Identifier L_CURLY PUBLIC STATIC VOID MAIN L_PAREN STRING L_SQUARE R_SQUARE Identifier R_PAREN L_CURLY SYSTEM_PRINT L_PAREN expression R_PAREN SEMICOLON R_CURLY R_CURLY	{
	$$ = (char*) malloc((100 + strlen($2)+ strlen($12)+ strlen($17))*sizeof(char));
	strcpy($$,"class "); strcat($$, $2); strcat($$, "{\n public static void main(String[] "); strcat($$, $12); strcat($$, "){System.out.println( "); strcat($$, $17); strcat($$, ");\n}\n}");
	free($2); free($12); free($17);  /*printf("Exiting Main Class without problems\n");*/}
;

typedeclaration: CLASS Identifier L_CURLY classtypes methods R_CURLY	{// Class declarations
					$$ = (char*) malloc((30+strlen($2)+strlen($4)+strlen($5))*sizeof(char));
					strcpy($$, "class "); strcat($$, $2); strcat($$, "{\n"); strcat($$, $4); strcat($$, "\n"); strcat($$, $5); strcat($$, "\n}");
					free($2); free($4); free($5);
}
				| CLASS Identifier EXTENDS Identifier L_CURLY classtypes methods R_CURLY 	{
					$$ = (char*) malloc((30+strlen($2)+strlen($4)+strlen($6)+strlen($7))*sizeof(char));
					strcpy($$, "class "); strcat($$, $2); strcat($$, " extends "); strcat($$, $4); strcat($$, "{\n"); strcat($$, $6); strcat($$, "\n"); strcat($$, $7); strcat($$, "\n}");
					free($2); free($4); free($6); free($7);
}
;

classtypes: 	{$$ = (char*) malloc(sizeof(char));	// Types declared in the class and methods
			 		$$[0] = '\0';} 			// Methods inside the class	
		|   classtypes type Identifier SEMICOLON {
													$$ = (char*) malloc((strlen($1)+strlen($2)+strlen($3)+10)*sizeof(char));
													strcpy($$, $1); strcat($$, $2); strcat($$, " "); strcat($$, $3); strcat($$,";");
													free($1); free($2); free($3);
}
;

methods: methoddeclaration methods {	
										//printf("Content of first string--Part1: %s\n", $1);
										$$ = (char*) malloc((strlen($1)+strlen($2)+10)*sizeof(char));
										//printf("Content of first string--Part2: %s\n", $1);
										strcpy($$, $1); strcat($$, $2);
										//printf("Inside methods block\n");
										// printf("Content of first:%s", $1);
										//free($2); //free($2);
}
 	| 				{$$ = (char*) malloc(2*sizeof(char));
			 		strcpy($$,""); } 			// Methods inside the class
;

methoddeclaration:	PUBLIC type Identifier L_PAREN method_arguments R_PAREN L_CURLY classtypes statement_list RETURN expression SEMICOLON R_CURLY{
							$$ = (char*) malloc((strlen($2)+strlen($3)+strlen($5)+strlen($8)+strlen($9)+strlen($11)+50)*sizeof(char));
							strcpy($$, "public "); strcat($$, $2); strcat($$," "); strcat($$, $3); strcat($$, "("); strcat($$, $5); strcat($$, "){\n"); strcat($$, $8); strcat($$, "\n"); strcat($$, $9); strcat($$, "\n"); strcat($$, "return "); strcat($$, $11); strcat($$, ";\n}\n");
							free($2); free($3); free($5); free($8); free($9); free($11);
							//printf("Contents of the method are: %s\n", $$);
}
;

method_arguments: type Identifier argument_list {// Arguments that the method takes
					$$ = (char*) malloc((strlen($1)+strlen($2)+strlen($3)+10)*sizeof(char));
					strcpy($$, $1); strcat($$," "); strcat($$, $2); strcat($$, $3);
					free($1); free($2); free($3);
}
				 |         		{$$ = (char*) malloc(sizeof(char));$$[0] = '\0';}
; 

argument_list:	COMMA type Identifier argument_list {// If there are multiple comma seperated arguments
					$$ = (char*) malloc((strlen($2)+strlen($3)+strlen($4)+10)*sizeof(char));
					strcpy($$, ", "); strcat($$, $2); strcat($$," "); strcat($$, $3); strcat($$, $4);
					free($2); free($3); free($4);
}
				| 				{$$ = (char*) malloc(sizeof(char));$$[0] = '\0';}
;		

statement_list: statement statement_list {
					$$ = (char*) malloc((strlen($1)+strlen($2)+10)*sizeof(char));
					strcpy($$, $1);	strcat($$, $2);	
					free($1); free($2);
}
				| 				{$$ = (char*) malloc(sizeof(char));$$[0] = '\0';}
;	// Multiple statements

type:	INTEGER L_SQUARE R_SQUARE 	{	$$ = (char*) malloc(sizeof(char)*10); strcpy($$, "int[] ");	}
		|	BOOLEAN 				{	$$ = (char*) malloc(sizeof(char)*10); strcpy($$, "boolean ");	}
		|	INTEGER 				{	$$ = (char*) malloc(sizeof(char)*10); strcpy($$, "int ");	}
		|	Identifier 				{	$$ = (char*) malloc(sizeof(char)*(strlen($1)+10)); strcpy($$, $1); free($1);	}
;

statement:	L_CURLY statement_list R_CURLY 	{$$ = (char *) malloc((strlen($2)+10)*sizeof(char)); strcpy($$,"{\n "); strcat($$,$2); strcat($$, " }\n"); free($2); }// List of statements in a block and for if, else and while blocks
			|	SYSTEM_PRINT L_PAREN expression R_PAREN SEMICOLON   {$$ = (char *) malloc((strlen($3)+35)*sizeof(char)); strcpy($$, "System.out.println("); strcat($$,$3); strcat($$,");\n"); free($3); }
			|	Identifier EQUALS expression SEMICOLON 	{$$ = (char*) malloc((strlen($1)+strlen($3)+15)*sizeof(char)); strcpy($$, $1); strcat($$, " = "); strcat($$,$3); strcat($$, ";\n"); free($1); free($3); }
			|	Identifier L_SQUARE expression R_SQUARE EQUALS expression SEMICOLON  {$$ = (char*) malloc((strlen($1)+strlen($3)+strlen($6)+15)*sizeof(char));  strcpy($$, $1); strcat($$,"["); strcat($$, $3); strcat($$,"] = "); strcat($$, $6);  strcat($$, ";\n"); free($1); free($3); free($6); }
			|	IF L_PAREN expression R_PAREN statement_list  { $$ = (char*) malloc((strlen($3)+strlen($5)+20)*sizeof(char)); strcpy($$, "if("); strcat($$, $3); strcat($$, ")"); strcat($$, $5); free($3); free($5); }
			|	IF L_PAREN expression R_PAREN statement_list ELSE statement_list  { $$ = (char*) malloc((strlen($3)+strlen($5)+strlen($7)+25)*sizeof(char)); strcpy($$, "if("); strcat($$, $3); strcat($$, ")"); strcat($$, $5); /*strcat($$, "\n");*/ strcat($$, "else "); strcat($$, $7); free($3); free($5); free($7);}
			|	WHILE L_PAREN expression R_PAREN statement_list  { $$ = (char*) malloc((strlen($3)+strlen($5)+20)*sizeof(char)); strcpy($$, "while("); strcat($$, $3); strcat($$, ")"); strcat($$, $5); free($3); free($5);}
			|	Identifier L_PAREN expression expression_comma R_PAREN SEMICOLON { /*printf("In statement macro\n");*/ char* temp = (char*) malloc((strlen($3)+strlen($4)+15)*sizeof(char)); strcpy(temp, $3); strcat(temp, $4); $$ = replace_macro($1, temp, 1); /*strcat($$, ";\n");*/ free($3); free($4); free(temp);}		/* Macro stmt call with expression list*/
			|	Identifier L_PAREN R_PAREN SEMICOLON 	{$$ = replace_macro($1, NULL, 1);  strcat($$,";\n");}  	// Macro statement call with void type argument list
;

expression_comma: COMMA expression expression_comma 	{$$ = (char*) malloc((strlen($2)+strlen($3)+10)); strcpy($$, ", "); strcat($$, $2); strcat($$, $3); free($2); free($3);}
					| 		{$$ = (char*) malloc(sizeof(char)); $$[0] = '\0';}
;

expression:     primaryexpression AND primaryexpression	{$$ = (char*) malloc(strlen($1)+strlen($3)+10); strcpy($$, $1); strcat($$, "&&"); strcat($$, $3); free($1); free($3);}
			|	primaryexpression OR primaryexpression  {$$ = (char*) malloc(strlen($1)+strlen($3)+10); strcpy($$, $1); strcat($$, "||"); strcat($$, $3); free($1); free($3);}
			|	primaryexpression NE primaryexpression	{$$ = (char*) malloc(strlen($1)+strlen($3)+10); strcpy($$, $1); strcat($$, "!="); strcat($$, $3); free($1); free($3);}
			|	primaryexpression LT EQUALS primaryexpression	{$$ = (char*) malloc(strlen($1)+strlen($4)+10); strcpy($$, $1); strcat($$, "<="); strcat($$, $4); free($1); free($4);}
			|	primaryexpression PLUS primaryexpression		{$$ = (char*) malloc(strlen($1)+strlen($3)+10); strcpy($$, $1); strcat($$, "+"); strcat($$, $3); free($1); free($3);}
			|	primaryexpression MINUS primaryexpression		{$$ = (char*) malloc(strlen($1)+strlen($3)+10); strcpy($$, $1); strcat($$, "-"); strcat($$, $3); free($1); free($3);}
			|	primaryexpression MUL primaryexpression			{$$ = (char*) malloc(strlen($1)+strlen($3)+10); strcpy($$, $1); strcat($$, "*"); strcat($$, $3); free($1); free($3);}
			|	primaryexpression DIV primaryexpression			{$$ = (char*) malloc(strlen($1)+strlen($3)+10); strcpy($$, $1); strcat($$, "/"); strcat($$, $3); free($1); free($3);}
			|	primaryexpression L_SQUARE primaryexpression R_SQUARE		{$$ = (char*) malloc(strlen($1)+strlen($3)+15); strcpy($$, $1); strcat($$, "["); strcat($$, $3); strcat($$, "]"); free($1); free($3);}
			|	primaryexpression LENGTH 	{$$ = (char*) malloc((strlen($1)+15)*(sizeof(char))); strcpy($$, $1); strcat($$, ".length"); free($1);}// LENGTH contains the token .length
			|	primaryexpression 			{$$ = (char*) malloc((strlen($1)+10)*(sizeof(char))); strcpy($$, $1); free($1);}
			|	primaryexpression DOT Identifier L_PAREN expression expression_comma R_PAREN {$$ = (char*) malloc((strlen($1)+strlen($3)+strlen($5)+strlen($6)+20)*sizeof(char)); strcpy($$, $1); strcat($$, "."); strcat($$, $3); strcat($$, "("); strcat($$, $5); strcat($$, $6); strcat($$,")"); free($1); free($3);  free($5);  free($6);}
			|	primaryexpression DOT Identifier L_PAREN R_PAREN 	{$$ = (char*) malloc((strlen($1)+strlen($3)+20)*sizeof(char)); strcpy($$, $1); strcat($$, "."); strcat($$, $3); strcat($$, "()"); free($1); free($3);}
			|	Identifier L_PAREN expression expression_comma R_PAREN	{ /*printf("In the right place\n");*/ char *temp = (char*) malloc((strlen($3)+strlen($4)+10)*sizeof(char)); /*strcpy(temp, "(");*/ strcpy(temp, $3); strcat(temp, $4); /*strcat(temp, ")");*/ $$ = replace_macro($1, temp, 0); free($3); free($4); free(temp);} 	/* Macro expr call */
			|	Identifier L_PAREN R_PAREN 			{$$ = replace_macro($1, NULL, 0);}			/* Macro expr call without argument list */
;

primaryexpression:	number 	{$$ = (char*) malloc((strlen($1)+10)*sizeof(char)); strcpy($$, $1); free($1);}// Represents a number
				|	TRUE	{$$ = (char*) malloc(10*sizeof(char)); strcpy($$, "true ");}
				|	FALSE	{$$ = (char*) malloc(10*sizeof(char)); strcpy($$, "false ");}
				|	Identifier 	{$$ = (char*) malloc((strlen($1)+10)*sizeof(char)); strcpy($$, $1); free($1);}
				|	THIS	{$$ = (char*) malloc(10*sizeof(char)); strcpy($$, "this");}
				|	NEW INTEGER L_SQUARE expression R_SQUARE 	{$$ = (char*) malloc((strlen($4)+20)*sizeof(char)); strcpy($$, "new int["); strcat($$, $4); strcat($$, "]"); free($4);}
				|	NEW Identifier L_PAREN R_PAREN 				{$$ = (char*) malloc((strlen($2)+15)*sizeof(char)); strcpy($$, "new "); strcat($$, $2); strcat($$, "()"); free($2);}
				|	NOT expression 		{$$ = (char*) malloc((strlen($2)+5)*sizeof(char)); $$ = strcpy($$, "!"); strcat($$, $2); free($2);}
				|	L_PAREN expression R_PAREN 	{$$ = (char*) malloc((strlen($2)+10)*sizeof(char)); strcpy($$,"("); strcat($$, $2); strcat($$, ")"); free($2);}
;

macrodefinition:	macrodefexpression
				|	macrodefstatement
;

macrodefstatement:	DEFINE Identifier L_PAREN Identifier Identifier_comma R_PAREN L_CURLY statement_list R_CURLY{
						char *temp = (char*) malloc((strlen($4)+strlen($5)+10)*sizeof(char)); strcpy(temp, $4); strcat(temp, $5);
						char *stat =  (char*) malloc((strlen($8)+10)*sizeof(char)); strcpy(stat, "{"); strcat(stat, $8); strcat(stat,"}");
						char *dec = (char*) malloc(strlen($2)+10); strcpy(dec, $2);
						free($4); free($5); free($8); add_to_table(dec, stat, temp, 1); free($2);
}
					|	DEFINE Identifier L_PAREN R_PAREN L_CURLY statement_list R_CURLY	{
						char *temp = (char*) malloc((strlen($6)+10)*sizeof(char)); strcpy(temp,"{"); strcat(temp,$6); strcat(temp, "}"); free($6); 
						char *dec = (char*) malloc(strlen($2)+10); strcpy(dec, $2); add_to_table(dec, temp, NULL, 1); free($2);
}
;

macrodefexpression:	DEFINE Identifier L_PAREN Identifier Identifier_comma R_PAREN L_PAREN expression R_PAREN{
						char *temp = (char*) malloc((strlen($4)+strlen($5)+10)*sizeof(char)); strcpy(temp, $4); strcat(temp, $5);
						char *stat =  (char*) malloc((strlen($8)+10)*sizeof(char)); strcpy(stat, "("); strcat(stat, $8); strcat(stat,")");
						char *dec = (char*) malloc(strlen($2)+10); strcpy(dec, $2);
						free($4); free($5); free($8); add_to_table(dec, stat, temp, 0); free($2); //printf("part-1\n");
}
					|	DEFINE Identifier L_PAREN R_PAREN L_PAREN expression R_PAREN{
						char *temp = (char*) malloc((strlen($6)+10)*sizeof(char)); strcpy(temp,"("); strcat(temp,$6); strcat(temp, ")"); free($6); 
						char *dec = (char*) malloc(strlen($2)+10); strcpy(dec, $2);
						add_to_table(dec, temp, NULL, 0);	free($2);
}
;

Identifier_comma: COMMA Identifier Identifier_comma 	{$$ = (char*) malloc((strlen($2)+strlen($3)+5)*sizeof(char)); strcpy($$, ","); strcat($$, $2); strcat($$,$3); free($2); free($3);}
				|	{$$ = (char*) malloc(2*sizeof(char)); $$[0] = '\0';}
;

Identifier: ID 	{$$ = (char*) malloc((strlen($1)+5)*sizeof(char)); strcpy($$, $1);}		// Dont put free here because it is a stack variable
;

number: 	NUM 	{$$ = (char*) malloc((strlen($1)+5)*sizeof(char)); strcpy($$, $1); strcat($$, " ");} 	// Dont put free here because it is a stack variable
;


%%
int yywrap() {return 1;}
int yyerror(char* s) {fprintf(stderr,"// Failed to parse macrojava code.");}
int main()
{
	yyparse();
	exit(0);
	return 0;
}
