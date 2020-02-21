
def Zeros(Number):
    count = 0
    while Number >= 5 :
        Number = Number //5
        count = count + Number
    return count

if __name__ == '__main__':
    tests = int( input())
    while tests:
        tests = tests - 1
        Number = int (input())
        print(Zeros(Number))
    exit(0)
        