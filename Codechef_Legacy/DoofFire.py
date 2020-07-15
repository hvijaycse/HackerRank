

def main():
    TestCase = int( input() )
    while TestCase:
        TestCase -= 1
        String = input()
        length = len( String)
        Query = int( input())
        Queries = list( map( int, input().split() ) )[ : Query]
        ans = []
        tmp = []
        for s in String:
            if s == '(':
                tmp.append(1)
            else:
                tmp.append(0)
        for Start in Queries:
            Start -= 1
            while Start < length and  not(tmp[Start]) :
                Start += 1
            if  Start < length and tmp[ Start]:
                Stack = 1
                Start += 1
                while Start < length and Stack:
                    if tmp[Start] :
                        Stack += 1
                    else:
                        Stack -= 1
                    Start += 1
                if Stack:
                    ans.append('-1')
                else:
                    ans.append( str( Start))

            else:
                ans.append('-1')
        print('\n'.join( ans))

if __name__ == "__main__":
    main()
    exit(0)