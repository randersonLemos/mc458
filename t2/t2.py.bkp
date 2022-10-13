def swap(X, i, j):
    keep = X[i]
    X[i] = X[j]
    X[j] = keep




if __name__ == '__main__':
    #import argparse
    #import time
    #parser = argparse.ArgumentParser()
    #parser.add_argument('--file', type=argparse.FileType('r'))
    #args = parser.parse_args()
    #n = int( args.file.readline().strip() )
    #X = list( map(int, args.file.readline().strip().split(' ') ) )

    n = int( input().strip() )
    X = list( map(int, input().strip().split(' ')) )

    count = 0
    IMIN  = 0
    IMAX  = n - 1

    #print('n:',n)

    #t = time.time()
    while True:
        for i in range(IMIN, IMAX):
            j = i + 1
            if X[i] > X[j]:
                keep = X[i]
                X[i] = X[j]
                X[j] = keep
                count += 1

        if (IMIN + 1) == X[IMIN]:
            IMIN += 1

        if (IMAX + 1) == X[IMAX]:
            IMAX -= 1

        if IMIN > IMAX:
            break

    #print('Time {:3.6f}'.format(time.time() - t))
    #print('n^2', n*n)
    print(count)



