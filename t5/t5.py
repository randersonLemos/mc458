import numpy as np

def check_range_coverage(V, Keys, Groups):
    I = []
    INITIALIZED = 0
    PIVO = 0
    LEFT = PIVO
    RIGHT = -1
    
    while True:
        if not Keys:
            break

        key = Keys.pop()
        left, right = key, Groups[key]
        if left <= PIVO:
            INITIALIZED = 1
            if RIGHT < right:
                LEFT  = left
                RIGHT = right
            elif RIGHT == right and left < LEFT:
                LEFT  = left
                RIGHT = right

            #print(left, right)
            #print(LEFT, RIGHT)
            #print('---')
        else:
            if INITIALIZED:
                INITIALIZED = 0

                I.append( (LEFT, RIGHT) )

                #print('***', I, '***')

                if LEFT <= V and V <= RIGHT:
                    return I, len(I)

                PIVO = RIGHT
                LEFT = PIVO
                RIGHT = -1

                Keys.append(key)
            else:
                return [], 0

    if INITIALIZED:
        I.append( (LEFT, RIGHT) )
        if LEFT <= V and V <= RIGHT:
            return I, len(I)

    return [], 0
                                        

if __name__ == '__main__':
    #import argparse
    #parser = argparse.ArgumentParser()
    #parser.add_argument('--file', required=True, type=argparse.FileType('r'))
    #args = parser.parse_args()
    #V = int( args.file.readline().strip() )
    #n = int( args.file.readline().strip() )

    #Groups = {}
    #for i in range(n):
    #    l, r =  list( map( int, args.file.readline().strip().split(' ') ) )
    #    if (l <= 0 and r > 0) or (l >= 0):
    #        if l in Groups:
    #            if Groups[l] < r:
    #                Groups[l] = r
    #        else:
    #            Groups[l] = r


    V = int( input().strip() )
    n = int( input().strip() )

    Groups = {}
    for i in range(n):
        l, r =  list( map( int, input().strip().split(' ') ) )
        if (l <= 0 and r > 0) or (l >= 0):
            if l in Groups:
                if Groups[l] < r:
                    Groups[l] = r
            else:
                Groups[l] = r


    Keys = sorted(Groups.keys(), reverse=True)


    #print('>>>')
    #print('V     ', [0,V])
    #print('Keys  ', Keys)
    #print('Groups', Groups)
    #print('---')
    #for key in reversed(Keys):
    #    print(key, Groups[key])
    #print('---')


    I, n = check_range_coverage(V, Keys, Groups)
    

    #print('---')
    print(n)
    if I:
        print( '\n'.join( ['{} {}'.format(l,r) for l, r in I] ) )
