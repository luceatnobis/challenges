// http://www.spoj.com/problems/VOWELS/

#include <stdio.h>
#include <stdint.h>

#define N_VOWELS 6

int main(int argc, char *argv[]){

    char *line = NULL; 
    char vowels[] = {'a', 'e', 'i', 'o', 'u', 'y'};
    uint64_t i, j, read;
    uint64_t len = 10000, vowel_count = 0;

    read = getline(&line, &len, stdin);
    if(line[read-1] == '\n')
        line[read-1] = '\0';

    for(i = 0; line[i]; i++){
        if(isupper(line[i]))
            line[i] += 0x20;    // make it lowercase
        for(j = 0; j < N_VOWELS; j++){
            if(line[i] == vowels[j]){
                vowel_count += 1;
                break;
            }
        }
    }
    free(line);
    printf("%lu\n", vowel_count);
    return 0;
}
