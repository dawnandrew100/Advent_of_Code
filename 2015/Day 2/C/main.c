#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "fileio.h"

struct box {
    int length;
    int width;
    int height;
};

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
    int n = 0;
    char *token_array[1000];
    struct box present_array[1000];
    char *token = strtok(filecon, "\n");
   while(token != NULL) {
       token_array[n] = token;
       n++;
       token = strtok(NULL, "\n");
       }
    n=0;
    int i = 1;
    int m;
    for (m=0;m<sizeof(token_array);m++){
        char *subtoken = strtok(token_array[n], "x");
        while (subtoken != NULL) {
            switch (i) {
                case 1:
                    present_array[n].length = atoi(subtoken);
                    i++;
                    break;
                case 2:
                    present_array[n].width = atoi(subtoken);
                    i++;
                    break;
                case 3:
                    present_array[n].height = atoi(subtoken);
                    i = 1;
                    n++;
                    break;
            }
            subtoken = strtok(NULL, "x");
        }
    }
    free(filecon);
    printf("%d*%d*%d\n", present_array[0].length,present_array[0].width,present_array[0].height);
    printf("%d*%d*%d\n", present_array[1].length,present_array[1].width,present_array[1].height);
    printf("%d*%d*%d\n", present_array[2].length,present_array[2].width,present_array[2].height);
    printf("%d*%d*%d\n", present_array[3].length,present_array[3].width,present_array[3].height);
    return 0;    
}
