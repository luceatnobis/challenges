#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <malloc.h>
#include <stdlib.h>
#include <unistd.h>

#define TUP_LEN 6

void process_case(FILE*);

int main(int argc, char *argv[]) {

    int testcase_count = NULL;
    size_t len = NULL, i = NULL;
    char *line = NULL;
    FILE *input = NULL;

    // lets figure out if we read from a file or from stdin
    if(argc == 2){  // we are reading from file
        if(access(argv[1], R_OK)){
            fprintf(stderr,"Could not access file %s\n", argv[1]);
            return EXIT_FAILURE;
        }
        input = fopen(argv[1],"r");
    } else {
        input = stdin;
    }
    getline(&line, &len, input);
    testcase_count = atol(line);

    for(i = 0; i < testcase_count ; i++){
        process_case(input);
    }
    free(line);
    fclose(input);
    return EXIT_SUCCESS;
}

void process_case(FILE* input){
    char *line = NULL, *t_ptr = NULL, *s_ptr = NULL, *endptr, *solution = NULL;
    ssize_t read = NULL;
    size_t len = NULL, i = NULL, j = NULL;

    uint64_t *n_tuples = malloc(sizeof(uint64_t));
    uint64_t *res = malloc(2 * sizeof(uint64_t));

    getline(&line, &len, input);
    endptr = line;
    *n_tuples = strtol(line, &endptr, 10);
    solution = calloc(*n_tuples * 2, sizeof(char));

    read = getline(&line, &len, input) - 1;
    line[read] = '\0';

    read = getline(&s_ptr, &len, input) - 1;
    s_ptr[read] = '\0';

    t_ptr = strtok(line, " ");
    for(;t_ptr; j++){
        memset((void*)res, 0, sizeof(uint64_t) * 2);
        for(i = 0; i < TUP_LEN; i++){
            res[0] |= t_ptr[i] & (1 << i);
            if(t_ptr[i] & (1 << ((i + 3) % 6))){
                res[1] ^= (1 << i);
            }
        }
        solution[j*2] = s_ptr[res[0]];
        solution[j*2+1] = s_ptr[res[1]];

        t_ptr = strtok(NULL, " ");
    }
    printf("%s\n", solution);
    getline(&line, &len, input);

    free(res);
    free(line);
    free(s_ptr);
    free(t_ptr);
    free(solution);
    free(n_tuples);
}
