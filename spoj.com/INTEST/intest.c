// http://www.spoj.com/problems/INTEST/

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdint.h>

void process_case(FILE* input);

int main(int argc, char *argv[]){
    char *line = NULL;
    uint64_t i, len = 0, testcase_count;
    FILE *input = NULL;

    // lets figure out if we read from a file or from stdin
    if(argc == 2){  // we are reading from file
        if(access(argv[1], R_OK)){
            fprintf(stderr, "Could not access file %s\n", argv[1]);
            return EXIT_FAILURE;
        }
        input = fopen(argv[1], "r");
    } else {
        input = stdin;
    }
    /*
    getline(&line, &len, input);
    testcase_count = atol(line);

    for(i = 0; i < testcase_count ; i++){
        process_case(input);
    }
    free(line);
    */
    process_case(input);
    return EXIT_SUCCESS;
}

void process_case(FILE* input){
    char *line = NULL, *tokptr = NULL;
    uint64_t i, n, k, x, div_counter = 0;
    uint64_t len = NULL;

    getline(&line, &len, input);
    tokptr = strtok(line, " ");
    n = atol(tokptr);

    tokptr = strtok(NULL, " ");
    k = atol(tokptr);
    free(line);
    line = NULL;

    for(i = 0; i < n; i++){
        getline(&line, &len, input);
        x = atol(line);
        if(x % k == 0)
            div_counter++;
    }
    printf("%lu\n", div_counter);
    free(line);
}
