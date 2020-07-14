
def mod(num1, num2,):
    if num1 > num2:
        return num1 - num2
    return num2 - num1


def main():
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        data = list( map( int, input().split() ) )
        N = data[0]
        Password = data[1:]
        i = 0 
        while i < N -1:
            if Password[i] == -1:
                Back = Password[ i - 1] 
                Rear = Password[ i + 1] 
                if Back % 2 == Rear % 2:
                    Password[i] = mod( Back, Rear)
                else:
                    Password[i] = ( Back + Rear) //2
            if Password[i] > 1:
                print( Password[i] - 1, end = '')
            else:
                print( Password[i], end = '')
            i += 1
        print(Password[N-1])

if __name__ == "__main__":
    main()
    exit(0)