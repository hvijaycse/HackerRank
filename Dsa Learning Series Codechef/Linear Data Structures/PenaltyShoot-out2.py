def mod( num ):
    if num > 0 :
        return num
    else:
        return num * -1

def main():
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        N = int( input())
        Goals = input()[ : 2* N]
        A_goals, B_goals = 0, 0
        Tries =  N - 1
        i = -2
        while i < 2*N - 2:
            i += 2
            if Goals[i] == '1':
                A_goals += 1
            if A_goals > B_goals and A_goals - B_goals  > Tries + 1:
                i -= 1
                break
            if B_goals > A_goals and B_goals - A_goals > Tries:
                i -= 1
                break
            if Goals[i + 1] == '1':
                B_goals += 1
            if mod( A_goals - B_goals ) > Tries:
                break
            Tries -= 1
        print( i + 2)
    return

if __name__ == "__main__":
    main()
    exit(0)