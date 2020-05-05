check = {
        '1' : True,
        '0': False
    }

convert = {
    0 : '0',
    1 : '1'
}

def bin( num):
    global convert
    string = []
    while num:
        string = [convert[num % 2]] + string
        num = num >> 1
    return string  


def todec( string):
    num = 0 
    power = len(string) -1
    for s in string:
        if check[s] :
            num += 2 ** power
        power -= 1
    return num

def F( X,Y, L, R):
    global check
    maximum = X
    other = Y
    if Y > maximum:
        maximum = Y
        other = X
    maximum = bin( maximum)
    other = bin( other)
    diff = len( maximum) - len(other) 
    for index , Value in enumerate( other):
        if check[Value]:
            maximum[ diff + index ] = '1'
    temp_max = todec( maximum)
    while temp_max > R:
        maximum = maximum[1:]
        temp_max = todec( maximum)
    return temp_max  

if __name__ == "__main__":
    TestCase = int(input())
    while TestCase:
        TestCase -= 1
        X, Y, L ,R = map( int, input().split())
        print(F(X, Y, L, R))
    exit(0)   