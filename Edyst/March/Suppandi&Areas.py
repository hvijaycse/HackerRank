

def main():
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        Shape = input()
        L1 = int( input() )
        L2 = int( input() )
        area = L1 * L2
        if Shape == 'rectangle':
            print( area )

        elif Shape == 'square':
            print( area // 2 )
        
        elif Shape == 'triangle':
            print( area )
        
        else:
            print(0)
if __name__ == "__main__":
    main()
    exit(0)