class coordinate:
    def __init__(self,Xvar,Yvar):
        self.x=int(Xvar)
        self.y=int(Yvar)
    
    def __lt__(self,a):
        if self.x<a.x or self.y<a.y:
            return 1
        else :
            return 0

def HS12MBR():
    lines=int(input())
    LL=coordinate(0,0)
    UR=coordinate(0,0)
    while lines:
        string=input().split()

        if string[0]=='c':
            LLR=coordinate(int(string[1])-int(string[3]),int(string[2])-int(string[3]))
            URR=coordinate(int(string[1])+int(string[3]),int(string[2])+int(string[3]))
            if LLR<LL:
                LL=LLR
            if UR<URR:
                UR=URR
        
        elif string[0]=='p':
            LLR=coordinate(string[1],string[2])
            URR=coordinate(string[1],string[2])
            if LL<LLR:
                LL=LLR
            if UR<URR:
                UR=URR
        else :
            LLR=coordinate(string[1],string[2])
            URR=coordinate(string[3],string[4])
            if LL<LLR:
                LL=LLR
            if UR<URR:
                UR=URR
        lines=lines-1
        
    print( LL.x,LL.y,UR.x,UR.y)
    print('')
            
                



def main():
    times=int(input())
    while times:
        HS12MBR()
        times=times-1
    return

if __name__=="__main__":
    main()
    exit(0)