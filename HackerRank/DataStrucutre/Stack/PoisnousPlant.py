from time import clock as time

def Dating( Plants) :
    Days = 0
    List_of_Stacks = []
    # Last_Plant = float('inf')
    Stack = [Plants[0]]
    for Plant in Plants[1:]:
        if Plant <= Stack[-1]:
            Stack.append(Plant)
        else:
            Stack.reverse()
            List_of_Stacks.append(Stack)
            Stack=[Plant]
    Stack.reverse()
    List_of_Stacks.append(Stack)
    Length = len( List_of_Stacks)
    while Length > 1:
        # print('Got ',List_of_Stacks, end = '')
        Days += 1
        i = 1
        while i < Length:
            if List_of_Stacks[i]:
                List_of_Stacks[i].pop()
            i += 1
        while [] in List_of_Stacks:
            List_of_Stacks.remove([])
            Length -= 1
        i = 0
        j = 1
        List_of_Stacks2 = [List_of_Stacks[0]]
        # print(' Middle ',List_of_Stacks, end = '')
        while j < Length:
            if List_of_Stacks2[i][0] >= List_of_Stacks[j][-1]:
                List_of_Stacks2[i] = List_of_Stacks[j] + List_of_Stacks2[i]
            else:
                List_of_Stacks2.append( List_of_Stacks[j])
                i += 1
            j += 1
        List_of_Stacks = List_of_Stacks2
        Length = len( List_of_Stacks)
        # print(' Changed ',List_of_Stacks)
    return Days

if __name__ == "__main__":
    file = open('32400.txt')
    Number = int(file.readline())
    # Number = int( input() )
    # Plants =  list( map(int, input().split() ) )
    Plants =  list( map(int, file.readline().split() ) )
    # Max_Days = 0
    # Plants.reverse()
    # Before = Plants.pop()
    # start = time()
    Days = Dating( Plants)
    print(Days)
    # end = time()
    # print('Time taken = ',(end - start))