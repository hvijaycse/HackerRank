def  pattern():
    row,column=map(int,input().split())
    
    for i in range(row):
        for j in range(column):
            if i == 0 or i == row-1:
                print("*",end='')
            elif j==0 or j==column-1:
                print("*",end='')
            else:
                print(".",end='')
        print('')


def main():
    times=int(input())
    while times:
        pattern()
        times=times-1

if __name__=="__main__":
    main()
