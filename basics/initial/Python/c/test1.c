#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define N 10000

int main(void) {
    char **p;
    p=(char **)calloc(1,sizeof(char *));
    p[0]=(char *)calloc(7,sizeof(char));
    strcpy(p[0],"Aaryan");
    printf("%s\n",p[0]);
    free(p);
    return 0;

}