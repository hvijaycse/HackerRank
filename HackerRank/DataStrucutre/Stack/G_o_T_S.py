

if __name__ == '__main__':
    games = int( input())
    
    while games:
        games = games - 1
        i = 0
        j = 0
        steps = 0
        SUM = 0
        N, M, Max = map( int, input().split())
        A = list( map(int, input().split() ))    
        B = list( map(int, input().split() ))
        while i < N and SUM + A[i] <= Max :
            SUM = SUM + A[i]
            i = i + 1
        steps = i
        while j < M and i > -1 :
            SUM =  SUM + B[j]
            j = j + 1
            while SUM > Max and i > 0:
                i = i - 1
                SUM = SUM - A[i]
            if SUM <= Max and (i + j) > steps :
                steps = i + j
        
        
        print(steps) 
    exit(0)