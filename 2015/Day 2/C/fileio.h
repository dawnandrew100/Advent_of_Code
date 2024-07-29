#ifndef FILEIO_H
#define FILEIO_H

#define MAX_DATA_SIZE 10000

int file_read(FILE* fileptr, char *contents);
int open_file(char *file_name, char *contents);
int min(int *int_array, int array_size);
int second_smallest(int *int_array, int array_size);


int file_read(FILE* fileptr, char *contents){
    char data[MAX_DATA_SIZE]; 
    char buffer[10];
    char x[10];
    int rc;
    int pos;
    
    // read data in 100 character chunks
    while (fgets(buffer, sizeof(buffer), fileptr) != NULL) {
        if ((rc = sscanf (buffer, "%10s %n", &x, &pos)) != 1) {
            perror("EOF or format error");
            return 1;
        } else if (buffer[pos] != '\0') {
            perror("Traling non-whitespace character");
            return 1;
        } else {
            strncat(data, buffer, strlen(buffer));
        }  
    } 
    strncpy(contents, data, MAX_DATA_SIZE);
    return 0;
}

int open_file(char *file_name, char *contents){
    FILE *fptr = fopen(file_name, "r");
    if (fptr) {
        int success = file_read(fptr, contents);
        
        if (fclose(fptr) == EOF) {
            perror("Error closing file");
            success = 1;
        }
        return success;
    }
    perror("Error opening file");
    return 1;
}

int min(int *int_array, int array_size) {
    if (array_size == 1) {
        return int_array[0];
    }
    if (array_size == 2) {
        int min = int_array[0];
        if (int_array[1] < int_array[0]) {
            min = int_array[1];
        }
        return min;
    }
    int i;
    int min = int_array[0];
    for (i=1;i<array_size;i++) {
        if (int_array[i] < min) {
            min = int_array[i];
        }
    }
    return min;
}

int second_smallest(int *int_array, int array_size) {
    array_size = array_size/sizeof(int);
    if (array_size == 1) {
        return int_array[0];
    }
    if (array_size == 2) {
        int min2 = int_array[0];
        if (int_array[1] > int_array[0]) {
            min2 = int_array[1];
        }
        return min2;
    }
    int i;
    int min = int_array[0];
    int min2 = int_array[1];
    for (i=1;i<array_size;i++) {
        if (int_array[i] < min) {
            min2 = min;
            min = int_array[i];
        } else if (int_array[i] >= min && int_array[i] <= min2) {
            min2 = int_array[i];
        }
    }
    return min2;
}
#endif
