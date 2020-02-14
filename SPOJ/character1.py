def pattern():
    row,column=map(int,input().split())
    pattern_even=['*','.']
    pattern_odd=['.','*']
    for i in range(row):
        if i%2==0:
            patt=pattern_even
        else:
            patt=pattern_odd
        for j in range(column):
            print(patt[j%2],end='')
        print('')

def main():
    times=int(input())
    while times:
        pattern()
        times=times-1

if __name__=="__main__":
    main()