#include <stdio.h>    
#include <stdlib.h>

void SCM(int *X, int *n, int *i, int *j, int *k, int *MaxSeq, int *MaxSuf) 
{
  if( (*n) == 1)
  {
    if ( X[1] < 0 )
    {
      *i = 0; *j = 0; *k = 0; *MaxSeq = 0; *MaxSuf = 0;
    }
    else
    {
      *i = 1; *j = 1; *k = 1; *MaxSeq = X[1]; *MaxSuf = X[1];
    }
  }
  else
  {
    int _n = (*n) - 1;
    SCM(X, &_n, i, j, k, MaxSeq, MaxSuf);
    if( (*k) == 0)
    {
      *k = *n;
    }
    *MaxSuf = *MaxSuf + X[*n];
    if( (*MaxSuf) > (*MaxSeq) )
    {
      *i = *k; *j = *n; *MaxSeq = *MaxSuf;
    }
    else if( (*MaxSuf) == (*MaxSeq) )
    {
      if( ( (*j) - (*i) ) < ( (*n) - (*k) ) )
      {
        *i = *k; *j = *n; *MaxSeq = *MaxSuf;
      }
    }
    else if( (*MaxSuf) < 0)
    {
      *MaxSuf = 0; *k = 0;
    }
  }
}

int main(){    
  int n = 0; scanf("%d\n", &n); n = n - 1;
  int *X = (int *) malloc(n * sizeof(int) );
  int i, j, k = 0;
  int MaxSeq, MaxSuf = 0;

  for(int i = 1; i < n; ++i)
  {
    int x;
    scanf("%d ", &x);
    X[i] = x;
  }

  //printf("n: %d\n", n);
  //printf("X: ");
  //for(int i = 1; i < n; ++i)
  //{
  //  printf("%d ", X[i]);
  //}
  //printf("\n");
  
  SCM(X, &n, &i, &j, &k, &MaxSeq, &MaxSuf);

  //printf("%d, %d, %d, %d, %d, %d", n, i, j, k, MaxSeq,  MaxSuf);
  
  printf("%d %d", i, j);

  free(X);
}  
