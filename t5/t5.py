import numpy as np

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True, type=argparse.FileType('r'))
    args = parser.parse_args()
    V = int( args.file.readline().strip() )
    n = int( args.file.readline().strip() )
    I = []
    for i in range(n):
        I.append( args.file.readline().strip().split(' ') )

    import IPython; IPython.embed()
    #aux = np.inf
    #print('-'.join( map(str,notas) ) , '|' ,V) 
    #for nota in notas:
    #    mod = V%nota
    #    print(mod)


    V = U + max(notas)
    V, n = PD(n, notas, V, U)

    print(V,n)

