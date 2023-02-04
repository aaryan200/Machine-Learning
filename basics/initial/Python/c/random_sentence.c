#include <stdio.h>
#include <stdlib.h>
#define N 1000

int main(int argc, char *argv[]) {
    FILE* fp;
    char str[N];
    int n,t,i=0;
    fp=fopen(argv[1],"r");
    printf("How much words's sentence u want:");
    scanf("%d",&n);
    for (i=0;i<n;i++) {
        srand(i);
        t=rand();
        for (int k=0;k<=t;k++) fgets(str,N,fp);
        printf("%s ",str);
    }
    printf("\n");
    return 0;
}