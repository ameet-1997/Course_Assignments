#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

int main()
{
	// FILE *fp = fopen("write_test_file.txt","w");
	fork();
	FILE *fp = fopen("write_test_file.txt","a");
	for(int i=0;i<5;++i)
	{
		fprintf(fp,"%c",i+'a');
	}
	fprintf(fp, "\n");
} 
