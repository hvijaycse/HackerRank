def Int():
    return int( input() )

def List():
    return input().split()

def Ilist():
    return list( map( int, input().split()))

def yes():
    print('YES')

def no():
    print('NO')

def Cpattern( String ):
    Pattern = ''
    count = 0
    Char = {}
    for s in String:
        if s not in Char:
            Char[s] = chr(97 + count)
            count += 1
        Pattern += Char[s]
    return Pattern

def main():
    TestCase = Int()
    for _ in range(TestCase):
        Parties = input().split()[1:]
        Voters = input().split()[1:]
        Patterns = {}
        Votes = {}
        for Party in Parties:
            Patterns[ Party ] = Cpattern( Party ) 
            Votes[Party] = 0
        Max_vote = 0
        for Vote in Voters:
            Vpattern = Cpattern( Vote )
            for Party in Parties:
                if Patterns[Party] == Vpattern:
                    Votes[Party] += 1
                    if Votes[Party] > Max_vote:
                        Max_vote = Votes[Party]
        if Max_vote == 0:
            print('stalemate')
        else:
            Answer = []
            for Party in Parties:
                if Votes[Party] == Max_vote:
                    Answer.append( Party )
            Answer.sort()
            print( ' '.join( Answer) )

            

if __name__ == "__main__":
    main()
    exit(0)