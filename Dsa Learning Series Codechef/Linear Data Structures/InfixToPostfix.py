
def main():
    Precedense = {
        '^' : 5,
        '*' : 4,
        '/' : 4,
        '-' : 3,
        '+' : 3
    }
    TestCase = int( input( ) )
    while TestCase:
        TestCase -= 1
        N = int( input())
        S = input()[ : N]
        S = '(' + S + ')'
        Operator = []
        for character in S:
            if character == '(':
                Operator.append('(')
            elif character == ')':
                Op = Operator.pop()
                while Op != '(':
                    print( Op, end = '')
                    Op = Operator.pop()
            elif character in Precedense:
                while Operator[-1] != "(" and Precedense[ Operator[ -1 ] ] >= Precedense[ character]:
                    print( Operator[-1], end = '')
                    Operator.pop()
                Operator.append( character)
            else:
                print( character, end = '')
        print('')       
    return 

if __name__ == "__main__":
    main()
    exit(0)