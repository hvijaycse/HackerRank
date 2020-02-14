import re

def ARITH():
    expression=input().strip()
    numbers=re.split('\*|\+|\-',expression)
    operator=expression[len(numbers[0])]
    outputs=[]
    biggest=0
    length=len(numbers[0])
    outputs.append( [ length,
                        numbers[0] ] 
                    )
    if biggest<length:
        biggest=length
        
    length=len(numbers[1])+1
    outputs.append( [ length,
                    operator + numbers[1] ]
                    )
    if biggest<length:
        biggest=length
    
    outputs.append( [ biggest ,
                        '-'*biggest ])
    
    # now cheking for operator
    
    if '+' in expression:
        answer=str( int( numbers[0] ) + int( numbers[1] ) )
        length=len(answer)
        
        outputs.append( [ length,
                         answer ] )
        if length>biggest:
            biggest=length
            
    if '-' in expression:
        answer=str( int( numbers[0] ) -  int( numbers[1] ) )
        length=len(answer)
        
        outputs.append( [ length,
                         answer ] )
        if length>biggest:
            biggest=length      
        
    
    if '*' in expression:
        first=int(numbers[0])
        answer=str(first*int(numbers[1]))
        if len(answer)>biggest:
                biggest=len(answer)
        length-=1
        i=0
        while length:
            length-=1
            product=int( numbers[1][length] ) * first
            product=str( product )
            temp_len=len( product)+i
            outputs.append( [ temp_len,
                             product ] )
            if temp_len>biggest:
                biggest=temp_len
            i+=1
        if len( answer[1] ) -1:
            outputs.append( [ biggest,
                            '-'*biggest ] )
            
            outputs.append( [ len(answer),
                            answer ] )
        
    for answer in outputs:
        print( ' '*( biggest - answer[0] ) + answer[1] )
    print('')
    return
            
        
                
            
        
    
    
if __name__=='__main__':
    times=int(input().strip())
    while times:
        ARITH()
        times-=1
    exit(0)