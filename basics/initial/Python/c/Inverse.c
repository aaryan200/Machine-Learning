#include <stdio.h>
#include <stdlib.h>

float *mult_matrix(float *m1, float *m2, int row_out, int common, int col_out) {
  float m3[row_out*col_out];
  float *p;
  for (int i=0;i<row_out;i++) {
    for (int j=0;j<col_out;j++) {
      m3[col_out*i+j] = 0.0;
      for (int k=0;k<common;k++) 
      m3[col_out*i+j] += m1[common*i+k]*m2[col_out*k+j];
    }
  }
  p=m3;
  return p;
}

float *add_col(float *a,int row, int col,int m, int i,int j) {
  for (int k=0;k<row;k++) {
    a[col*k+i] += m*a[col*k+j];
  }
  return a;
}
int main(void) {
  return 0;
}
