#include <sys/stat.h>
#include <stdio.h>
#include <time.h>

int main()
{
	struct stat s; 												// Structure to store file information
   	stat("os.txt", &s); 										// Store the information about file
   	printf("INode Number of file: %ld\n", (long) s.st_ino); 	// Print details about the file
   	printf("Size of the file is: %ld KB\n", (long) s.st_size);	
}