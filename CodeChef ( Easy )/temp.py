

def getbit( num ):
    setbit = []
    mask = 1
    for pos in range(31, -1, -1):
        if ( mask << pos) & num:
            setbit.append( pos)
    return setbit