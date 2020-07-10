
def main():
    TestCase = int( input() )
    while TestCase:
        TestCase -= 1
        N, x = map( int, input().split() )
        xtmp = x
        Countries_Patient = list( map( int, input().split() ) )[ : N]
        Countries_Patient.sort()
        Tmp_Patient = [a for a in Countries_Patient]
        Days1 = 0 
        Days2 = 0 
        Start = 0 
        Max = len( Countries_Patient)
        while  Start < Max and Countries_Patient[Start] < x:
            Start += 1
        tmpStart = Start
        if Start > 0:
            tmpStart = Start - 1
        forward = Start
        Backward = Start - 1
        while forward < Max:
            # print( Countries_Patient, x, forward)
            Days1 += 1
            if x >= Countries_Patient[forward]:
                x = Countries_Patient[forward]
                Countries_Patient[forward] = 0
                forward += 1
            x = x << 1
        while Backward >= 0:
            Days1 += 1
            # print( Countries_Patient, x)
            if x >= Countries_Patient[ Backward]:
                x = Countries_Patient[Backward]
                Countries_Patient[ Backward] = 0
                Backward -= 1
            x = x << 1
        
        forward = tmpStart
        Backward = tmpStart - 1
        while forward < Max:
            # print( Countries_Patient, x, forward)
            Days2 += 1
            if xtmp >= Tmp_Patient[forward]:
                xtmp = Tmp_Patient[forward]
                Tmp_Patient[forward] = 0
                forward += 1
            xtmp = xtmp << 1
        while Backward >= 0:
            Days2 += 1
            # print( Tmp_Patient, xtmp)
            if xtmp >= Tmp_Patient[ Backward]:
                xtmp = Tmp_Patient[Backward]
                Tmp_Patient[ Backward] = 0
                Backward -= 1
            xtmp = xtmp << 1
        print( min(( Days1, Days2)))
            
if __name__ == "__main__":
    main()
    exit(0)