def swap(X, i, j):
    keep = X[i]
    X[i] = X[j]
    X[j] = keep


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=argparse.FileType('r'))
    args = parser.parse_args()
    n = int( args.file.readline().strip() )
    X = list( map(int, args.file.readline().strip().split(' ') ) )

    #n = int( input().strip() )
    #X = list( map(int, input().strip().split(' ')) )

    #print(X)

    count = 0
    IMIN = 0
    IMAX = n - 1

    while True:
        for i in range(IMIN, IMAX):
            j = i + 1
            if X[i] > X[j]:
                swap(X,i,j)
                count += 1
                no_swap = False

        if (IMIN + 1) == X[IMIN]:
            IMIN += 1

        if (IMAX + 1) == X[IMAX]:
            IMAX -= 1

        if IMIN > IMAX:
            break


    #print(X)
    print(count)



