#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main(int argc, char** argv){

	if(argc != 3) return 0;

	int iFirstNum = atoi(argv[1]);
	int iSecondNum = atoi(argv[2]);

	if(iSecondNum == 0){
		return 0;
	}

	printf("FirstNum: %d\n", iFirstNum);
	printf("SecondNum: %d\n", iSecondNum);

	int iResult = (iFirstNum / iSecondNum);

	printf("Result: %d\n\n", iResult);

