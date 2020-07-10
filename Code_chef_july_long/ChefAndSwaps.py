# cook your dish here


def main():
    TestCase = int( input() )
    while TestCase:
        TestCase -= 1
        Cost = 0
        N = int( input() )
        A = list( map( int, input().split() ) )[ :N ]
        B = list( map( int, input().split() ) )[ :N ]
        DictA = {}
        DictB = {}
        DictT = {}
        for a in A:
            if a not in DictA:
                DictA[a] = 1
                DictT[a] = 1
            else:
                DictA[a] += 1
                DictT[a] += 1

        for b in B:
            if b not in DictB:
                DictB[b] = 1
            else:
                DictB[b] += 1

            if b not in DictT:
                DictT[b] = 1
            else:
                DictT[b] += 1

        WillContinue = True
        for elm in DictT.keys() :
            if DictT[elm] % 2 != 0:
                print(-1)
                WillContinue = False
                break

        if WillContinue:
            for elm in DictT.keys():
                if elm not in DictA:
                    DictA[elm] = 0
                if elm not in DictB:
                    DictB[elm] = 0
            A_Great = []
            B_Great = []
            for elm in DictT.keys():
                if DictA[elm] > DictB[elm]:
                    A_Great.append( elm )
                elif DictB[elm] > DictA[elm]:
                    B_Great.append( elm ) 
            A_Great.sort( reverse = True)
            B_Great.sort()
            while A_Great and B_Great:
                a = A_Great[-1]
                b = B_Great[-1]
                DictA[a] -= 1
                DictB[a] += 1
                DictA[b] += 1
                DictB[b] -= 1
                if DictA[a] == DictB[a]:
                    A_Great.pop()
                if DictB[b] == DictA[b]:
                    B_Great.pop()
                Cost += min( [a, b])
            print( Cost)
       

if __name__ == "__main__":
    main()
    exit(0)