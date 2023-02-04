#include <bits/stdc++.h>
#include <vector>
#include <iostream>
using namespace std;

int f(int n) {
    int i;
    int out=1;
    for (i=1;i<=n;i++) out=out*i;
    return out;
}
vector<string> permute(char **s,int n) {
    int m=f(n);
    vector <string> v(n*m*n,"a");
    v[0]=s[1];
    int i,j,c,k,l,temp;
    for (i=0;i<n;i++) {
        if (i==0) v[0]=s[1];
        else {
            j=0;
            temp=f(i+1);
            while (j<temp) {
                for (k=0;k<i+1;k++) {
                    c=(int)(j/(i+1));
                    for (l=0;l<i+1;l++) {
                        if (l<k) v[n*m*i+n*j+l]=v[n*m*(i-1)+n*c+l];
                        else if (l==k) v[n*m*i+n*j+l]=s[i+1];
                        else if (l>k) v[n*m*i+n*j+l]=v[n*m*(i-1)+n*c+l-1];
                    }
                    j+=1;
                }
            }
        }
    }
    return v;
}

int main(int argc,char *argv[]) {
    int n=argc-1;
    vector <string> out;
    out=permute(argv,n);
    int m=f(n);
    for (int i=0;i<m;i++) {
        for (int j=0;j<n;j++) cout<<out[n*m*(n-1)+n*i+j]<<" ";
        cout<<endl;
    }
    return 0;
}