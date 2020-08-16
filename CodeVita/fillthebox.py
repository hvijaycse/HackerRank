
def getmax_count(Array):
    # print('-'*10)
    # print( Array)
    AC = 0
    for index, count in enumerate(Array):
        while count:
            possible = False
            start = max(0, index - count + 1)
            end = start + count
            end_limt = min( N, index + count)
            while end <= end_limt and not possible:
                possible = True
                for value in Array[start: end]:
                    if value < count:
                        possible = False
                start +=1
                end += 1
            if possible:
                AC = max( AC, count)
            # print( count, possible)
            count -= 1
    return AC



N = int(input())
wall = []
RC = []
CC = []
for _ in range(N):
    row = input().split()
    RC.append(row.count('D'))
    wall.append(row)
for i in range(N):
    Column = [row[i] for row in wall]
    CC.append(Column.count('D'))

# print(
#     RC,
#     RC[::-1],
#     CC,
#     CC[::-1], sep='\n'
# )
AC1 = getmax_count( CC)
# CC.reverse()
# AC2 = getmax_count(CC)
AR1 = getmax_count( RC)
# RC.reverse()
# AR2 = getmax_count( RC)

print(max(AC1, AR1))
