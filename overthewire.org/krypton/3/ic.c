#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>

#define BUF 1024

int* frequency_count(char* filename, int* dict);
char* caesar_shift(char* filename, char shift);

int main(){

	int i;
	int dict[SCHAR_MAX] = {0};

	char imax = 0, shift = 0; //0x45 - 0x41
	char* filename = "HINTS";

	frequency_count(filename, dict);

	for(i = 0x61; i <= 0x7a; i++){
		dict[i - 0x20] += dict[i];
		dict[i] ^= dict[i];
	}
	
	for(i = 0; i < 0x61; i++){
		if(dict[i] > dict[imax]){
			imax = i;
		}
	}

	for(i = 0; i < SCHAR_MAX; i++){
		printf("%c: %i\n", i, dict[i]);
	}

	// determine shift in modular system
	for(i = 0; i < 26; i++){
		if ((imax - 0x41 + i) % 26 == 4){
			shift = i;
			break;
		}
	}

	return EXIT_SUCCESS;
	
	caesar_shift(filename, shift);
}

int* frequency_count(char* filename, int* dict){

	FILE* f;
	int i;
	char buf[BUF] = {0};

	f = fopen(filename, "r");

	while( fgets(buf, BUF, f) ){
	
		for(i = 0; buf[i]; i++){
			if (buf[i] > 0x20 && buf[i] < 0x7f){
				dict[ buf[i] ] += 1;
			}
		}
	}
	fclose(f);
	
	return dict;
}

char* caesar_shift(char* filename, char shift){

	int i;
	FILE* fp;
	char* src_buf, wchar;
	long filesize;

	fp = fopen(filename, "r");
	fseek(fp, 0L, SEEK_END);
	filesize = ftell(fp);
	fseek(fp, 0, SEEK_SET);

	src_buf = calloc(filesize, sizeof(char));
	fgets(src_buf, filesize, fp);

	for(i = 0; src_buf[i]; i++){
		if(src_buf[i] != 0x20){
			wchar = src_buf[i] - 0x41;
			wchar = ((wchar + shift) % 26) + 0x41;
			src_buf[i] = wchar;
		}
	}
	
	printf("%s\n", src_buf);
	return filename;
}
