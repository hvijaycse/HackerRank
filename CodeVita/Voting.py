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
    N = Int()
    Voters = 'A' + input() + 'B'
    VC = {
        'A': -1,
        'B': -1
    }
    LV = ''
    Index = 0
    while Index < len(Voters):
        Vote = Voters[Index]
        if Vote != '-':
            LV = Vote
            VC[Vote] += 1
        else:
            DC = 0
            while Voters[Index] == '-':
                DC += 1
                Index += 1
            NV = Voters[Index]
            if NV == LV:
                VC[NV] += 1
            elif LV == 'B' and NV == 'A':
                VC['A'] += DC //2
                VC['B'] += DC //2
            VC[NV] += 1
            LV = NV
        Index += 1
    
    if VC['A'] == VC['B']:
        print('Coalition Goverment')
    elif VC['A'] > VC['B']:
        print('A')
    else:
        print('B')

if __name__ == "__main__":
    main()
    exit(0)
