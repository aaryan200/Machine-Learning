/*
16th March, 2022
Problem 4

Roll Number:CO21BTECH11001
Name: Aaryan

 */
#include <stdio.h>
#include <stdlib.h>
#define N 5000

/*It returns the length of the string s.*/
int my_strlen(char *s) {
    int len=0;
    int i;
    for (i=0;s[i]!='\0';i++) len+=1;
    return len;
}

/*It performs the mathematical operation between the operands a and b,
where c is the operator 
and return the result of that operation.*/
int execute(int a,int b,char c) {
    int temp;
    if (c=='+') temp=a+b;
    else if (c=='-') temp= a-b;
    else if (c=='*') temp=a*b;
    return temp;
}

/*It evaluates the postfix expression written in string s
and returns the evaluated value.*/
int cal_postfix(char *s) {
    int i,m,n=0;
    int a[N];
    m=my_strlen(s);
    for (i=0;i<m;i++) {
        if ((int)s[i]>=48 && (int)s[i]<=57) {
            a[n]=(int)s[i]-48;
            n+=1;
        }
        else {
            a[n-2] =execute(a[n-2],a[n-1],s[i]);
            n-=1;
        }
    }
    if (n==1) return a[0];
    else return 0;
}

int main(void) {
    char s[N];
    scanf("%s",s);

    printf("%d\n",cal_postfix(s));

    return 0;
}