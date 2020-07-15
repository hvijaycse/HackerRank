

def main():
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        N = int( input())
        data  = list( map( int, input().split() ) )[: N]
        Wall = [ a/2 for a in data]
        Query = int( input() )
        while Query:
            Query -= 1
            x, y = map( int , input().split())
            point = (x + y ) / 2
            start = 0
            end = N -1
            mid = (start + end )//2
            while Wall[ mid] != point:
                if start == end:
                    break
                if Wall[mid] < point:
                    start = mid + 1
                    mid = ( start + end )//2
                    continue
                else:
                    end = mid
                    mid = ( start + end) //2
            if Wall[mid] == point:
                print(-1)
            elif  Wall[mid] > point:
                print( mid)
            else:
                print( mid + 1)
if __name__ == "__main__":
    main()
    exit(0)