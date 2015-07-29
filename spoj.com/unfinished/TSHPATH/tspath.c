// http://www.spoj.com/problems/TSHPATH/

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdint.h>
#include <limits.h>
#include <malloc.h>

#define INF_MARKER 0xDEADBEEFCAFEBABE
#define MAX_CITY_LEN 10
#define ALPHABET_LEN 26

void process_case(FILE* input);
long search(char *needle, char **haystack, uint64_t n);

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
    return EXIT_SUCCESS;

}

void process_case(FILE *input){
    char *line, *tokptr;
    char **cities;
    uint64_t a, b, i, j, k;
    uint64_t *p, *q, *r;
    uint64_t city, conn, cost, n_cities, city_conn_n, read;
    uint64_t len = 0;

    uint64_t **distance;

    getline(&line, &len, input);
    n_cities = atol(line);

    cities = malloc(sizeof(char*) * n_cities);
    distance = malloc(sizeof(uint64_t*) * n_cities);

    for(i = 0; i < n_cities; i++){
        read = getline(&cities[i], &len, input);
        cities[i][read-1] = '\0';

        distance[i] = malloc(sizeof(uint64_t) * n_cities);
        for(j = 0; j < n_cities; j++){
            if(j == i)
                distance[i][j] = 0;
            else
                distance[i][j] = INF_MARKER;
        }

        getline(&line, &len, input);
        city_conn_n = atol(line);

        for(j = 0; j < city_conn_n; j++){
            getline(&line, &len, input);
            tokptr = strtok(line, " ");
            city = atol(tokptr) - 1;

            tokptr = strtok(NULL, " ");
            cost = atol(tokptr);

            distance[i][city] = cost;
        }
    }

    // lets apply floyd warshall (https://www.youtube.com/watch?v=8TRX85-myD4)
    for(k = 0; k < n_cities; k++){
        for(i = 0; i < n_cities; i++){
            if(i == k)
                continue;
            for(j = 0; j < n_cities; j++){
                if(j == k)
                    continue;
                p = &distance[i][j];
                q = &distance[i][k];
                r = &distance[k][j];
                if(*p > *q + *r)   // does a shorter path exist?
                    *p = *q + *r;
            }
        }
    }
    getline(&line, &len, input);
    conn = atol(line);

    for(i = 0; i < conn; i++){
        read = getline(&line, &len, input);
        line[read-1] = '\0';

        tokptr = strtok(line, " ");
        a = search(tokptr, cities, n_cities);
        tokptr = strtok(NULL, " ");
        b = search(tokptr, cities, n_cities);
        printf("%lu\n", distance[a][b]);
    }
    // seperates test cases
    getline(&line, &len, input);
    free(distance[0]);
    free(cities);
    free(distance);
    
}

long search(char *needle, char **haystack, uint64_t n){
    long i;
    for(i = 0; i < n; i++){
        if(strcmp(needle, haystack[i]) == 0)
            return i;
    }
    return -1;
}
