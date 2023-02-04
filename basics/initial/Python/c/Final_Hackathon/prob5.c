/*
15th March, 2022
Problem 5

Roll Number:CO21BTECH11001
Name: Aaryan

 */
#include <stdio.h>
#include <stdlib.h>

/*This function returns the maximum of two integers p and q*/
int max(int p,int q) {
    return p>q ? p:q;
}

/*This function returns the maximum sum of all values in the cells
along different paths from leftmost bottommost to rightmost upmost cell
of a matrix a of size nxn.
The paths are such that you can go either right, or up, from
your current location. */
int max_score(int *a,int n) {
    int i,j;
    for (i=n-2;i>=0;i=i-1) a[n*i]+=a[n*(i+1)];
    
    for (i=1;i<n;i++) a[n*(n-1)+i]+=a[n*(n-1)+i-1];

    for (i=n-2;i>=0;i=i-1) {
        for (j=1;j<=n-1;j++) 
        a[n*i+j]+=max(a[n*(i+1)+j],a[n*i+j-1]);
    }
    return a[n-1];
}

int main(void) {
    int n,i;
    scanf("%d",&n);
    int *M;
    M= (int *)calloc(n*n,sizeof(int));

    for (i=0;i<n*n;i++) scanf("%d",&M[i]);
    
    printf("%d\n",max_score(M,n));
    free(M);
    return 0;
}