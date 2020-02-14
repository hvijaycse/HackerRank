def rev(string):
    temp=''
    lenght=len(string)
    while lenght:
        temp+=string[lenght-1]
        lenght-=1
    return temp
        

def palin():
    string=input().strip()
    lenght=len(string)
    if string=='9'*lenght:
        return str(int(string)+2)
    mid=lenght//2
    if lenght%2 !=0:
        number=int(string[0:mid+1])
        temp=str(number)
        temp=temp+rev(temp[0:-1])
        while temp<string:
                number+=1
                temp=str(number)
                temp+=rev(temp)
        
    else:
        if string[mid-1]>string[mid]:
            temp=string[0:mid]+rev(string[0:mid])            
        else:
            number=int(string[:mid])
            temp=str(number)
            temp+=rev(temp)
            while temp<string:
                number+=1
                temp=str(number)
                temp+=rev(temp)
                
    
    return temp
    
if __name__=="__main__":
    times=int(input())
    while times:
        print(palin(),'\n')
        times=times-1
    exit(0)