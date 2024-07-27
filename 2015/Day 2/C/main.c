#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "fileio.h"

typedef struct box {
    int length;
    int width;
    int height;
} box;

int main(void) { 
    char *filecon = (char*)malloc(MAX_DATA_SIZE*sizeof(char));
    if (filecon == NULL) {
        perror("Error allocating memory");
        return 1;
    }
    int status = open_file("input.txt", filecon);
    if (status != 0) {
        return status;
    }
    printf("%s",filecon);
    free(filecon);
    return 0;    
}
