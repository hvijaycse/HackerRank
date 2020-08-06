def Int():
    return int( input() )

def List():
    return input().split()

def Ilist():
    return list( map( int, input().split()))

def yes():
    print('YES')

def no():
    print('NO')

def getRoman(number): 
    num = [1, 4, 5, 9, 10, 40, 50, 90,  
           100, 400, 500, 900, 1000] 
    sym = ["I", "IV", "V", "IX", "X", "XL",  
           "L", "XC", "C", "CD", "D", "CM", "M"] 
    i = 12
    Roman = []
    while number: 
        div = number // num[i] 
        number %= num[i] 
        while div: 
            Roman.append( sym[i])
            div -= 1
        i -= 1
    return ''.join(Roman)

def main():
    N = Int()
    Values = {}
    for char in ['I', 'V', 'X', 'L', 'C', 'D', 'M']:
        Values[char] = ord(char) - ord('A') + 10
    while 1 <= N  and N <= 3999:
        roman = getRoman(N)
        tmpN = 0
        Base = float('-inf')
        for char in roman:
            if Base < Values[char]:
                Base = Values[char]
        Base += 1
        power = len( roman) -1 
        for char in roman:
            tmpN += Values[char] * ( Base ** power)
            power -= 1
        # print( roman ,":", tmpN)
        N = tmpN
    print( N)        

if __name__ == "__main__":
    main()
    exit(0)