#include <stdio.h>
#include <stdlib.h>
#define N 1000

int main(int argc, char *argv[]) {
    FILE* fp;
    char str[N];
    int i=0;
    fp=fopen(argv[1],"r");
    while (fgets(str,N,fp)!=NULL) {
        i+=1;
    }
    printf("%d\n",i);
    return 0;
}