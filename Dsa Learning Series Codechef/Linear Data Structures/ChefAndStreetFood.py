
def main():
    TestCase = int( input() )
    while TestCase:
        TestCase -= 1
        N = int( input())
        profit = 0
        while N:
            N -= 1
            S, P, V = map( int, input().split())
            S += 1
            Current_profit = ( P // S) * V
            if Current_profit > profit:
                profit = Current_profit
        print( profit)
    return

if __name__ == "__main__":
    main()
    exit(0)