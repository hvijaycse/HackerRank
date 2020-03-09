if __name__ == "__main__":
    N , X, Y = map( int, input().split())
    Cost = list( map( int, input().strip().split()[:N]))
    Max_cost = 0
    head = 0
    tail = 0
    current_cost = 0
    while True:
        while current_cost < X:
            if head == N:
                break
            current_cost += Cost[head]
            head +=1
        if current_cost > X:
            while current_cost > X:
                current_cost -= Cost[tail]
                tail += 1 
        if current_cost > Max_cost :
            Max_cost = current_cost
        current_cost -= Cost[tail]
        tail +=1
        if head == N:
            break
    final = Max_cost
    while Y - 1:
        Max_cost = Max_cost * 2
        final += Max_cost
        Y = Y - 1
    print( final)