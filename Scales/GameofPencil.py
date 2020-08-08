def solve3(A, B, C):
    Player = 0
    while True:
        print( A, B, C)
        possible = False
        for i in range( B//2 + 1,1 , -1):
            if B %i == 0 and B//i >= C:
                possible = True
                break
        if possible:
            A = i
            B = B//i
            if Player:
                Player = 0
            else:
                Player = 1
        else:
            break
    return Player