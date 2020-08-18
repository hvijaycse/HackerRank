# cook your dish here
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


def getEff(Relatvie, start, end, cost, dp, fc):
    # print((start, end))
    Stack = [(start, end)]
    while Stack:
        i, j = Stack[-1]
        found = True
        if i == j:
            ans = 0
        elif dp[i][j] != None:
            ans = dp[i][j]
        else:
            ans = float('inf')
            for k in range(i, j):
                tmp_ans = fc[i][k]
                dp[i][k] = tmp_ans
                if dp[k + 1][j] != None:
                    tmp_ans += dp[k + 1][j]
                    if tmp_ans < ans:
                        ans = tmp_ans
                else:
                    found = False
                    Stack.append((k + 1, j))
        if found:
            dp[i][j] = ans
            Stack.pop()
    return dp[start][end]

def main():
    TestCase = Int()
    for _ in range(TestCase):
        N, K = Ilist()
        Relative = Ilist()
        dp = [[None for _ in range(N + 1)] for _ in range(N + 1)]
        fc = [[0 for _ in range(N)] for _ in range(N)]

        for start in range(N):
            cost = K
            DC = {}
            for end in range(start, N):
                rel = Relative[end]
                if rel not in DC:
                    DC[rel] = 1
                else:
                    DC[rel] += 1
                    if DC[rel] == 2:
                        cost += 2
                    else:
                        cost += 1
                fc[start][end] = cost

        print(getEff(Relative, 0, N, K, dp, fc))

        # for row in dp:
        #     print(row)

        # for i in range(N):
        #     for j in range(i, N):
        #         print((i, j), fc[i][j], end=' , ')
        #     print()


if __name__ == "__main__":
    main()
    exit(0)
