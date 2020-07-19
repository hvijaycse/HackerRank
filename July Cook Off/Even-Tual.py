

def main():
    TestCase = int( input() )
    for _ in range(TestCase):
        N = int( input() )
        S = input()
        Flag = True
        assert( len(S) == N )
        if N % 2:
            print("NO")
            continue
        WordCount = {}
        for w in S:
            if w in WordCount:
                WordCount[w] += 1
            else:
                WordCount[w] = 1
        for count in WordCount.values():
            if count %2 :
                print("NO")
                Flag = False
                break
        if Flag:
            print('YES')

if __name__ == "__main__":
    main()
    exit(0)