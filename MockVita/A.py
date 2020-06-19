
def main():
    Testcase = int( input())
    while Testcase:
        Testcase -= 1
        Max_Price = int( input())
        last_sum = 1
        count = 1
        while  last_sum < Max_Price :
            last_sum = last_sum + (last_sum + 1)
            count += 1
        print( count)
    return
if __name__ == "__main__":
    main()
    exit(0)