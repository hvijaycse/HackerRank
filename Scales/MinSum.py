# class solution:


def solve( A, B, C):
    Parent = {}
    Values = {}
    for rows in B:
        Parent[rows[1]] = rows[0]
        Values[(rows[0], rows[1])] = rows[2]
    Counts = {}
    for i in range( A , 1, -1):
        P = Parent[i]
        if (P,i) not in Counts:
            Counts[(P,i)] = 1
        else:
            Counts[(P,i)] += 1
        while P != 1:
            i = P
            P = Parent[i]
            if (P,i) not in Counts:
                Counts[(P,i)] = 1
            else:
                Counts[(P,i)] += 1

    Summer = []
    for count in Counts:
        Summer.append(
            Values[count]* Counts[count]
        )
    Summer.sort()
    # print( Counts)
    # print(Summer)
    while C and Summer[-1] >=0:
        Summer.pop()
        C -= 1
    Total = sum( Summer)%( 10**9 + 7)
    print( Total)
            
            




        