
def Int():
    return int( input() )

def List():
    return input().split()

def Ilist():
    return list( map( int, input().split()))

def yes():
    print('YES')

def no():
    print('NO')

def main():
    TestCase = Int()
    for _ in range(TestCase):
        N = Int()
        Array = Ilist()
        assert( N == len( Array))
        count = 0
        DictCount = {}
        for elm in Array:
            if elm in DictCount:
                DictCount[elm] += 1
            else:
                DictCount[elm] = 1
        Total = sum( DictCount.values())
        Elements = list(DictCount.keys())
        Elements.sort()
        for Element in Elements[ : -1]:
            Total = Total - DictCount[ Element]
            count += Total * DictCount[Element]
        print( count)
        
if __name__ == "__main__":
    main()
    exit(0)