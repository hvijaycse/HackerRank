

def main():
    A, B = map( int, input().split() )
    ans = A - B
    last = ans % 10
    if last == 9:
        Nlast = 8
    else:
        Nlast = last + 1
    ans = ans - last + Nlast
    print( ans)

if __name__ == "__main__":
    main()
    exit(0)