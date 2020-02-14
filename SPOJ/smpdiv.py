def Dividers():
    num,x,y=map(int,input().split())

    for i in range(1,num):
        if i%x==0 and i%y!=0:
            print(i,end=' ')
    print('')
def main():
    times=int(input())
    while times:
        Dividers()
        times=times-1
    return

if __name__=="__main__":
    main()
    exit(0)