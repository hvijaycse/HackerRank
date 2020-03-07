# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement as cwr

if __name__ == '__main__':
    String, Upto = input().split()
    Upto = int( Upto)
    String = [i for i in String]
    String.sort()
    Ls = cwr(String, Upto)
    print('\n'.join( [''.join(ans) for ans in Ls]  ) )
