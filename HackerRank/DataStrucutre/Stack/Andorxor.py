
if __name__ == "__main__":
    Enties = int( input())
    Values = list( map( int, input().split() ))
    s1_max = Values[0] ^ Values[1]
    stack = []
    for value in Values:
        while stack:
            top = stack[-1]
            s1 = value ^ top
            if s1 > s1_max:
                s1_max = s1
            if value < top:
                stack.pop()
            else:
                break
        stack.append(value)    
    print( s1_max)
        
            
    
         

