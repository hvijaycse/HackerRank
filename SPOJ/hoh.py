def hoh():
    string=input()
    i=0
    while i<int(len(string)/2):
        print(string[i],end='')
        i=i+2
    print('')


def main():
    times=int(input())
    while times:
        hoh()
        times=times-1
    

if __name__=="__main__":
    main()

exit(0)