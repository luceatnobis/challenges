#include <stdio.h>
#include <ctype.h>
#include <assert.h>
#include <stdint.h>
#include <string.h>
#include <malloc.h>
#include <stdlib.h>
#include <unistd.h>

#define MAX_EXP_LEN 400 // given in task description

char r_assoc[] = {"^"};
char l_assoc[] = {"+-/*"};

char operators[] = {"+-/*^"}; // ascending priority
char precedences[] = {"+\02-\02/\03*\03^\04"}; // ascending priority
char allowed[] = {"abcdefghijklmnopqrstuvwxyz0123456789+-/*^()"};

void process_case(FILE *input);
void stack_push(uint64_t *i, char *s, char c);
char stack_pop(uint64_t *i, char *s);

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
    char t;
    char *line = NULL, *stack = NULL, *sptr = NULL, *endptr = NULL;
    ssize_t read = NULL;
    size_t len = NULL, i = NULL;

    uint64_t l_prec = 0, s_prec = 0;
    uint64_t* s_index = malloc(sizeof(uint64_t) * 1);
    *s_index = 0;

    read = getline(&line, &len, input) - 1;
    stack = calloc(read, sizeof(char));
    line[read] = '\0';
    endptr = line;

    for(; i < read; i++){
       if(strchr(allowed, line[i]) == NULL){
           fprintf(stderr,"Disallowed \"%c\" at %lu\n", line[i], i);
           exit(1);
        }
        if(line[i] == '(')
            stack_push(s_index, stack, line[i]);
        if(line[i] == ')')
            while((t=stack_pop(s_index, stack))){
                if(t == '(')
                    break;
                printf("%c", t);
            }
        else if(isdigit(line[i])){
            sptr = line + i;
            printf("%lu", strtol(sptr, &endptr, 10));
            i += (endptr - sptr - 1);
        }
        else if(isalpha(line[i])){
            printf("%c", line[i]);
        }
        else if(strchr(operators, line[i]) != 0){
            while((stack[*s_index-1] != '\0' && strchr(operators, stack[*s_index-1]) != NULL)){
                l_prec = precedences[strchr(precedences, line[i]) - precedences + 1];
                s_prec = precedences[strchr(precedences, stack[*s_index-1]) - precedences + 1];
                if((strchr(l_assoc, line[i]) != NULL && l_prec <= s_prec) || (strchr(r_assoc, line[i]) != NULL && l_prec < s_prec)){
                    printf("%c", stack_pop(s_index, stack));
                }
                break;
            }
            stack_push(s_index, stack, line[i]);
        }
    }
    while(*s_index){
        printf("%c", stack_pop(s_index, stack));
    }
    printf("\n");
    free(stack);
    free(s_index);
    free(line);

    stack = NULL;
    s_index = NULL;
    line = NULL;

}
inline void stack_push(uint64_t *i, char *s, char c){
    assert(*i < MAX_EXP_LEN);
    s[*i] = c;
    *i = *i+1;
}

inline char stack_pop(uint64_t *i, char *s){
    assert(*i >= 0);
    *i = *i-1;
    char c = s[*i];
    s[*i] = '\0';
    return c;
}
