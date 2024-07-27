#ifndef FILEIO_H
#define FILEIO_H

#define MAX_DATA_SIZE 10000

int file_read(FILE* fileptr, char *filecon);
int open_file(char *file_name, char *filecon);

int file_read(FILE* fileptr, char *filecon){
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
    strncpy(filecon, data, MAX_DATA_SIZE);
    return 0;
}

int open_file(char *file_name, char *filecon){
    FILE *fptr = fopen(file_name, "r");
    if (fptr) {
        int success = file_read(fptr, filecon);
        
        if (fclose(fptr) == EOF) {
            perror("Error closing file");
            success = 1;
        }
        return success;
    }
    perror("Error opening file");
    return 1;
}
#endif
