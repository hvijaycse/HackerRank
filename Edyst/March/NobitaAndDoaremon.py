
def main():
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        words = input()
        print( words[0], end = '')
        index = 1
        Length = 2
        while True:
            segement = words[ index: index + Length]
            if len( segement ) == Length:
                print( segement[0], segement[-1], end = '', sep='')
            else:
                break
            index = index + Length
            Length += 1

        print()
if __name__ == "__main__":
    main()
    exit(0)