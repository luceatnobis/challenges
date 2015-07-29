#include <stdio.h>
#include <string.h>

int main(int arc, char* argv[]){

	char buffer[10];
	strncpy(buffer, argv[1],10);
	printf("You entered: %s", buffer);
	return 0;
}
