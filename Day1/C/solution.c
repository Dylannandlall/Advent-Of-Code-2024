#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    FILE *file; 
    char *buffer;
    long size;
    char *line;
    char *lineEnd;
    char *tempstr;
    int left;
    int right;
    int *left_arr;
    int *right_arr;

    file = fopen("input.txt", "r");
    if (file == NULL) {
        fprintf(stderr, "Error opening file");
        return 1;
    }

    fseek(file, 0L, SEEK_END);
    size = ftell(file);
    rewind(file);

    buffer = (char *)malloc((size_t)size + 1);
    if (buffer == NULL) {
        fprintf(stderr, "Could not allocate buffer");
        fclose(file);
        return 1;
    }

    fread(buffer, size, 1, file);
    buffer[size] = '\0';

    line = buffer;

    while (*line != '\0') {
        lineEnd = strchr(line, '\n');

        if (lineEnd == NULL) {
            break; 
        }
        
        tempstr = strdup(line);
        left = atoi(strtok(tempstr, " "));
        right = atoi(strtok(NULL, " "));
        printf("Left: %d\tRight: %d\n", left, right);

        line = lineEnd + 1; 
    }

    // while(line != NULL) {
    //     left = atoi(strtok(line, " "));
    //     right = atoi(strtok(NULL, " "));

    //     fprintf(stdout, "Left: %d\tRight: %d\n", left, right);
    //     line = strtok(buffer, " ");
    // }
}