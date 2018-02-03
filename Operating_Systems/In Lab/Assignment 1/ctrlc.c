#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

int main()
{
	int pid = fork();

	if(pid)
	{
		printf("Current Process: %d\n", getpid());
		printf("Child Process: %d\n", pid);
	}
	else
	{	
		for(int i=0;i<100000000;++i)
		{
			printf("In Child Process\n");	
		}
	}
} 
 
