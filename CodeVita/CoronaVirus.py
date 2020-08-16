def Int():
    return int(input())


def MList():
    return input().split()


def Ilist():
    return list(map(int, input().split()))


def yes():
    print('YES')


def no():
    print('NO')


def main():
    # let's define moves
    TR = (-1, 1)
    TL = (-1, -1)
    BR = (1, 1)
    BL = (1, -1)

    # lets define rotation:
    Clockwise = {
        TR: BR,
        BR: BL,
        BL: TL,
        TL: TR,
    }

    AntiC = {
        TR: TL,
        TL: BL,
        BL: BR,
        BR: TR,
    }

    WallTOP = {
        TR : BR,
        TL : BL,
        BR : TR,
        BL : TL
    }

    Wallside = {
        TL:TR,
        TR:TL,
        BL : BR,
        BR : BL
    }

    safe = 0
    Dead = 0
    Matrix = []
    for _ in range(9):
        row = [char for char in input()]
        Matrix.append(row)
        safe += row.count('a')
        safe += row.count('c')
    Hits = 0
    Y, X = 7, 1
    Movement = TR
    Locations = [[0, 0]]
    while Hits < 2:
        # print('.', end='')
        Locations.append([X, 8-Y])
        # print(X, 8-Y,Y,X)
        if Matrix[Y][X] != '.':
            # print(Matrix[Y][X])
            if Matrix[Y][X] == 'a':
                Matrix[Y][X] = '-'
                Movement = AntiC[Movement]
                Dead += 1
            elif Matrix[Y][X] == 'c':
                Matrix[Y][X] = '-'
                Movement = Clockwise[Movement]
                Dead += 1
            else:
                Hits += 1
                if Y == 0 or Y == 8:
                    Movement = WallTOP[Movement]  
                else:
                    Movement = Wallside[Movement] 
            # print(Movement)
        Y += Movement[0]
        X += Movement[1]
    for location in Locations:
        print(location[0], location[1])
    for row in Matrix:
        print(''.join(row))
    print('safe=', safe - Dead, sep='')
    print('infected=', Dead, sep='')


if __name__ == "__main__":
    main()
    exit(0)
