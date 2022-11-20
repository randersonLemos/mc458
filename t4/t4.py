import numpy as np

def print_matrix(m):
    row, col = m.shape
    shell = np.zeros((row+1, col+1))

    shell[1:,1:] = m

    for r in range(row):
        shell[r+1,0] = r

    for c in range(col):
        shell[0,c+1] = c

    print('\n'.join(['{}'.format(['{:5.0f}'.format(el) for el in row]).strip(']').strip('[') for row in shell]).replace("'", '').replace(',', ''))


def PD(n, notas, V, U):
    r = np.empty((n+1, V+1)).astype(float)
    r[0, :] = np.inf
    r[:, 0] = 0

    #print(notas, V)
    #print_matrix(r)
    #print('======')

    for v in range(1, V+1):
        for i in range(1, n+1):
            nota = notas[i-1]
            if nota > v:
                r[i, v] = r[i-1,v]
            else:
                #div = v//nota
                #aux = r[i-1,v] 
                #for d in range(1,div+1):
                #    if aux > r[i-1, v - nota*d] + d:
                #        aux = r[i-1, v - nota*d] + d
                #r[i,v] = aux
                r[i,v] = min(r[i-1,v], r[i, v-nota] + 1, r[i-1,v-nota] + 1)
            
            if v >= U and i == n and r[i,v] != np.inf:
                return v, int(r[i,v])


        #print_matrix(r[:,:v+1])
        #print('======')



if __name__ == '__main__':
    #import argparse
    #parser = argparse.ArgumentParser()
    #parser.add_argument('--file', required=True, type=argparse.FileType('r'))
    #args = parser.parse_args()
    #U = int( args.file.readline().strip() )
    #n = int( args.file.readline().strip() )
    #notas = list( map( int, args.file.readline().strip().split(' ') ) )

    U = int( input().strip() )
    n = int( input().strip() )
    notas = list( map(int, input().strip('\n').split(' ')) )

    #aux = np.inf
    #print('-'.join( map(str,notas) ) , '|' ,V) 
    #for nota in notas:
    #    mod = V%nota
    #    print(mod)


    V = U + max(notas)
    V, n = PD(n, notas, V, U)

    print(V,n)

