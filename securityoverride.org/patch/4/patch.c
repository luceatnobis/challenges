#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]){
	
	char buffer[3];
	strncpy(buffer, argv[1], 3);
	printf("%s",buffer);
	return 0;
}
