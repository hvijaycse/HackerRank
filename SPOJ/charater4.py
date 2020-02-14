def  pattern():
    row,column,h,w=map(int,input().split())
    rower=3+h-2
    columer=3+w-2
    for i in range(1+row*(1+h)):
        for j in range(1+column*(1+w)):
            if i%rower == 0 :
                print("*",end='')
            else:
                if j%columer == 0 :
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
