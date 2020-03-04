#!/bin/python3
# Complete the minimumMoves function below.

def minimumMoves(grid, Length, startX, startY, goalX, goalY, Last_move = None, key = 0, values = {}):
    if startX < 0 or startX >= Length or startY < 0 or startY >= Length:
        return  values
    if grid[startX][startY] == 'X':
        return values
    if not Last_move:
        values[(startX, startY )] = key
        #Down
        values = minimumMoves( grid, Length, startX + 1, startY, goalX, goalY, 1, key + 1, values)
        #up
        values = minimumMoves( grid, Length, startX - 1, startY, goalX, goalY, 2, key + 1, values)
        #LEft
        values = minimumMoves( grid, Length, startX, startY + 1, goalX, goalY, 3, key + 1, values)
        #Right
        values = minimumMoves( grid, Length, startX, startY - 1, goalX, goalY, 4, key + 1, values)
    else:
        if (startX, startY) in values:
            Last_key = values[(startX, startY)]
            if Last_key <= key:
                return values
            else:
                values[(startX, startY)] = key
        else:
            values[(startX, startY)] = key
        if startX == goalX and startY == goalY:
            return values
        else:
            values[(startX, startY)] = key
        # print( startX, startY, values[(startX, startY)])
        if Last_move == 1:
            #Contine Down
            values = minimumMoves( grid, Length, startX + 1 , startY, goalX, goalY, 1, key , values)
            #LEft
            values = minimumMoves( grid, Length, startX, startY + 1, goalX, goalY, 3, key + 1, values)
            #Right
            values = minimumMoves( grid, Length, startX, startY - 1, goalX, goalY,  4, key + 1, values)
        if Last_move == 2:
            #Contine up
            values = minimumMoves( grid, Length, startX - 1 , startY, goalX, goalY, 2, key, values)
            #LEft
            values = minimumMoves( grid, Length, startX, startY + 1, goalX, goalY, 3, key + 1, values)
            #Right
            values = minimumMoves( grid, Length, startX, startY - 1, goalX, goalY,  4, key + 1, values)
        if Last_move == 3:
            #up
            values = minimumMoves( grid, Length, startX + 1 , startY, goalX, goalY, 1, key + 1, values)
            #LEft
            values = minimumMoves( grid, Length, startX, startY + 1, goalX, goalY, 3, key, values )
            #Down
            values = minimumMoves( grid, Length, startX - 1, startY, goalX, goalY,  2, key + 1, values)
        if Last_move == 4:
            #up
            values = minimumMoves( grid, Length, startX + 1 , startY, goalX, goalY, 1, key + 1, values )
            #right
            values = minimumMoves( grid, Length, startX, startY - 1, goalX, goalY, 4, key, values )
            #Right
            values = minimumMoves( grid, Length, startX - 1, startY, goalX, goalY,  2, key + 1, values)
    if not Last_move:
        return values[(goalX, goalY)]
    else:
        return values
                
        
        


if __name__ == '__main__':

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, n, startX, startY, goalX, goalY)
    print(result) 

