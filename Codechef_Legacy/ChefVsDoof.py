
def main():
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        N = int(input())
        A = list( map( int, input().split()) )[ : N]
        for a in A:
            if not a %2:
                print('NO')
                break
        if a%2:
            print( 'YES')

        


if __name__ == "__main__":
    main()
    exit(0)