def Int():
    return int(input())


def List():
    return input().split()


def Ilist():
    return list(map(int, input().split()))


def yes():
    print('YES')


def no():
    print('NO')


def FloodFill(Matrix, X, Y, X_limit, Y_limit):
    Coordinates = [(X, Y)]
    Time = 0
    while Coordinates:
        Time += 1
        New_cordinate = []
        for cord in Coordinates:
            x, y = cord
            Movement = [
                (x - 1, y),
                (x + 1, y),
                (x, y - 1),
                (x, y + 1)
            ]
            for move in Movement:
                if -1 < move[0] and move[0] < X_limit and -1 < move[1] and move[1] < Y_limit:
                    if Matrix[move[0]][move[1]] == 'o':
                        Matrix[move[0]][move[1]] = 'V'
                        New_cordinate.append(move)
        Coordinates = New_cordinate
        # for row in Matrix:
        #     print(row)
        # print('-' * Y_limit)
        # print( Coordinates)
    return Time


def main():
    M, N = Ilist()
    Matrix = []
    for _ in range(M):
        row = List()
        Matrix.append(row)
    X, Y = Ilist()
    Matrix[X ][Y ] = 'V'
    print(FloodFill(Matrix, X , Y , M, N))


if __name__ == "__main__":
    main()
    exit(0)

# o o o o o c c c c c
# c o o c o c o c o c
# o o o o o o o o o o
# c c c c c c c c c c
# o c o c o c o c o c
# c o o o o o o o o c
# o o o o o o o o o o
# c c c c c c c c c c
# o o o o o c c c c c
# o o c c c c c c c c