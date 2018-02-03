#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

int main()
{
	// FILE *fp = fopen("write_test_file.txt","w");
	fork();
	FILE *fp = fopen("write_test_file.txt","w");
	for(int i=0;i<5;++i)
	{
		fprintf(fp,"%c",i+'a');
	}
	fprintf(fp, "\n");
}

// // Code for showing that file pointers and variables are handled differently

// int main()
// {
// 	int i=0;
// 	fork();
// 	i++;
// 	printf("The value of i is: %d\n",i);
// }

// // Code for opening file pointer after forking the process

// int main()
// {	
// 	// FILE *fp = fopen("test_file.txt","r");
// 	fork();
// 	FILE *fp = fopen("test_file.txt","r");
// 	char c = fgetc(fp);
// 	while(c != EOF)
// 	{	
// 		putchar(c);
// 		fflush(stdout);
// 		c = fgetc(fp);
// 	}

// 	// printf("Hello World\n");
// 	return 0;
// }

// Code for opening file pointer before fork

// int main()
// {	
// 	// FILE *fp = fopen("test_file.txt","r");
// 	fork();
// 	FILE *fp = fopen("test_file.txt","r");
// 	char c = fgetc(fp);
// 	while(c != EOF)
// 	{	
// 		putchar(c);
// 		c = fgetc(fp);
// 	}

// 	// printf("Hello World\n");
// 	return 0;
// }
