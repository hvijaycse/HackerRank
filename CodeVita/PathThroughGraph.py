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


def prime_list():
    N = 32000
    Prime = [True for _ in range(N + 1)]
    S = 2
    while S * S <= N:
        if Prime[S]:
            for i in range(S*S, N + 1, S):
                Prime[i] = False
        S += 1
    Final_list = []
    for i in range(2, N + 1):
        if Prime[i]:
            Final_list.append(i)
    return Final_list


def main():
    PrimeNumbers = prime_list()
    M, N = Ilist()
    if M == N:
        print(0)
        return
    Bigger = max(M, N)
    Smaller = min(M, N)
    tmpB = Bigger
    tmpS = Smaller

    Parent1 = []
    Parent2 = []

    while Bigger > 1:
        for p in PrimeNumbers:
            if not Bigger % p:
                Bigger = Bigger // p
                Parent1.append(Bigger)
                break
    if Parent1[0] != tmpB:
        Parent1 = [tmpB] + Parent1
    # Parent1.reverse()
    while Smaller > 1:
        for p in PrimeNumbers:
            if not Smaller % p:
                Smaller = Smaller // p
                Parent2.append(Smaller)
                break
    if not Parent2:
        Parent2.append(1)
    if Parent2[0] != tmpS:
        Parent2 = [tmpS] + Parent2

    # print( Parent1, Parent2)

    for index, factor in enumerate( Parent2):
        if factor in Parent1:
            print(  index + Parent1.index(factor))
            break
if __name__ == "__main__":
    main()
    exit(0)
