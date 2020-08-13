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
    Match = True
    String = input()
    pattern = input()
    last_char = ''
    Si = 0
    Pi = 0
    while Si < len(String) and Pi < len(pattern):
        if pattern[Pi] == '+':
            while Si < len(String) and String[Si] == last_char:
                Si += 1
            Pi += 1
        elif pattern[Pi] == String[Si]:
            last_char = pattern[Pi]
            Pi += 1
            Si += 1
        else:
            Match = False
            break
    
    if Pi < len( pattern):
        if pattern[Pi] == '+':
            Pi += 1
        else:
            Match = False 

    if Match and Si == len(String) and Pi == len(pattern):
        print('Matched')
    else:
        print('Does not match')


if __name__ == "__main__":
    main()
    exit(0)
