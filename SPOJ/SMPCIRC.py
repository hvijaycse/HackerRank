def circles():
    x1,y1,r1,x2,y2,r2=map(int,input().split())

    if x1==x2:
        if y1==y2:
            if r1==r2:
                print('O')
                return 
    distance= int(((x2-x1)**2+(y2-y1)**2)**0.5)
    if distance+r1 <r2 or distance+r2<r1:
        print('I')
    elif distance+r1==r2 or distance+r2==r1:
        print('E')
    else:
        print('O')


def main():
    times=int(input())
    while times:
        circles()
        times=times-1
    
    return

if __name__=="__main__":
    main()
    exit(0)