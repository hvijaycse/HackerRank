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

def main():
    N = Int()
    T = Int()
    Race = []
    Leads = {}
    Step = []
    for i in range(N):
        Row = Ilist()
        Race.append(Row)
        Leads[i] = 0 
        Step.append( Row[-1])
    Steps_count = [0 for i in range(N)]
    max_lead = 0
    position = 0
    for index in range( T //2):
        max_step = 0
        to_increase = []
        for r in range( N):
            Steps_count[r] += sum(Race[r][position: position + 2])* Step[r]
            if Steps_count[r] > max_step:
                max_step = Steps_count[r]
                to_increase = [r]
            elif Steps_count[r] == max_step:
                to_increase.append(r)
        for i in to_increase:
            Leads[i] += 1
            if Leads[i] > max_lead:
                max_lead = Leads[i]
        position += 2
    answers = []
    for index, lead in Leads.items():
        if lead == max_lead:
            answers.append(index + 1)
    print( min( answers))    


    
            
        

if __name__ == "__main__":
    main()
    exit(0)