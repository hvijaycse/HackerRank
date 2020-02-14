Operators = ['+','-','/','*','^']

def ONP( Expression):
    global Operators
    Stack = []
    Operator = []
    for character in Expression:
        if character in Operators:
            Operator.append( character)
        elif character == ')':
            oprands = []
            Operate = Operator.pop()
            while Stack[-1] != '(':
                oprands.append( Stack.pop())
            Stack.pop()
            oprands.reverse()
            Stack.append( ''.join( oprands) +
                        Operate)
        else:
            Stack.append( character)
    
    return Stack.pop()

if __name__ == "__main__":
    Cases = int( input().strip())
    while Cases:
        Cases = Cases -1
        Expression =  input()
        print( ONP( Expression))
    exit( 0)
        