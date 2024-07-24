#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_DATA_SIZE 10000

char *file_read(FILE* fileptr){
  char *filecon = (char*)malloc(MAX_DATA_SIZE*sizeof(char));
  char data[MAX_DATA_SIZE]; 
  char buffer[100]; 

  // read data in 100 character chunks
  while (fgets(buffer, sizeof(buffer), fileptr)) { 
      strncat(data, buffer, strlen(buffer));
  } 
  filecon = data;
  return filecon;
}

char *open_file(char *file_name){
  FILE *fptr = fopen(file_name, "r");
  if (fptr == NULL) {
      perror("Error opening file");
      return NULL;
  }
  char *contents = file_read(fptr);
  if (fclose(fptr) == EOF) {
      perror("Error closing file");
      return NULL;
  }
  return contents;
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
