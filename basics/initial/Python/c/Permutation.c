#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#define N 100
int f(int n) {
    if (n==0) return 1;
    else {
        int a= 1,i;
        for (i=1;i<=n;i++) {
            a=a*i;
        }
        return a;
    }
}

int main(int argc, char *argv[]) {
    char **p;
    int i,j,c,k,l,temp;
    int n=argc-1;
    int m=f(n);
    p=(char**)malloc(n*m*n*sizeof(char*));
    for (i=0;i<n*m*n;i++) {
        p[i]=(char *)calloc(N,sizeof(char));
    }
    strcpy(p[0],argv[1]);
    for (i=0;i<n;i++) {
        if (i==0) strcpy(p[0],argv[1]);
        else {
            j=0;
            temp=f(i+1);
            while (j<temp) {
                for (k=0;k<i+1;k++) {
                    c=(int)(j/(i+1));
                    for (l=0;l<i+1;l++) {
                        if (l<k) strcpy(p[n*m*i+n*j+l],p[n*m*(i-1)+n*c+l]);
                        else if (l==k) strcpy(p[n*m*i+n*j+l],argv[i+1]);
                        else if (l>k) strcpy(p[n*m*i+n*j+l],p[n*m*(i-1)+n*c+l-1]);
                    }
                    j+=1;
                }
            }
        }
    }
    for (i=0;i<m;i++) {
        for (j=0;j<n;j++) printf("%s ",p[n*m*(n-1)+n*i+j]);
        printf("\n");
    }
    for (i=0;i<n*m*n;i++) {
        free(p[i]);
    }
    free(p);
    return 0;
}
