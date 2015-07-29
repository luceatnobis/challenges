#include <stdio.h>

int main(){
	char original []= {"lol.php"};
	char newFileName [] = {'l','\0','o','l'};
	int renameFile = 0;
	
	renameFile = rename(original, newFileName);
	if(renameFile!=0){
		perror("Error in renaming file.");
	}
}
