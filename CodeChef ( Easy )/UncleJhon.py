

def Int():
    return int( input() )

def List():
    return input().split()

def Ilist():
    return list( map( int, input().split()))


def main():
    TestCase = Int()
    for _ in range( TestCase):
        Count = 0
        N = Int()
        Playlist = Ilist()[:N]
        K = Int()
        Num = Playlist[ K - 1]
        for Song in Playlist:
            if Song < Num:
                Count += 1
        print( Count + 1)
if __name__ == "__main__":
    main()
    exit(0)