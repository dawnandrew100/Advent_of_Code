#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "fileio.h"
#define input_size 1000

struct box {
    int length;
    int width;
    int height;
};

int wrapping_paper_size(struct box *present_ptr);
int ribbon_size(struct box *present_ptr);

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
    char *token_array[input_size];
    struct box present_array[input_size];
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
    
    int wrapping_paper_sqft = wrapping_paper_size(present_array);
    int ribbon_ft = ribbon_size(present_array);
    printf("Wraping paper needed: %d sqft\nRibbon needed: %d ft\n", wrapping_paper_sqft, ribbon_ft);
    return 0;    
}

int wrapping_paper_size(struct box *present_ptr) {
    int total = 0;
    int i;
    for (i=0;i<input_size;i++) {
        int side1 = 2 * present_ptr[i].length * present_ptr[i].width;
        int side2 = 2 * present_ptr[i].width * present_ptr[i].height;
        int side3 = 2 * present_ptr[i].height * present_ptr[i].length;
        int box_array[3] = {side1, side2, side3};
        int smallest_side = min(box_array, sizeof(box_array));
        total += side1 + side2 + side3 + (smallest_side/2);
    }
    return total;
}

int ribbon_size(struct box *present_ptr) {
    int i;
    int total = 0;
    for (i=0;i<input_size;i++) {
        int perimeter[3] = {present_ptr[i].length, present_ptr[i].width, present_ptr[i].height};
        int ribbon = (2*min(perimeter, sizeof(perimeter)))+(2*second_smallest(perimeter, sizeof(perimeter)));
        int bow = present_ptr[i].length * present_ptr[i].width * present_ptr[i].height;
        total += ribbon + bow;
    }
    return total;
}
