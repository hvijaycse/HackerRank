
def Plaindrome( ):
    Number = int(input())
    Number1 = Number
    
    if not Number:
        print('1')
        return 
    
    num =[]
    Length = 0
    while Number:
        num.insert( 0, Number % 10)
        Number = Number // 10 
        Length = Length + 1
    
    if num.count(9) == Length:
        print( Number1 + 2)
        return
     
    Second_Num = list(num)
    Mid_Element = Length >> 1
    
    if Length % 2 == 0:
        Mid_Element = Mid_Element - 1
         
    temp = Mid_Element 
    
    while temp + 1 :
        num[ Length - temp -1]  = num[ temp]
        temp = temp - 1
        
    while num <= Second_Num:
        num[Mid_Element] = num[Mid_Element] + 1
        num[ -Mid_Element -1] = num[Mid_Element]
        temp = Mid_Element
        while num[temp] > 9:
            num[temp] = num[ -temp -1 ] = 0
            num[ temp -1] = num[-temp] = (num[temp -1 ] + 1)
            temp = temp - 1
                              
    for  value in num:
        print(value, end='')
    print('')            
            
if __name__ == "__main__":
    times = int( input())
    while times:
        Plaindrome()
        times = times - 1
    exit(0)