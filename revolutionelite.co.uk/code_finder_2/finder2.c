#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>

// &

int main(int argc, char *argv[]){

    int star[8][4][2] = {
        // y, x
        { {0, 0}, {0, -1}, {0, -2}, {0, -3} },   // left
        { {0, 0}, {0, 1}, {0, 2}, {0, 3} },   // right
        { {0, 0}, {-1, 0}, {-2, 0}, {-3, 0} },   // up
        { {0, 0}, {1, 0}, {2, 0}, {3, 0} },   // down

        { {0, 0}, {-1, -1}, {-2, -2}, {-3, -3} },   // up-left
        { {0, 0}, {-1, 1}, {-2, 2}, {-3, 3} },   // up-right

        { {0, 0}, {1, -1}, {2, -2}, {3, -3} },   // down-left
        { {0, 0}, {1, 1}, {2, 2}, {3, 3} },     // down-right
    };

    FILE *f;
    uint8_t **grid;
    char *line = NULL, c[4] = {0};

    uint64_t *len, *matrix;
    int64_t i = 0, j = 0, s = 0, x = 0, x2 = 0, y2 = 0, y = 0, llen = 0, lines = 0, read = 0;

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
    matrix = calloc(sizeof(uint64_t), 10000);

    for(y = 0; y < lines; y++){
        for(x = 0; x < llen; x++){
            for(s = 0; s < 8; s++){
                for(i = 0; i < 4; i++){
                    y2 = (y + lines + star[s][i][0]) % lines;
                    x2 = (x + llen + star[s][i][1]) % llen;
                    c[i] = grid[y2][x2];

                }
                matrix[atoi(c)]++;
            }
        }
    }
    for(i = 0, j = 1; j < 10000; j++){
        if(matrix[j] > matrix[i])
            i = j;
    }
    printf("%lu:%lu\n", i, matrix[i]);
    free(matrix);
    for(i = 0; i < lines; i++){
        free(grid[i]);
    }
    free(grid);
    free(line);
    free(len);
    return EXIT_SUCCESS;
}

