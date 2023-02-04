/*
17th March, 2022
Problem 3

Roll Number:CO21BTECH11001
Name: Aaryan

 */
#include <stdio.h>
#include <stdlib.h>
#define N 5000

int max(int p,int q) {
    return p>=q ? p:q;
}

int my_strlen(char *s) {
    int len=0;
    int i;
    for (i=0;s[i]!='\0';i++) len+=1;
    return len;
}

char *sum(char *s1,char *s2) {
    int n=my_strlen(s1);
    int m=my_strlen(s2);
    char *p;
    char *q;
    int x;
    char a[1];
    a[0]='0';
    for (int i=0;i<n;i++) {
        if (s1[i]==0) x+=1;
    }
    for (int i=0;i<m;i++) {
        if (s2[i]==0) x+=1;
    }
    if (x==n+m) {
        q=a;
        return q;
    }
    else if (n>=m) {
        char s3[n+1];
        int i,carry=0;
        for (i=m-1;i>=0;i=i-1) {
            s3[m-1-i]=((int)s1[i+n-m]+(int)s2[i]-96+carry)%10+48;
            carry=((int)s1[i+n-m]+(int)s2[i]-96+carry)/10;
        }
        for (i=n-m-1;i>=0;i=i-1) {
            s3[n-1-i]=((int)s1[i]+carry-48)%10+48;
            carry=((int)s1[i]+carry-48)/10;
        }
        s3[n]=carry+48;
        int temp=0;
        while (s3[n-temp]=='0') temp+=1;
        char s6[n+1-temp];
        for (i=temp;i<n+1;i++) s6[i-temp]=s3[n-i];
        p=s6;
    }
    else {
        char s4[m+1];
        int i,carry=0;
        for (i=n-1;i>=0;i=i-1) {
            s4[n-1-i]=((int)s2[i+m-n]+(int)s1[i]-96+carry)%10+48;
            carry=((int)s2[i+m-n]+(int)s1[i]-96+carry)/10;
        }
        for (i=m-n-1;i>=0;i=i-1) {
            s4[m-1-i]=((int)s2[i]-48+carry)%10+48;
            carry=((int)s2[i]-48+carry)/10;
        }
        s4[m]=carry+48;
        int temp=0;
        while (s4[m-temp]=='0') temp+=1;
        char s5[m+1-temp];
        for (i=temp;i<m+1;i++) s5[i-temp]=s4[m-i];
        p=s5;
    }
    return p;
}

char *multiply(char *s1,char *s2) {
    int n=my_strlen(s1);
    int m=my_strlen(s2);
    char *p;
    if (s1[0]!='-' && s2[0]!='-') {
        char s3[(n+m)*m];
        char out[n+m];
        int k,i,j;
        for (i=0;i<n+m;i++) out[i]='0';
        
        for (k=0;k<m;k++) {
            int carry=0;
            for (i=n-1;i>=0;i=i-1) {
                s3[k*(n+m)+m-k+i]=(((int)s1[i]-48)*((int)s2[m-1-k]-48)+carry)%10+48;
                carry=(((int)s1[i]-48)*((int)s2[m-1-k]-48)+carry)/10;
            }
            s3[k*(n+m)+m-k-1]=carry;
            for (j=0;j<m-k-1;j++) s3[k*(n+m)+j]='0';
            for (j=n+m-k;j<n+m;j++) s3[k*(n+m)+j]='0';
            char s4[n+m];
            for (j=0;j<n+m;j++) s4[j]=s3[k*(n+m)+j];
            int temp=my_strlen(sum(out,s4));
            char s5[temp];
            for (j=0;j<temp;j++) s5[j]=sum(out,s4)[j];
            for (j=0;j<temp;j++) out[n+m-temp+j]=s5[j];
        }
        int temp1=0;
        while (out[temp1]==0) temp1+=1;
        char out1[n+m-temp1];
        for (i=0;i<n+m-temp1;i++) out1[i]=out[i+temp1];
        p=out1;
    }
    else if (s1[0]=='-' && s2[0]!='-') {
        char s_alt[n-1];
        for (int i=1;i<n;i++) s_alt[i-1]=s1[i];
        char s3[(n-1+m)*m];
        char out[n-1+m];
        int k,i,j;
        for (i=0;i<n-1+m;i++) out[i]='0';
        
        for (k=0;k<m;k++) {
            int carry=0;
            for (i=n-2;i>=0;i=i-1) {
                s3[k*(n-1+m)+m-k+i]=(((int)s_alt[i]-48)*((int)s2[m-1-k]-48)+carry)%10+48;
                carry=(((int)s_alt[i]-48)*((int)s2[m-1-k]-48)+carry)/10;
            }
            s3[k*(n-1+m)+m-k-1]=carry;
            for (j=0;j<m-k-1;j++) s3[k*(n-1+m)+j]='0';
            for (j=n+m-k-1;j<n+m-1;j++) s3[k*(n-1+m)+j]='0';
            char s4[n+m-1];
            for (j=0;j<n+m-1;j++) s4[j]=s3[k*(n-1+m)+j];
            int temp=my_strlen(sum(out,s4));
            char s5[temp];
            for (j=0;j<temp;j++) s5[j]=sum(out,s4)[j];
            for (j=0;j<temp;j++) out[n+m-1-temp+j]=s5[j];
        }
        int temp1=0;
        while (out[temp1]==0) temp1+=1;
        char out1[n+m-temp1];
        out1[0]='-';
        for (i=1;i<n+m-temp1;i++) out1[i]=out[i+temp1];
        p=out1;
    }
    else if (s1[0]!='-' && s2[0]=='-') {
        char s_alt[m-1];
        for (int i=1;i<m;i++) s_alt[i-1]=s2[i];
        char s3[(n-1+m)*(m-1)];
        char out[n-1+m];
        int k,i,j;
        for (i=0;i<n-1+m;i++) out[i]='0';
        
        for (k=0;k<m-1;k++) {
            int carry=0;
            for (i=n-1;i>=0;i=i-1) {
                s3[k*(n-1+m)+m-1-k+i]=(((int)s1[i]-48)*((int)s_alt[m-2-k]-48)+carry)%10+48;
                carry=(((int)s1[i]-48)*((int)s_alt[m-1-k]-48)+carry)/10;
            }
            s3[k*(n-1+m)+m-1-k-1]=carry;
            for (j=0;j<m-1-k-1;j++) s3[k*(n-1+m)+j]='0';
            for (j=n+m-k-1;j<n+m-1;j++) s3[k*(n-1+m)+j]='0';
            char s4[n+m-1];
            for (j=0;j<n+m-1;j++) s4[j]=s3[k*(n-1+m)+j];
            int temp=my_strlen(sum(out,s4));
            char s5[temp];
            for (j=0;j<temp;j++) s5[j]=sum(out,s4)[j];
            for (j=0;j<temp;j++) out[n+m-1-temp+j]=s5[j];
        }
        int temp1=0;
        while (out[temp1]==0) temp1+=1;
        char out1[n+m-temp1];
        out1[0]='-';
        for (i=1;i<n+m-temp1;i++) out1[i]=out[i+temp1];
        p=out1;
    }
    else if (s1[0]=='-' && s2[0]=='-') {
        char s_alt1[n-1];
        for (int i=1;i<n;i++) s_alt1[i-1]=s1[i];
        char s_alt2[m-1];
        for (int i=1;i<m;i++) s_alt2[i-1]=s2[i];
        char s3[(n-1+m-1)*(m-1)];
        char out[n-1+m-1];
        int k,i,j;
        for (i=0;i<n-1+m-1;i++) out[i]='0';
        
        for (k=0;k<m-1;k++) {
            int carry=0;
            for (i=n-2;i>=0;i=i-1) {
                s3[k*(n-1+m-1)+m-1-k+i]=(((int)s_alt1[i]-48)*((int)s_alt2[m-2-k]-48)+carry)%10+48;
                carry=(((int)s_alt1[i]-48)*((int)s_alt2[m-2-k]-48)+carry)/10;
            }
            s3[k*(n-1+m-1)+m-1-k-1]=carry;
            for (j=0;j<m-1-k-1;j++) s3[k*(n-1+m-1)+j]='0';
            for (j=n+m-1-k-1;j<n+m-1;j++) s3[k*(n-1-1+m)+j]='0';
            char s4[n+m-1-1];
            for (j=0;j<n+m-1-1;j++) s4[j]=s3[k*(n-1+m-1)+j];
            int temp=my_strlen(sum(out,s4));
            char s5[temp];
            for (j=0;j<temp;j++) s5[j]=sum(out,s4)[j];
            for (j=0;j<temp;j++) out[n+m-2-temp+j]=s5[j];
        }
        int temp1=0;
        while (out[temp1]==0) temp1+=1;
        char out1[n+m-temp1-2];
        for (i=0;i<n+m-temp1-2;i++) out1[i]=out[i+temp1];
        p=out1;
    }
    return p;
}
int main(void) {
    char s1[N];
    char s2[N];
    scanf("%s %s",s1,s2);
    int n=my_strlen(multiply(s1,s2));
    for (int i=0;i<n;i++){
        printf("%c",multiply(s1,s2)[i]);
    }
    printf("\n");
    
    return 0;
}