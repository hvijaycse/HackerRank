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
    ''' Yaay baby this was a trick question no need of the corrdinates'''
    TestCase = Int()
    for _ in range(TestCase):
        N = Int()
        # X = []
        # Y = []
        for _ in range(N):
            tmpx, tmpy = Ilist()
            # X.append(tmpx)
            # Y.append(tmpy)
        edges = N
        while N > 5:
            edges += N//2
            N = N // 2
        print(edges)


if __name__ == "__main__":
    main()
    exit(0)
