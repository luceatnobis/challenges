#include <cstdio>
#include <cstring>

int main(int argc, char** argv)
{
	if(argc != 2) return 0;
	
	char Buffer[10];
	memset(Buffer, 0, 10);
	strncpy(Buffer, argv[1],9);
	printf("%s\n",Buffer);
	return 1;
}
