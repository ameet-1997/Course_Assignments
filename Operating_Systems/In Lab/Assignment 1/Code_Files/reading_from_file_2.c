#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

// Code for opening file pointer after forking the process

int main()
{	
	// FILE *fp = fopen("test_file.txt","r");
	fork();
	FILE *fp = fopen("test_file.txt","r");
	char c = fgetc(fp);
	while(c != EOF)
	{	
		putchar(c);
		// Prints to stdout, whatever is in the buffer
		fflush(stdout);
		c = fgetc(fp);
	}

	// printf("Hello World\n");
	return 0;
} 
