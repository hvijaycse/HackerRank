# import operator as op
# from functools import reduce

# def nc2(n):
#     r = min(2, n-2)
#     numer = reduce(op.mul, range(n, n-r, -1), 1)
#     denom = reduce(op.mul, range(1, r+1), 1)
#     return numer // denom

def Bit( num ):
    max_bit = max( num )
    min_bit = min( num )
    value = max_bit * 11 + min_bit*7
    value = value % 100
    if value < 10:
        return 0
    else:
        return int( str( value)[0])

def main():
    N = int( input() )
    data = input().split()
    Number = [ [ int(j) for j in i] for i in data ]
    odd = {}
    even = {}
    for i in range( N):
        value = Bit( Number[i] )
        if i % 2:
            if value in odd:
                odd[value] += 1
            else:
                odd[value] = 1
        else:
            if value in even:
                even[value] += 1
            else:
                even[value] = 1
    Count = 0
    for elm in odd.values():
        if elm == 2:
            Count += 1
        elif elm > 2:
            Count += 2
    for elm in even.values():
        if elm == 2:
            Count += 1
        elif elm > 2:
            Count += 2
    print( Count)


if __name__ == "__main__":
    main()
    exit(0)