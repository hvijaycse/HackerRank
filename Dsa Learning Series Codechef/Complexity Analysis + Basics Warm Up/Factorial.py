
def main():
    T = int( input())
    while T:
        T = T - 1
        Num = int( input())
        count = 0
        while Num >= 5:
            Num = Num //5
            count += Num
        print( count)
    return

if __name__ == "__main__":
    main()
    exit(0)