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
        N, K = Ilist()
        S = input()
        if N != K:
            Rearrange = False
            time = N // K
            counter = {
                '0': 0,
                '1': 0,
            }
            for chars in S:
                counter[chars] += 1
            # print(zeroes, ones)
            if counter['0'] % time == 0 and counter['1'] % time == 0:
                for i in range(K):
                    if S[i] != S[2*K - i - 1]:
                        Rearrange = True
                        break
                    Back = S[:K]
                    Front = S[K:2*K]
                    i = 2*K
                    while i < N:
                        if S[i: i + K] != Back:
                            Rearrange = True
                            break
                        i += K
                        if i < N and S[i:i+K] != Front:
                            Rearrange = True
                            break
                        i += K
                if Rearrange:
                    front = '0' * (counter['0'] // time) + '1' * (counter['1'] // time)
                    back = '1' * (counter['1'] // time) + '0' * (counter['0'] // time)
                    S = ''
                    i = 1
                    while time:
                        time -= 1
                        if i%2:
                            S += front
                        else:
                            S += back
                        i += 1
            else:
                S = 'IMPOSSIBLE'
        print(S)


if __name__ == "__main__":
    main()
    exit(0)
