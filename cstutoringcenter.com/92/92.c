#include <stdio.h>
#include <stdlib.h>

#define MAX_LIMIT 10000000

int main(){

	unsigned int a, b, val, dist; // a = b + 1
	long sum = 0;

	for(a = 1;a<=MAX_LIMIT;a++){
		dist = 0;
		b = a - 1;
		val = a ^ b;
		
		while(val){
			++dist;
			val &= val -1;
		}
		sum += dist;
	}
	printf("Summe: %li\n", sum);
    return EXIT_SUCCESS;
}
