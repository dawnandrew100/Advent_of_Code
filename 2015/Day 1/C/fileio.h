#ifndef FILEIO_H
#define FILEIO_H

#define MAX_DATA_SIZE 10000
#define buffer_size 100

int file_read(FILE* fileptr, char *contents){
    char data[MAX_DATA_SIZE]; 
    char buffer[buffer_size];
    char x[buffer_size];
    int rc;
    int pos;

    // read data in 100 character chunks
    while (fgets(buffer, sizeof(buffer), fileptr) != NULL) {
        if ((rc = sscanf (buffer, "%s %n", &x, &pos)) != 1) {
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
#endif
