def Int():
    return int( input() )

def List():
    return input().split()

def Ilist():
    return list( map( int, input().split()))

def yes():
    print('yes')

def no():
    print('no')

def main():
    jump = False
    N = Int()
    Six = N % 6
    if Six == 0 or Six == 1 or Six == 3:
        jump = True
    if jump:
        yes()
    else:
        no()



if __name__ == "__main__":
    main()
    exit(0)