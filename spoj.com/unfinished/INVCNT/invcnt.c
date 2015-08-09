// http://www.spoj.com/problems/INVCNT/

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>
#include <malloc.h>

void process_case(FILE* input);

int main(int argc, char *argv[]){
    char *line;
    uint64_t len = 0, i, testcase_n;
    FILE *input = NULL;

    if(argc == 2){  // we are reading from file
        if(access(argv[1], R_OK)){
            fprintf(stderr, "Could not access file %s\n", argv[1]);
            return EXIT_FAILURE;
        }
        input = fopen(argv[1], "r");
    } else {
        input = stdin;
    }
    getline(&line, &len, input);
    testcase_n = atol(line);
    free(line);
    line = NULL;

    // we have a blank space between t and the cases so we consume it
    getline(&line, &len, input);
    free(line);
    line = NULL;

    for(i = 0; i < testcase_n; i++){
        process_case(input);
    }
    return EXIT_SUCCESS;
}

void process_case(FILE* input){
    char *line = NULL;
    int64_t i, j, n;
    uint64_t len = 0, inv_count = 0;
    uint64_t *A;

    getline(&line, &len, input);
    n = atol(line);
    free(line);
    line = NULL;

    A = calloc(sizeof(uint64_t), n);
    getline(&line, &len, input);
    A[0] = atol(line);
    free(line);
    line = NULL;

    for(j = 1; j < n; j++){
        getline(&line, &len, input);
        A[j] = atol(line);
        free(line);
        line = NULL;

        for(i = j - 1; i >= 0; i--){
            if(A[i] > A[j])
                inv_count++;
        }
    }
    free(A);
    printf("%lu\n", inv_count);
    
    // testcase ends with blank line so we consume it
    getline(&line, &len, input);
    free(line);
    line = NULL;
}
