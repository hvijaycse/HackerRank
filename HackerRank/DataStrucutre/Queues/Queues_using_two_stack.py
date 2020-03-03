# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    Stack1 = []
    Stack2 = []
    Queries = int( input())
    After = []
    while Queries:
        Query = input().split()
        if Query[0] == '1':
            Stack2.append( Query[1])
        else:
            After.append(Query[0])
        Queries = Queries - 1
    while Stack2:
        Stack1.append( Stack2.pop())
    for query in After:
        if query == '2':
            Stack1.pop()
        else:
            print( Stack1[-1])
    
