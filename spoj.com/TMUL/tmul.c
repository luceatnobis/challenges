// http://www.spoj.com/problems/TMUL/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>

int main(int argc, char *argv[]){
    uint64_t len = 1, i, testcase_count;
    uint64_t x, y;
    char *line = malloc(len), *tokptr;
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
    testcase_count = atol(line);
    for(i = 0; i < testcase_count; i++){
        getline(&line, &len, input);
        tokptr = strtok(line, " ");
        x = atol(tokptr);

        tokptr = strtok(NULL, " ");
        y = atol(tokptr);
        printf("%lu\n",  x * y);

    }
    free(line);
    fclose(input);
    return EXIT_SUCCESS;
}
