#include <stdio.h>
#include <stdlib.h>

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
int *permut(int n) {
    
    int m=f(n);
    int a[m*n];
    int *p;
    p=a;
    if (n==1) {
        a[0]=1;
        return p;
    }
    else if (n>=2) {
        int d=f(n-1);
        int i,j,c,k;
        int b[d*(n-1)];
        for (i=0;i<d*(n-1);i++) b[i]=permut(n-1)[i];
        i=0;
        while (i<m) {
            for (j=0;j<n;j++) {
                c=i/n;
                for (k=0;k<n;k++) {
                    if (k<j) a[n*i+k]=b[(n-1)*c+k];
                    if (k==j) a[n*i+k]=n;
                    if (k>j) a[n*i+k]=b[(n-1)*c+k-1];
                }
                i+=1;
            }
        }
        return p;
    }
}

int main(){
    int n,i,j;
    
    printf("Enter a natural number:");
    scanf("%d",&n); 
    int m=f(n);
    int *a;
    a=(int *)calloc(m*n,sizeof(int));
    a=permut(n);
    /*for (i=0;i<m;i++) {
        for (j=0;j<n;j++) a[n*i+j]=permut(n)[n*i+j];
    }*/
    for (i=0;i<m;i++) {
        for (j=0;j<n;j++) {
            printf("%d ",a[n*i+j]);
        }
        printf("\n");
    }
    free(a);
    return 0;
}
