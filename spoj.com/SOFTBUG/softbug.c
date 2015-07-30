// http://www.spoj.com/problems/SOFTBUG/

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <unistd.h>

#define NEEDLE "BUG"
#define NEEDLE_LEN 3

int main(int argc, char *argv[]){
    uint64_t i, s_len, read, len = 0;
    char needle[] = {NEEDLE};
    char *line = NULL, *pos = NULL;

    while((read = getline(&line, &len, stdin)) != EOF){
        while((pos = strstr(line, needle)) != NULL){
            int l =  strlen(pos + 3);
            memmove(pos, pos + 3, l);
            pos[l] = '\0';
        }
            printf("%s", line);
    }

    return EXIT_SUCCESS;
}
