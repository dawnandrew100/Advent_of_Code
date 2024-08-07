#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "fileio.h"

int final_floor(char *filecon);
int basement(char *filecon);

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
    int floor_ans = final_floor(filecon);
    int basement_ans = basement(filecon);
    printf("Final floor: %d\nFirst basement position: %d", floor_ans, basement_ans);
    free(filecon);
    return 0; 
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
