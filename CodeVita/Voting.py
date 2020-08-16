N = int(input())
Voters = input() + 'B'
lastVoters = 'A'
A_Count = 0
B_count = 0
Index = 0
while Index < N + 1:
    v = Voters[Index]
    # print(v)
    if v != '-':
        lastVoters = v
        if v == 'A':
            A_Count += 1
        else:
            B_count += 1
    else:
        DashCount = 0
        while Voters[Index] == '-':
            DashCount += 1
            Index += 1
        nextVoter = Voters[Index]
        if lastVoters == nextVoter:
            if lastVoters == 'A':
                A_Count += DashCount
            else:
                B_count += DashCount
        elif lastVoters == 'B' and nextVoter == 'A':
            A_Count += DashCount // 2
            B_count += DashCount //2
        if nextVoter == 'A':
            A_Count += 1
        else:
            B_count += 1
        lastVoters = nextVoter
    Index += 1
# print(A_Count, B_count)
B_count -= 1
if A_Count == B_count:
    print('Coilation')
elif A_Count > B_count:
    print('A')
else:
    print('B')