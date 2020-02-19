#!/bin/python3


# to determine wether to push aur to pop the stack
Brackets = {
    '[':1,
    '{':1,
    '(':1,
    ']':0,
    '}':0,
    ')':0
}

#this is for replacement while poping so that the matching pair if any opening bracket is found then 
# it can be close as the closing bracket was not ahead so it is reaplced by f, meaning that this cases is a failS
Replace = {
    '}':'{',
    ']':'[',
    ')':'(',
    '{':'F',
    '[':'F',
    '(':'F'
}

# Complete the isBalanced function below.
def isBalanced( Sequnce ):
    global Brackets
    stack = []
    try:
        for character in Sequnce:
            if Brackets[character]:
                stack.append(character)
            else:
                Inbetween = [ Replace[character]]
                Popped = stack.pop()
                while Popped != Inbetween[ -1] :
                    Inbetween.append( Replace[Popped])
                    Popped = stack.pop()
        if stack:
            Return_value = 'NO'
        else:
            Return_value = 'YES'
    except:
        Return_value = 'NO'
    return Return_value    
if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        print( result)

