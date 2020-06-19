

def main():
    TestCase = int( input() )
    while TestCase:
        TestCase -= 1
        Start = list( map( int, input().split()))
        End = list( map( int, input().split()))
        Count = 0
        Whiler = []
        for s, e in zip( Start, End):
            if s != e:
                Whiler.append(1)
            else:
                Whiler.append(0)
        while Whiler[0] or Whiler[1] or Whiler[2]:
            Count += 1
            if Whiler.count(1) == 1:
                break
            else:
                




if __name__ == "__main__":
    main()