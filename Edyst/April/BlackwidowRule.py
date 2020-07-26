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
        Data = Ilist()
        N = Data[0]
        Matrix =[ Data[start : start+N] for start in range(2,N*N, N)]
        DictCount ={}
        Values = set()
        for r, Row in enumerate( Matrix):
            for c, value in enumerate(Row):
                if value in DictCount:
                    DictCount[value].append( (r,c))
                else:
                    DictCount[value] = [(r,c)]
                Values.add( value )
        Rows , Columns = set(), set()
        for value in Values:
            if len(DictCount[value]) > 1:
                Row = []
                Column = []
                for cordinate in DictCount[value]:
                    r,c = cordinate[0], cordinate[1] 
                    if r in Row:
                        Rows.add(r)
                    else:
                        Row.append(r)
                    if c in Column:
                        Columns.add(c)
                    else:
                        Column.append(c)
        if Rows or Columns:
            print( 'DANGER', len(Rows), len(Columns))
        else:
            print('SAFE')
       

if __name__ == "__main__":
    main()
    exit(0)