# cook your dish here


def main():
    TestCase = int( input() )
    while TestCase:
        TestCase -= 1
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
            DictT[elm] = DictT[ elm] // 2
        if WillContinue:
            ans = 0
            Minimum = min( DictT.keys())
            A_list = []
            B_list = []
            for elm in DictB.keys():
                if elm not in DictA:
                    A_count = 0
                else:
                    A_count = DictA[elm]
                if DictB[elm] > A_count:
                    Length = DictB[elm] - A_count  
                    for i in range( Length):
                        B_list.append(elm)          
            for elm in DictA.keys():
                if elm not in DictB:
                    B_count = 0
                else:
                    B_count = DictB[elm]
                if DictA[elm] > B_count:
                    Length = DictA[elm] - B_count
                    for i in  range( Length):
                        A_list.append( elm)
            A_list.sort()
            B_list.sort()
            Length = len( A_list)
            while A_list and B_list:
                if A_list[0] < B_list[0]:
                    if A_list[0] * ( Length -1 ) > (Minimum* Length):
                        ans += Minimum * Length
                        break
                    else:
                        ans += A_list[0] 
                    A_list = A_list[2:]
                    B_list.pop()
                    B_list.pop()
                    Length -= 2
                else:
                    if B_list[0] * ( Length -1 ) > (Minimum* Length):
                        ans += Minimum * Length
                        break
                    else:
                        ans += B_list[0] 
                    B_list = B_list[2:]
                    A_list.pop()
                    A_list.pop()
                    Length -= 2
            print( ans)

if __name__ == "__main__":
    main()
    exit(0)