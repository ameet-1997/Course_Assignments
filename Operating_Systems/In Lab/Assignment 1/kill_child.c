#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <signal.h>

int main()
{
	int pid = fork();

	if(pid)
	{
		kill(pid, SIGTERM);
	}

	printf("Print\n");
} 
