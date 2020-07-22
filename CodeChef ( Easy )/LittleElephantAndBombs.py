def main():
    TestCase = int( input() )
    for _ in range( TestCase):
        N = int( input() )
        Buildings = list(input())
        if N >1:
            for i in range( N ):
                if Buildings[i] == '1':
                    if  i == 0:
                        if Buildings[i + 1] == '0':
                            Buildings[i + 1] = '2'
                    elif i == N - 1:
                        if Buildings[i - 1] == '0':
                            Buildings[i - 1] = '2'
                    else:
                        if Buildings[i + 1 ] == '0':
                            Buildings[i + 1] = '2'
                        if Buildings[i - 1] == '0':
                            Buildings[i - 1] = '2'
        print( Buildings.count('0'))

                
    
if __name__ == "__main__":
    main()
    exit(0)