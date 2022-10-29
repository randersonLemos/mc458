import numpy as np


convert = {}
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
    def __init__(self, d, k):
        self.d = d
        self.k = k

        self.B = np.zeros(d)
        self.C = np.zeros(k)


    def sort(self, arr):
        self.C = self.C * 0

        for j in range(self.d):
            self.C[ convert[arr[j]] ] = self.C[ convert[arr[j]] ] + 1




if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True, type=argparse.FileType('r'))
    args = parser.parse_args()
    n = int( args.file.readline().strip() )
    X = list( map(list, args.file.read().strip('\n').replace(' ', '').split('\n') ) )
    M = np.array(X)
    
    d, _ = M.shape
    k = 16

    cs = CountSort(d=d, k=k)
    cs.sort(M[:,-1])

    #n = int( input().strip() )
    #X = list( map(int, input().strip().split(' ')) )
