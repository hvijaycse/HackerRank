def binary(num):
    string=''
    while num>0:
        string=string+str(num%2)
        num=num//2
    return string[::-1]

def main():
    string=input()
    print('char. ASCII code')
    for i in string:
        print(i,' ',ord(i),binary(ord(i)))
    return

if __name__=="__main__":
    main()