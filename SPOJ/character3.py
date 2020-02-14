def  pattern():
    row,column=map(int,input().split())
    for i in range(4+3*(row-1)):
        for j in range(4+3*(column-1)):
            if i%3 == 0 :
                print("*",end='')
            else:
                if j%3 == 0 :
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
