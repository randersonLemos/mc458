import sys
sys.setrecursionlimit(100000)

def SCM(X, n):
    i = 0; j = 0; k = 0
    MaxSuf = 0; MaxSeq = 0

    if n == 1:
        if X[1] < 0: # x_1
            i = 0; j = 0; k = 0; MaxSeq = 0; MaxSuf = 0
        else:
            i = 1; j = 1; k = 1; MaxSeq = X[1]; MaxSuf = X[1]
    else:
        i, j, k, MaxSeq, MaxSuf = SCM(X, n - 1)
        if k == 0 : k = n
        MaxSuf = MaxSuf + X[n]
        if MaxSuf > MaxSeq:
            i = k; j = n; MaxSeq = MaxSuf
        elif MaxSuf == MaxSeq:
            if (j-i) < (n-k):
                i = k; j = n; MaxSeq = MaxSuf
        elif MaxSuf < 0:
            MaxSuf = 0; k = 0
    return i, j, k, MaxSeq, MaxSuf
        

if __name__ == '__main__':
    #import argparse
    #parser = argparse.ArgumentParser()
    #parser.add_argument('--file', type=argparse.FileType('r'))
    #args = parser.parse_args()
    #n = int( args.file.readline().strip() )
    #X = list( map(int, args.file.readline().strip().split(' ') ) )

    n = int( input().strip() )
    X = list( map(int, input().strip().split(' ')) )

    n = n - 1
    X = [0] + X
    
    i, j, k, MaxSeq, MaxSuf = SCM(X, n)

    print(i, j)
