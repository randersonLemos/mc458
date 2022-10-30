import numpy as np


convert = {}
convert[' '] = -1
convert['0'] = 0
convert['1'] = 1
convert['2'] = 2
convert['3'] = 3
convert['4'] = 4
convert['5'] = 5
convert['6'] = 6
convert['7'] = 7
convert['8'] = 8
convert['9'] = 9
convert['A'] = 10
convert['B'] = 11
convert['C'] = 12
convert['D'] = 13
convert['E'] = 14
convert['F'] = 15


class CountSort:
    def __init__(self, n, m, k):
        self.n = n
        self.m = m
        self.k = k

        self.C = np.zeros(k).astype('int')


    def sort(self, arr, M):
        B = np.empty( (self.n, self.m ), dtype='<U1' )

        for i in range(self.k):
            self.C[i] = 0

        for j in range(self.n):
            self.C[ convert[arr[j]] ] = self.C[ convert[arr[j]] ] + 1

        for i in range(1, self.k):
            self.C[i] = self.C[i] + self.C[i-1]

        for j in reversed(range(self.n)):
            ori = j
            des = self.C[convert[arr[j]]] - 1

            B[ self.C[convert[arr[j]]] - 1, :] = M[j, :]
            self.C[ convert[arr[j]] ] = self.C[ convert[arr[j]] ] - 1

        return B


if __name__ == '__main__':
    #import argparse
    #parser = argparse.ArgumentParser()
    #parser.add_argument('--file', required=True, type=argparse.FileType('r'))
    #args = parser.parse_args()
    #n = int( args.file.readline().strip() )
    #counter = {}
    #for i  in range(n):
    #    m = args.file.readline().strip('\n')
    #    if m in counter:
    #        counter[m] += 1
    #        continue
    #    counter[m] = 1


    n = int( input().strip() )
    counter = {}
    for i in range(n):
        m = input().strip('\n')
        if m in counter:
            counter[m] += 1
            continue
        counter[m] = 1


    n = len(counter)
    M = np.empty((n, 31), dtype='<U1')
    fix = {} 
    i = 0
    for key in counter:
        M[i,:] = list(key)
        i += 1

   
    row, col = M.shape
    k = 16
    cs = CountSort(n=row, m=col, k=k)
    for c in reversed(range(col)):
        A = M[:,c]
        M = cs.sort(A, M)


    print(n)
    for r in range(row):
        m = M[r,:]
        key = ''.join(m)
        print(key, counter[key])
