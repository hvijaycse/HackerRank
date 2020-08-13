from itertools import permutations


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
        IsPalin = True
        Plain = input()
        for i in range(len(Plain) // 2):
            if Plain[i] != Plain[-i - 1]:
                IsPalin = False
                break
        if not IsPalin:
            print('Not a palindrome')
            continue
        if len(Plain) % 2:
            mid = Plain[len(Plain) // 2]
        else:
            mid = ''
        Permuts = set(permutations(Plain[: len(Plain) // 2]))
        Answer = []
        for perm in Permuts:
            Answer.append(''.join(perm) + mid + ''.join(perm[::-1]))
        Answer.sort()
        print('\n'.join(Answer))


if __name__ == "__main__":
    main()
    exit(0)
