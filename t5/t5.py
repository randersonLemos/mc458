import numpy as np

def check_range_coverage(V, Keys, Groups):
    I = []
    candidate = (0, 0)
    for key in Keys:
        l, r = key, Groups[key]
        print(l,r)

    import IPython; IPython.embed()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True, type=argparse.FileType('r'))
    args = parser.parse_args()
    V = int( args.file.readline().strip() )
    n = int( args.file.readline().strip() )

    Groups = {}
    for i in range(n):
        l, r =  list( map( int, args.file.readline().strip().split(' ') ) )
        if (l < 0 and r > 0) or (l > 0):
            if l in Groups and Groups[l] < r:
                Groups[l] = r
            else:
                Groups[l] = r

    Keys = sorted(Groups.keys())
                

    print('V     ', [0,V])
    print('Keys  ', Keys)
    print('Groups', Groups)

    check_range_coverage(V, Keys, Groups)
