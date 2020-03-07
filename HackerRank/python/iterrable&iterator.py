# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == '__main__':
    n = int( input())
    String = input().split()
    k = int(input())
    Comb = list(combinations( String, k))
    count = 0
    for combi in Comb:
        if 'a' in combi:
            count += 1
    ans = count / len(Comb)
    print("%.4f" % ans)

    
