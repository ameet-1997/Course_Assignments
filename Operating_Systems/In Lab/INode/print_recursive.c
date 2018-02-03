#include <unistd.h>
#include <sys/types.h>
#include <dirent.h>
#include <stdio.h>
#include <string.h>
#include <sys/stat.h>

void list_recursive(const char *name, int spaces)
{
    DIR *dir;
    struct dirent *entry;

    if(!(dir = opendir(name))) 	// If the directory does not exist
    {
    	return;
    }

    while((entry = readdir(dir)) != NULL)
    {
        if(entry->d_type == DT_DIR) 	// If the "file" is a directory, call recursively
        {
            char path[1024];
            if(strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0) 	// If parent directory or current, then dont print
            {																			// Else stack overflow
                continue;
            }
            snprintf(path, sizeof(path), "%s/%s", name, entry->d_name); 				// Print the path to a string
            struct stat s;
            stat(path, &s);
            printf("%ld :: ", (long) s.st_ino);
            printf("%*s[%s]\n", spaces, "", entry->d_name);
            list_recursive(path, spaces + 2);
        }
        else
        {	
        	struct stat s;
        	char path[1024];
        	snprintf(path, sizeof(path), "%s/%s", name, entry->d_name);
        	stat(path, &s);
      		printf("%ld :: ", (long) s.st_ino);
            printf("%*s- %s\n", spaces, "", entry->d_name);
        }
    }
    closedir(dir);
}

int main(void) {
    list_recursive(".", 0); 	// Call the function on current directory
    return 0;
}