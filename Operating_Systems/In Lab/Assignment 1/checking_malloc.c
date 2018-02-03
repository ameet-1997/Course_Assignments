#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

int main()
{
	int *pt;
	int i=0;
	pt = (int*) malloc(sizeof(int));
	*pt = 0;
	fork();

	(*pt)++;

	printf("The value is: %d\n", *pt);
	printf("The value of the pointer is: %p\n",pt);
	printf("The address value of variable is: %p\n",&i);
} 
