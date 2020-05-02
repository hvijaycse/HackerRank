

if __name__ == '__main__':
    Rows = int( input())
    Column = int( input())
    Matrix = []
    for _ in range(Rows):
        row = list( map(int , input().split()))
        Matrix.append(row)
    Max_sum = max( Matrix[0])
    Last =  Max_sum
    for row in range(1, Rows):
        New_max = max( Matrix[row])
        if New_max > Last:
            Max_sum += New_max
            Last = New_max
        else:
            break
    print(Max_sum)
    