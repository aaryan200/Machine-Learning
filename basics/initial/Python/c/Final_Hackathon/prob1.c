/*
15th March, 2022
Problem 1

Roll Number:CO21BTECH11001
Name: Aaryan

 */
#include <stdio.h>
#include <stdlib.h>

/*This function prints outer product of two vectors a ,of size size_a,
 and b, of size size_b. */
int print_outer_product(int *a, int size_a, int *b, int size_b) {
    int i,j,temp;
    for (i = 0; i < size_a; i++) {
        for (j = 0; j < size_b; j++) {
            temp = a[i]*b[j];
            printf("%d ",temp);
        }
        printf("\n");
    }
    return 0;
}

int main(void) {
    int m,n,i;
    scanf("%d %d",&m,&n);
    int *a;
    a=(int *)calloc(m,sizeof(int));

    int *b;
    b=(int *)calloc(n,sizeof(int));

    for (i=0;i<m;i++) scanf("%d",&a[i]);
    
    for (i=0;i<n;i++) scanf("%d",&b[i]);

    print_outer_product(a,m,b,n);

    free(a);
    free(b);
    return 0;
}