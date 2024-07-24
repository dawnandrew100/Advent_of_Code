#include "fileio.h"

int main(void) { 
    char *contents = open_file("input.txt");
    if (contents == NULL){
        return 1;
    }
    int floor_ans = final_floor(contents);
    int basement_ans = basement(contents);
    printf("Final floor: %d\nFirst basement position: %d", floor_ans, basement_ans);
    return 0; 
}
