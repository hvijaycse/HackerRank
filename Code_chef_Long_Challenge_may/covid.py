
def Covid():
    N = int(input())
    Persons = list(map(int, input().split()))
    Diff = []
    for i in range( N - 1):
        Diff.append( Persons[i + 1] - Persons[i])
    MaxLen = len( Diff) 
    Minimum = float('inf')
    Maximum = 1
    i = -1
    while i < MaxLen:
        i += 1
        count = 1
        while i < MaxLen and Diff[i] < 3:
            count += 1
            i += 1
        if Maximum < count :
            Maximum = count
        if count < Minimum :
            Minimum = count
    print( Minimum, Maximum)
    return

        
    

if __name__ == "__main__":
    TestCase = int(input( ))
    while TestCase:
        TestCase -= 1
        Covid()
    exit(0)