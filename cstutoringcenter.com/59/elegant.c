#include <stdio.h>
#include <stdarg.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

uint64_t triangle_sum(uint64_t n, uint64_t **triangle);
uint64_t min_field(uint64_t n, uint64_t* field);
uint64_t min_args(uint64_t first, ...);

int main(int argc, char *argv[]){
    char *line, *tokptr;
    size_t len = 0, read;
    uint64_t tok_n, sum, l_len = 0, i = 0, line_n = 0;
    uint64_t **triangle = malloc(sizeof(uint64_t*) * 100);
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

    while((read=getline(&line, &len, input)) != EOF){
        uint64_t *n_field;
        tok_n = 0;
        read = read - 1;
        line[read] = '\0';
        if(strlen(line) == 0){
            fprintf(stderr, "lol no hahahah\n");
            return EXIT_FAILURE;
        }
        for(i=0; i < read; i++){
            if(line[i] == 0x20){
                tok_n += 1;
            }
        }
        n_field = malloc(sizeof(uint64_t) * tok_n);
        
        tokptr = strtok(line, " ");
        for(i=0; i < tok_n; i++){
            n_field[i] = atoi(tokptr);
            tokptr = strtok(NULL, " ");
        }
        triangle[line_n] = n_field;
        line_n += 1;
    }

    sum = triangle_sum(line_n, triangle);
    
    for(i=line_n; i; i--){
        free(triangle[i]);
    }
    free(triangle);
    printf("%lu\n", sum);
}

uint64_t triangle_sum(uint64_t n, uint64_t **triangle){
    uint64_t i, j, sum;
    uint64_t *r, *l, *nl;

    l = triangle[0];
    for(i = 1; i < n; i++){
        nl = malloc(sizeof(uint64_t) * (i+1));
        r = triangle[i];
        nl[0] = l[0] + r[0];
        for(j = 1; j < i; j++){
            nl[j] = min_args(2, l[j-1], l[j]);
            nl[j] +=  r[j];
        }
        nl[i] = l[j-1] + r[j];
        l = nl;
    }
    sum = min_field(n, l);
    free(l);
    return sum;
}

uint64_t min_field(uint64_t n, uint64_t *field){
    uint64_t i, min;
    if(n == 1)
        return field[0];
    min = field[0];
    for(i = 1; i < n; i++){
        if(min > field[i]){
            min = field[i];
        }
    }
    return min;
}

uint64_t min_args(uint64_t n, ...){
    uint64_t i, a, min;
    va_list ap;

    va_start(ap, n);
    min = va_arg(ap, uint64_t);
    for(i = 1; i < n; i++){
        if ((a = va_arg(ap, uint64_t)) < min)
            min = a;
    }
    return min;
}
