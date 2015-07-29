#include <stdio.h>
#include <stdarg.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

uint64_t max_args(uint64_t first, ...);
uint64_t max_field(uint64_t n, uint64_t* field);
uint64_t triangle_sum(uint64_t n, uint64_t **triangle);
uint64_t process_triangle(FILE* input);

int main(int argc, char *argv[]){
    char *line;
    uint64_t len = 0, i, triangle_count;
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
    triangle_count = atol(line);
    for(i = 0; i < triangle_count; i++){
        printf("%lu\n", process_triangle(input));

    }
    return EXIT_SUCCESS;
}

uint64_t process_triangle(FILE *input){
    char *line, *tokptr;
    size_t len = 0, read, lines;
    uint64_t i = 0, j = 0, line_n = 0;
    uint64_t **triangle;
       
    getline(&line, &len, input);
    lines = atol(line);
    triangle = malloc(sizeof(uint64_t*) * (lines + 1));

    for(j=0; i < lines; j++){
        read=getline(&line, &len, input);
        i = 0;
        uint64_t *n_field;
        read = read - 1;
        line[read] = '\0';

        n_field = malloc(sizeof(uint64_t) * (line_n + 1));
        
        tokptr = strtok(line, " ");
        while(tokptr != NULL){
            n_field[i] = atoi(tokptr);
            tokptr = strtok(NULL, " ");
            i += 1;
        }
        triangle[line_n] = n_field;
        line_n += 1;
    }
    return triangle_sum(lines, triangle);
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
            nl[j] = max_args(2, l[j-1], l[j]);
            nl[j] +=  r[j];
        }
        nl[i] = l[j-1] + r[j];
        free(l);
        l = nl;
    }
    sum = max_field(n, l);
    free(l);
    for(i = 1; i < n; i++){
        free(triangle[i]);
    }
    free(triangle);
    return sum;
}

uint64_t max_field(uint64_t n, uint64_t *field){
    uint64_t i, max;
    if(n == 1)
        return field[0];
    max = field[0];
    for(i = 1; i < n; i++){
        if(max < field[i]){
            max = field[i];
        }
    }
    return max;
}

uint64_t max_args(uint64_t n, ...){
    uint64_t i, a, max;
    va_list ap;

    va_start(ap, n);
    max = va_arg(ap, uint64_t);
    for(i = 1; i < n; i++){
        if ((a = va_arg(ap, uint64_t)) > max)
            max = a;
    }
    return max;
}
