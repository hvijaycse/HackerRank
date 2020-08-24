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
    for _ in range(TestCase):
        _, K = Ilist()
        Weights = Ilist()
        trip = 0
        summer = 0
        for w in Weights:
            if w > K:
                trip = -1
                break
            if summer + w < K:
                summer += w
            elif summer + w == K:
                summer = 0
                trip += 1
            else:
                summer = w
                trip += 1
        if trip != -1 and summer >0 and summer <= K:
            trip += 1
        print(trip)
            



if __name__ == "__main__":
    main()
    exit(0)
