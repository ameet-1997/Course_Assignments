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
		printf("In Child Process, Process ID: %d\n", getpid());
	}
} 
