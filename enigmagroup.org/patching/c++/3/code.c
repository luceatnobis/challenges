#include <cstdio>
#include <cstdlib>
#include <cstring>
 
void Authorize(){
	// Authorize user!
	printf("You are authorized!\n");
}
 
int main()
{
	char c = 'A';
	char buffer[10];
	char password[] = "ninechars";
	 
	printf("Addr of c: %x\nAddr of buffer: %x\n\n",&c,buffer);
	 
	printf("Please enter your password: ");
	scanf("%s",buffer);
	 
	if(strcmp(buffer,password)==0) c = 0;
	 
	printf("Value of c = %d\n\n",c);
 
	c == 0 ? Authorize() : exit(1) ;

	system("pause");
}
