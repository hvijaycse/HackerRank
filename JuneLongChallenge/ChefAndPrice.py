
def main():
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        N, K = map( int, input().split())
        Prices = list( map( int, input().split()))[ : N ]
        Loss = 0
        for price in Prices:
            if price - K > 0 :
                Loss += price - K
        print( Loss)
    return


if __name__ == "__main__":
    main()
    exit(0)