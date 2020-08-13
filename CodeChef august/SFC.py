import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom


def Int():
    return int(input())


def List():
    return input().split()


def Ilist():
    return list(map(int, input().split()))


def yes():
    print('YES')


def no():
    print('NO')


def main():
    TestCase = Int()
    Div = 10 ** 9 + 7
    for _ in range(TestCase):
        N = Int()
        Data = Ilist()
        Counts = [0 for _ in range(N + 1)]
        CD = {}
        for num in Data:
            if num in CD:
                CD[num] += 1
            else:
                CD[num] = 1
        Numbers = list( CD.keys())
        Numbers.sort()
        I = 0
        while I < len(Numbers):
            num = Numbers[I]
            Back = I - 1
            Front = I + 1
            K2 = CD[num]
            Counts[num] += 2 ** (K2) - 1
            IS = Counts[num]
            while Back > -1:
                K1 = CD[Numbers[Back]]
                Back -= 1
                if K1 < K2:
                    till = min(K1, K2 - 1)
                else:
                    till = K2
                TIS = IS
                for K in range(1, till + 1):
                    TIS -= ncr(K2, K)
                    Counts[num] += ncr(K1, K) * TIS
            while Front < len(Numbers):
                K1 = CD[Numbers[Front]]
                Front += 1
                till = min(K1, K2)
                TIS = IS
                for K in range(1, till + 1):
                    K1CK = ncr( K1, K)
                    Counts[num] += TIS * K1CK
                    TIS -= K1CK
            I += 1
        for C in Counts[1:]:
            print( int(C) % Div , end= ' ')
        print()
        


if __name__ == "__main__":
    main()
    exit(0)
