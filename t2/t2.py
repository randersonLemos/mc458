import math

inv = 0

def intercala(A, p, q, r):
    B = []
    n = r - p + 1
    for i in range(p, q+1):
        B.append(A[i])
    for j in reversed(range(q+1,r+1)):
        B.append(A[j])

    i = 0
    j = n - 1
    for k in range(p,r+1):
        if B[i] <= B[j]:
            A[k] = B[i]
            i = i + 1
        else:

            A[k] = B[j]
            j = j - 1


def intercala2(A, p, q, r):
    global inv
    B = []
    n = r - p + 1
    for i in range(p, r+1):
        B.append(A[i])

    i = 0
    j = q - p + 1
    n = r - p + 1
    B.append(math.inf)
    for k in range(p,r+1):
        if B[i] <= B[j] and i < (q - p + 1):
            inv += abs((k-p) - i)
            A[k] = B[i]
            i = i + 1
        else:
            A[k] = B[j]
            j = j + 1


def mergesort(A, p, r):
    if p < r:
        q = int( (p+r)/2 )
        mergesort(A, p  , q)
        mergesort(A, q+1, r)
        intercala2(A, p, q, r)


if __name__ == '__main__':
    #import argparse
    #parser = argparse.ArgumentParser()
    #parser.add_argument('--file', type=argparse.FileType('r'))
    #args = parser.parse_args()
    #n = int( args.file.readline().strip() )
    #X = list( map(int, args.file.readline().strip().split(' ') ) )

    n = int( input().strip() )
    X = list( map(int, input().strip().split(' ')) )

    count = 0
    p = 0
    r = n - 1

    mergesort(X, p, r)

    print(inv)
