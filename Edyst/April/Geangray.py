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

def getbits(num):
    bits = set()
    mask = 1
    for i in range(32):
        if (mask <<i) & num:
            bits.add(i)
    return bits

def main():
    TestCase = Int()
    for _ in range(TestCase):
        L = Int()
        Data = Ilist()
        N = Data[0]
        Energy = Data[1:]
        FinalPower = 0
        Bits = getbits( L )
        for bit in Bits:
            factor = 1
            if bit > N - 1:
                while bit > N -1:
                    bit -= 1
                    factor = factor * 2
            curr_power = Energy[bit] * factor
            bit -= 1
            factor =  factor * 2
            while bit >= 0:
                if Energy[bit]* factor <= curr_power:
                    curr_power = Energy[bit] * factor
                factor = factor * 2
                bit -= 1
            FinalPower += curr_power
        print( FinalPower )


if __name__ == "__main__":
    main()
    exit(0)