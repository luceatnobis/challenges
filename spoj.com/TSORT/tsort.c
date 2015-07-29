// http://www.spoj.com/problems/TSORT/

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdint.h>

int comp(int *a, int *b);

int main(int argc, char *argv[]){
    char *line = NULL;

    int i, n, read;
    size_t len = 0;
    int *numbers;

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

    getline(&line, &len, input);
    n = atol(line);
    free(line);
    line = NULL;

    numbers = malloc(n * sizeof(int));
    for(i = 0; i < n; i++){
        getline(&line, &len, input);
        numbers[i] = atoi(line);
        free(line);
        line = NULL;
    }
    qsort(numbers, n, sizeof(int), (void*)comp);
    for(i = 0; i < n; i++){
        printf("%i\n", numbers[i]);
    }
    free(numbers);
    return EXIT_SUCCESS;
}

int comp(int *a, int *b){

    int x = *(const int *)a;
    int y = *(const int *)b;
    if(x == y)
        return 0;
    return x < y ? -1 : 1;
}
