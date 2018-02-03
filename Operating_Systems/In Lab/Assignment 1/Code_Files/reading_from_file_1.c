#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h> 

//Code for opening file pointer before fork

int main()
{	
	FILE *fp = fopen("test_file.txt","r");
	fork();
	// FILE *fp = fopen("test_file.txt","r");
	char c = fgetc(fp);
	while(c != EOF)
	{	
		putchar(c);
		c = fgetc(fp);
	}

	// printf("Hello World\n");
	return 0;
}