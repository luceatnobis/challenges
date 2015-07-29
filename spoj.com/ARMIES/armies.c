// http://www.spoj.com/problems/ARMIES/
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdint.h>

int comp(int *a, int *b);
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
    getline(&line, &len, input);
    testcase_count = atol(line);

    for(i = 0; i < testcase_count ; i++){
        process_case(input);
    }
    free(line);
    return EXIT_SUCCESS;
}

void process_case(FILE* input){
    char *countries[] = {"Bajtocja", "Megabajtolandia"};
    char *line = NULL, *tokptr = NULL;
    uint64_t i;
    uint64_t b_armies_n, m_armies_n, more_armies, min_armies, read;
    uint64_t len = 0, more_divs = 0xFF;

    uint64_t *b_armies, *m_armies;

    // read in for b...
    getline(&line, &len, input);
    b_armies_n = atol(line);
    b_armies = calloc(b_armies_n, sizeof(uint64_t));

    free(line);
    line = NULL;
    getline(&line, &len, input);

    tokptr = strtok(line, " ");
    b_armies[0] = atol(tokptr);
    for(i = 1; i < b_armies_n; i++){
        tokptr = strtok(NULL, " ");
        b_armies[i] = atol(tokptr);
    }

    // read in for m...
    free(line);
    line = NULL;
    getline(&line, &len, input);
    m_armies_n = atol(line);
    m_armies = calloc(m_armies_n, sizeof(uint64_t));

    free(line);
    line = NULL;
    getline(&line, &len, input);
    tokptr = strtok(line, " ");
    m_armies[0] = atol(tokptr);
    for(i = 1; i < m_armies_n; i++){
        tokptr = strtok(NULL, " ");
        m_armies[i] = atol(tokptr);
    }

    min_armies = b_armies_n > m_armies_n ? b_armies_n : m_armies_n;
    qsort(b_armies, b_armies_n, sizeof(uint64_t), (void*)comp);
    qsort(m_armies, m_armies_n, sizeof(uint64_t), (void*)comp);

    for(i = 0; i < min_armies; i++){
        if(b_armies[i] == m_armies[i])  // armies of equal size meet
            continue;
        printf("%s\n", countries[b_armies[i] < m_armies[i]]);
        goto free;
    }
    // we land here if so far we've encountered only armies of equal strength
    more_armies = b_armies_n > m_armies_n ? 0 : 1;
    if(b_armies_n == m_armies_n){
        printf("Draw\n");
    } else {
        printf("%s\n", countries[more_armies]);
    }

free:
    free(line);
    free(b_armies);
    free(m_armies);
    return;
}

int comp(int *a, int *b){

    return *b - *a;
}
