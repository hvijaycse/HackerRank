
def main():
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        Pairs = 0
        Friends = input()
        index = 1
        while index < len( Friends):
            if (Friends[index -1 ] == 'x' and Friends[index] == 'y') or (Friends[index -1 ] == 'y' and Friends[index] == 'x'):
                Pairs += 1
                index += 2
            else:
                index += 1
        print( Pairs)
    return

if __name__ == "__main__":
    main()
    exit(0)