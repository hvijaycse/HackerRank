
def main():
    N = int( input())
    while N :
        N = N -1
        String = input()
        First = {}
        Second = {}
        length = len( String)
        Second_start = length // 2 
        if len( String) %2:
            Second_start += 1
        for i in String[: length//2]:
            if i not in First:
                First[i] = 1
            else:
                First[i] += 1
        for i in String[ Second_start:]:
            if i not in Second:
                Second[i] = 1
            else:
                Second[i] += 1
        if First == Second:
            print('YES')
        else:
            print('NO')
    return

if __name__ == "__main__":
    main()
    exit(0)