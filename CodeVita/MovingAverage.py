def Int():
    return int(input())


def List():
    return input().split()


def Ilist():
    return list(map(int, input().split()))


def Flist():
    return list(map(float, input().split()))


def yes():
    print('YES')


def no():
    print('NO')


def getCondition(av1, av2):
    if av1 < av2:
        return 2
    else:
        return 3


def main():
    Changes = 0
    X, Y = Ilist()
    N = Int()
    Points = Flist()
    Faster = min(X, Y)
    Slower = max(X, Y)
    Fast_array = [ round( Point / float( Faster), 6) for Point in Points ]
    Slower_array = [ round( Point / float( Slower), 6) for Point in Points ]
    F_av = sum( Fast_array[ Slower - Faster: Slower])
    S_av = sum( Slower_array[: Slower])
    Initial_condition = getCondition(F_av, S_av)
    for index in range( Slower, N):
        F_av -= Fast_array[ index - Faster]
        S_av -= Slower_array[ index - Slower]
        F_av += Fast_array [index]
        S_av += Slower_array[index]
        # print(F_av, S_av)
        if Initial_condition != getCondition(F_av, S_av):
            Changes += 1
            Initial_condition = getCondition(F_av, S_av)
    print(Changes)


if __name__ == "__main__":
    main()
    exit(0)
