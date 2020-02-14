def palin():
    string=input()
    old=string
    string=[i for i in string]
    if len(string)%2==0:
        mid=int(len(string)/2 -1)
        for i in range(len(string)//2):
            neg=i*-1 -1
            string[neg]=string[i]
        while True:
            if int(old)<int(''.join(string)):
                return ''.join(string)
            else:
                string[mid]=str(int(string[mid])+1)
                string[mid*-1 -1]=string[mid]
                continue
    else:
        mid=len(string)//2 
        for i in range(len(string)//2):
            neg=i*-1
            string[neg]=string[i]
        while True:
            if int(old)<int(''.join(string)):
                return ''.join(string)
            else:
                string[mid]=str(int(string[mid])+1)
                continue

        
    



if __name__=="__main__":
    times=int(input())
    while times:
        times=times-1
        print(palin())