/*
15th March, 2022
Problem 2

Roll Number:CO21BTECH11001
Name: Aaryan

 */
#include <stdio.h>
#include <stdlib.h>

/* The function check_right_rot checks if every row,except the first,
of the given matrix a of size nxn is obtained by rotating the 
previous row to right by one.
If yes, it returns 1
If no, it returns 0 */
int check_right_rot(int *a, int n) {
    int i,k,temp,temp1,temp2,x,y,z;
    z = 0;
    for (i = 0; i < n-1;i++) {
        if (i==0) {
            x = a[0];
            temp = 0;
            for (k=1;k<n;k++) {
                if (x==a[n*k+k]) temp += 1;
                else break;
            }
            if (temp == n-1) z+=1;
            else break;
        }
        else if (i >=1) {
            x = a[i];
            temp1 =0;
            for (k=i+1;k<n;k++) {
                if (x==a[n*(k-i)+k]) temp1 +=1;
                else break;
            }
            if (temp1 == n-1-i) z+=1;
            else break;

            y = a[n*i];
            temp2 = 0;
            for (k=i+1;k<n;k++) {
                if (y==a[n*k+k-i]) temp2+=1;
                else break;
            }
            if (temp2 == n-1-i) z+=1;
            else break;
        }
    }
    if (z==2*n-3) return 1;
    else return 0;
}

/* The function check_left_rot checks if every row,except the first,
of the given matrix a of size nxn is obtained by rotating the 
previous row to left by one.
If yes, it returns 1
If no, it returns 0 */
int check_left_rot(int *a, int n) {
    int i,k,temp,temp1,temp2,x,y,z;
    z = 0;
    for (i = n-1; i>0;i = i-1) {
        if (i==n-1) {
            x = a[n-1];
            temp = 0;
            for (k=n-2;k>=0;k=k-1) {
                if (x==a[n*(n-1-k)+k]) temp += 1;
                else break;
            }
            if (temp == n-1) z+=1;
            else break;
        }
        else if (i < n-1) {
            x = a[i];
            temp1 =0;
            for (k=i-1;k>=0;k=k-1) {
                if (x==a[n*(i-k)+k]) temp1 +=1;
                else break;
            }
            if (temp1 == i) z+=1;
            else break;

            y = a[n*i+n-1];
            temp2 = 0;
            for (k=i+1;k<n;k++) {
                if (y==a[n*k+i+n-1-k]) temp2+=1;
                else break;
            }
            if (temp2 == n-1-i) z+=1;
            else break;
        }
    }
    if (z==2*n-3) return 1;
    else return 0;
}

int main(void) {
    int n,i;
    scanf("%d",&n);
    int *a;
    a = (int *)calloc(n*n,sizeof(int));
    for (i=0;i<n*n;i++) scanf("%d",&a[i]);
    if (check_left_rot(a,n)==1) printf("Yes\n");
    else if (check_right_rot(a,n)==1) printf("Yes\n");
    else printf("No\n");
    free(a);
    return 0;
}