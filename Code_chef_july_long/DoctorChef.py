
def main():
    TestCase = int( input() )
    while TestCase:
        TestCase -= 1
        N, x = map( int, input().split() )
        Countries_Patient = list( map( int, input().split() ) )[ : N]
        Countries_Patient.sort()
        Days = 0 
        Start = 0 
        Max = len( Countries_Patient)
        while  Start + 1 < Max and Countries_Patient[Start] < x:
            Start += 1
        if Start > 0:
            count1 = 0
            count2 = 1
            tmpx = x
            while tmpx < Countries_Patient[Start]:
                tmpx = tmpx << 1
                count1 += 1
            tmpx = Countries_Patient[ Start -1 ] * 2
            while tmpx < Countries_Patient[ Start]:
                tmpx = tmpx << 1
                count2 += 1
            if count2 <= count1:
                Start = Start - 1
        forward = Start
        Backward = Start - 1
        while forward < Max:
            Days += 1
            if x >= Countries_Patient[forward]:
                x = Countries_Patient[forward]
                Countries_Patient[forward] = 0
                forward += 1
            x = x << 1
        while Backward >= 0:
            Days += 1
            if x >= Countries_Patient[ Backward]:
                x = Countries_Patient[Backward]
                Countries_Patient[ Backward] = 0
                Backward -= 1
            x = x << 1
        print( Days)   
if __name__ == "__main__":
    main()
    exit(0)