def main():
    N = int( input())
    Bracket = input().split()[ : N ]
    Nest_Depth, Max_Depth = 0, 0
    First_Index, tmp_FI = 0, 0
    Max_Symbol, tmp_MS = 0, 0
    Max_Index, tmp_MI = 0, 0
    Index = 0
    while Index < N:
        if Bracket[Index] == '1':
            if not Nest_Depth:
                tmp_MI = Index
            tmp_FI = Index
            Nest_Depth += 1
            tmp_MS += 1
        else:
            if Nest_Depth > Max_Depth:
                Max_Depth = Nest_Depth
                First_Index = tmp_FI
            Nest_Depth -= 1
            
            tmp_MS += 1
            if not Nest_Depth:
                if tmp_MS > Max_Symbol:
                    Max_Symbol = tmp_MS
                    Max_Index = tmp_MI
                tmp_MS = 0
        Index += 1
    print( Max_Depth, First_Index + 1, Max_Symbol, Max_Index + 1 )
    return

if __name__ == "__main__":
    main()
    exit(0)