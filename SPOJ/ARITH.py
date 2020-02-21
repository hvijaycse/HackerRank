def Calculate(Expression, Operator):
    Return_String = ""
    output = []
    Index = Expression.index(Operator)
    First = Expression[ : Index ]
    Second = Expression[ Index: ]
    Answer = str(eval(Expression))
    maximum = 0
    for values in [First, Second]:
        Length = len(values)
        output.append((Length, values))
        if Length > maximum:
            maximum = Length
    
    if Operator == '*' and len(Second[1:]) != 1:
        
        dashes = max( len(Second), len( str( eval( 
                                                  Second[-1] +
                                                   '*' +
                                                   First )) ))
        output.append( ( dashes, '-' * dashes ))
        Second = Second[1:]
        Second_Len = len(Second)
        times = Second_Len
        while times:
            Muli = str( eval( Second[ times -1] + 
                             '*' + 
                             First ))
            Muli = Muli + ' ' * ( Second_Len - times )
            current_len = len( Muli)
            output.append( ( current_len, Muli))
            if current_len > maximum:
                maximum =  current_len
            times = times - 1 
        Second = Muli
    dashes = max( len( Second), len(Answer))
    output.append( (dashes, '-' * dashes ))
    output.append( ( len( Answer), Answer))            
    for values in output:
        Return_String += ' ' * (maximum - values[0] ) + values[1] +'\n'
    return Return_String + '\n'
    
            
if __name__=='__main__':
    times=int(input().strip())
    output = ""
    while times:
        Expression = input()
        if '+' in Expression:
            output += Calculate(Expression, '+')
        elif '-' in Expression:
            output += Calculate(Expression, '-')
        else:
            output += Calculate(Expression, '*')
        times-=1
    print(output)
    exit(0)