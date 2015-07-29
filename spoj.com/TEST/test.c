#define _GNU_SOURCE
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

int main(void){
    char* pos_n;
    size_t len = 0;
    char *line = calloc(sizeof(char), len + 1);

    while(-1 != getline(&line, &len, stdin)){
        char *endptr = NULL;
        if((pos_n = strchr(line, '\n')) != NULL){
            *pos_n = '\0';
        }
        int conv = strtol(line, &endptr, 10);
        if(endptr == line){
            printf("Error: %s\n", endptr);
            continue;
        }
        if(conv == 42){
            break;
        }
        printf("%i\n", conv);
        free(line);
    }
    return EXIT_SUCCESS;
}
