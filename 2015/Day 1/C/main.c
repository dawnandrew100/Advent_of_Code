#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_DATA_SIZE 10000

char *file_read(FILE* fileptr);
int final_floor(char *filecon);
int basement(char *filecon);

int main(void) { 
    FILE *fptr = fopen("input.txt", "r"); 
    char *contents = file_read(fptr);

    int floor_ans = final_floor(contents);
    int basement_ans = basement(contents);
    printf("Final floor: %d\nBasement: %d", floor_ans, basement_ans);
    return 0; 
}

char *file_read(FILE* fileptr){
    char *filecon;
    char data[MAX_DATA_SIZE] = ""; 
    char buffer[100]; 

    // read data in 100 character chunks
    while (fgets(buffer, sizeof(buffer), fileptr)) { 
        strncat(data, buffer, strlen(buffer));
    } 
    filecon = data;
    return filecon;
}

int final_floor(char *filecon) {
    int i;
    int floor_num = 0;
    for(i=0; i<strlen(filecon); i++) {
        if (filecon[i] == '(') {
            floor_num++;
        } else if (filecon[i] == ')') {
            floor_num--;
        }
    }
    return floor_num;
}

int basement(char *filecon) {
    int i;
    int floor_num = 0;
    for(i=0; i<strlen(filecon); i++) {
        if (filecon[i] == '(') {
            floor_num++;
        } else if (filecon[i] == ')') {
            floor_num--;
        }
        if (floor_num == -1) {
            return i+1;
        }
    }
    return -1;
}
