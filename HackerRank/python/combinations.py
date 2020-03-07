from itertools import combinations 

if __name__ == '__main__':
    String, Upto =  input().split()
    Upto = int(Upto)
    String = [i for i in String]
    String.sort()
    for i in range(1, Upto + 1):
        Answers = list( combinations(String, i))
        for ans in Answers:
            print(''.join(ans))
    exit(0)
