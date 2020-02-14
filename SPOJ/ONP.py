operator=['+', '-', '*', '/', '^']
precd={'+':0,'-':1,'*':2,'/':3,'^':4}

def ONP(expression):
    stack=[]
    pos_expression=[]

    for char in expression:
        if char in operator:
            while stack and precd[stack[-1]>=precd[char]:
                pos_expression.append(stack.pop)
            
        
        elif char==")":
            while stack[-1]!='(':
                pos_expression.append(stack.pop())
            stack.pop()
        
        elif char=="(":
            stack.append('(')
        else:
            pos_expression.append(char)
    
    return ''.join(pos_expression)
     

if __name__=="__main__":
    times=int(input())
    while times:
        expression=input()
        print(ONP(expression))
        times=times-1