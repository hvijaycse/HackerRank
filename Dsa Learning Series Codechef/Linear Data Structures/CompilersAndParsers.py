def main():
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        String = input()
        L_count = 0
        Maximum = 0
        cuur_count = 0
        for i in String:
            if i == '<':
                L_count += 1
                cuur_count +=1
            elif not L_count:
                break
            else:
                L_count -= 1
                cuur_count += 1
                if not( L_count):
                    Maximum += cuur_count
                    cuur_count = 0
        print( Maximum)

    return

if __name__ == "__main__":
    main()
    exit(0)