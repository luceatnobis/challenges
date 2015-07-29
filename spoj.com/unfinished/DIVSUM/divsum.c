#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#include <malloc.h>
#include <math.h>

long divsum(long n);

int main(int argc, char *argv[]){

    long n_testcases, i, j;
    long len = 0;
    char *line, *endptr;

    // get first line
    getline(&line, &len, stdin);
    n_testcases = strtol(line, &endptr, 10);
    printf("Goign to read %lu lines\n", n_testcases);
    uintptr_t *nums = malloc(sizeof(long) * n_testcases);

    /*
    for(i=0; i < n_testcases; i++){
        getline(&line, &len, stdin);
        long penis = strtol(line, &endptr, 10);
        divsum(penis);
    }
    for(i=0; i < n_testcases; i++){
        for(j = 0; j < i; j++){
            if(nums[i] == nums[j]){
                nums[j] = nums[i];
            }
        }
    }
    */
    /*
    for(i = 0; i < n_testcases; i++){
        printf("%d\n", nums[i]);
    }
    */
    return EXIT_SUCCESS;
}

long divsum(long n){
    long sum = 0, i, i_stop;
    if(n % 2 == 0){ // n is even
        i_stop = n / 2;
        for(i = 1; i <= i_stop; i++){
            if(n % i == 0){
                sum += i;
            }
        }
    }
    else{
        i_stop = (n-1) / 2;
        for(i = 1; i < i_stop; i+=2){
            if(n % i == 0){
                sum += i;
            }
        }
    }
    // printf("%lu => %lu\n", n, sum);
    return sum;
}
