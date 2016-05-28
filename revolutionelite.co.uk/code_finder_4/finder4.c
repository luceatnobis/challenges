#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>

// &

void knight(int64_t, int64_t, int64_t);

char c[4] = {0};
int64_t star[][2] = {
    // y, x
    {-2, -1}, {-2, 1},
    {-1, 2}, {1, 2},
    {2, 1}, {2, -1},
    {-1, -2}, {1, -2}
};

uint64_t Y, X, res_counter = 0;
uint8_t **grid;

int main(int argc, char *argv[]){

    FILE *f;
    char *line = NULL;

    uint64_t *len, llen = 0, lines = 0;
    int64_t i = 0, j = 0, x = 0, y = 0, read = 0;

    if(argc == 2){  // we are reading from file
        if(access(argv[1], R_OK)){
            fprintf(stderr, "Could not access file %s\n", argv[1]);
            return EXIT_FAILURE;
        }
    } else {
        fprintf(stderr, "Usage: %s <file>\n", argv[0]);
        return EXIT_FAILURE;
    }

    len = malloc(sizeof(uint64_t));
    *len = 0;

    f = fopen(argv[1], "r");

    while(!feof(f)){
      if(fgetc(f) == '\n')
        lines++;
    }
    fseek(f, 0, SEEK_SET);

    grid = calloc(sizeof(uint8_t*), lines);
    
    while((read=getline(&line, len, f)) != -1){
        if(!llen)
            llen = read - 1;
        if(llen != read - 1){
            fprintf(stderr, "Mismatching line lengths; exiting\n");
            return EXIT_FAILURE;
        }
        grid[i] = malloc(sizeof(int8_t) * (read - 1));
        for(j = 0; j < (read - 1); j++){
            grid[i][j] = line[j];
        }
        i++;
    }

    fclose(f);
    Y = lines, X = llen;

    for(y = 0; y < Y; y++){
        for(x = 0; x < X; x++){
            knight(y, x, 3L);
        }
    }
    printf("%li\n", res_counter);
    for(i = 0; i < Y; i++){
        free(grid[i]);
    }
    free(grid);
    free(line);
    free(len);
    return EXIT_SUCCESS;
}

void knight(int64_t y, int64_t x, int64_t n){
    c[3 - n] = grid[y][x];
    grid[y][x] = 0xFF;
    if(n == 0){
        if(strcmp("1234", c) == 0)
            res_counter += 1;
    } else {
        int64_t s, x2, y2;
        for(s = 0; s < 8; s++){
            y2 = (y + Y + star[s][0]) % Y;
            x2 = (x + X + star[s][1]) % X;
            if(grid[y2][x2] == 0xFF)
                continue;
            knight(y2, x2, n - 1);
        }
    }
    grid[y][x] = c[3 - n];
}
