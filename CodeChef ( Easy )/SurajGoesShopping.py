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

def main():
    TestCase = Int()
    for _ in range(TestCase):
        N = Int()
        price = Ilist()
        assert( N == len( price))
        price.sort()
        cost = 0
        for i in range( len(price), 0, -4):
            end = i -4
            if end < 0:
                end = 0
            tmp_array = price[end : i]
            if len(tmp_array ) ==1:
                cost += tmp_array[0]
            elif len( tmp_array) == 2:
                cost += tmp_array[0] + tmp_array[1]
            else:
                cost += tmp_array[-1] + tmp_array[-2]
        print( cost)
        

if __name__ == "__main__":
    main()
    exit(0)