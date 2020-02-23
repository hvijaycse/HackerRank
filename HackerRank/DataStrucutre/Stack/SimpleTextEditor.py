if __name__ == "__main__":
    UndoStack = []
    String = ''
    Cases = int( input())
    while Cases :
        Cases = Cases - 1
        Case = input().strip().split()
        if Case[0] == '1' :
            UndoStack.append( String)
            String += Case[1]
        elif Case[0] == '2' :
            UndoStack.append( String)
            String = String[ :  - int(Case[1])]
        elif Case[0] == '3':
            print( String[ int( Case[1] ) -1 ] )
        else:
            String = UndoStack.pop()
    exit(0)
        
    