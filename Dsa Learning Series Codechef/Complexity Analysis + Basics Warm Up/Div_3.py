
def Mult3( K , d0, d1):
    Pattern = [2,4,8,6]
    Sum = d0 + d1
    for i in range( K -2):
        if not Sum % 10:
            break
        if  Sum %10 == 2:
            Length = K - (i + 2)
            Sum += 20*( Length // 4) 
            for i in range( Length %4):
                Sum += Pattern[i]
            break
        Sum += Sum % 10
    if not Sum % 3:
        return 'YES'
    else:
        return 'NO'
            

def main():
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        K , d0, d1 = map( int, input().split()) 
        print( Mult3( K, d0, d1))
    return

if __name__ == "__main__":
    main()
    exit(0)