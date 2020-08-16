# cook your dish here
def Int():
    return int(input())


def List():
    return input().split()


def Ilist():
    return list(map(int, input().split()))


def yes():
    print('YES')


def no():
    print('NO')


def getEff(Relative, K):
    # if K == 1:
    #     Final = []
    #     tmp = {}
    #     for r in Relative:
    #         if r not in tmp:
    #             tmp[r] = 1
    #         else:
    #             Final.append(tmp)
    #             tmp = {
    #                 r: 1
    #             }
    #     if tmp:
    #         Final.append(tmp)
    #     Answer = len(Final)
    # else:
    Answers = {}
    Indexes = {}
    # Start = 0
    # end = len(Relative)
    Stacks = [(0, len(Relative))]
    # a = 1
    while Stacks:
        # a = 0
        SE = Stacks[-1]
        Founded = True
        if SE not in Answers:
            Founded = False
            start = SE[0]
            end = SE[1]
            # DIS = []
            LEFT = {}
            RIGHT = {}
            LEFTF = 0
            RIGHTF = 0
            # for Rel in Relative[start: end]:
            for index in range(start, end):
                Rel = Relative[index]
                if Rel not in LEFT:
                    LEFT[Rel] = 1
                else:
                    LEFT[Rel] += 1
                    if LEFT[Rel] == 2:
                        LEFTF += 2
                    else:
                        LEFTF += 1
            if LEFTF < 2*K:
                Answers[SE] = K + LEFTF
                Founded = True
            else:
                # min_ans = float('inf')
                if SE not in Indexes:
                    DIS = []
                    Min_fight = LEFTF
                    # print( Relative[start:end ])
                    for index in range(end - 1, start - 1, -1):
                        Rel = Relative[index]
                        if Rel not in RIGHT:
                            RIGHT[Rel] = 1
                        else:
                            RIGHT[Rel] += 1
                            if RIGHT[Rel] == 2:
                                RIGHTF += 2
                            else:
                                RIGHTF += 1

                        if LEFT[Rel] > 2:
                            LEFTF -= 1
                        elif LEFT[Rel] == 2:
                            LEFTF -= 2
                        LEFT[Rel] -= 1

                        if LEFTF + RIGHTF < Min_fight:
                            DIS = [index]
                            Min_fight = LEFTF + RIGHTF
                        elif LEFTF + RIGHTF == Min_fight:
                            DIS.append(index)
                        # print( Rel, LEFTF, RIGHTF)
                    Indexes[SE] = DIS
                DIS = Indexes[SE]

                for index in DIS:
                    Both_present = True
                    SE1 = (start, index)
                    SE2 = (index + 1, end)
                    if SE1 not in Answers:
                        Stacks.append(SE1)
                        Both_present = False
                    if Both_present and SE2 not in Answers:
                        Stacks.append(SE2)
                        Both_present = False
                    if not Both_present:
                        break
                if Both_present:
                    min_value = float('inf')
                    for index in DIS:
                        SE1 = (start, index)
                        SE2 = (index + 1, end)
                        if Answers[SE1] + Answers[SE2] < min_value:
                            min_value = Answers[SE1] + Answers[SE2]
                    Answers[SE] = min_value
                    Founded = True
                else:
                    Founded = False
        # print( Answers, Stacks, Indexes)
        if Founded:
            Stacks.pop()
    # print( Answers)
    Answer = Answers[SE]
    return Answer

def getEff2(Relative, K):
    if K == 1:
        Final = []
        tmp = {}
        for r in Relative:
            if r not in tmp:
                tmp[r] = 1
            else:
                Final.append(tmp)
                tmp = {
                    r: 1
                }
        if tmp:
            Final.append(tmp)
        Answer = len(Final)
    else:
        DIS = []
        LEFT = {}
        RIGHT = {}
        LEFTF = 0
        RIGHTF = 0
        for Rel in Relative:
            if Rel not in LEFT:
                LEFT[Rel] = 1
            else:
                LEFT[Rel] += 1
                if LEFT[Rel] == 2:
                    LEFTF += 2
                else:
                    LEFTF += 1
        if LEFTF < 2*K:
            Answer = K + LEFTF
        else:
            Min_fight = LEFTF
            min_answer = float('inf')
            for index in range(len(Relative) - 1, -1, -1):
                Rel = Relative[index]
                if Rel not in RIGHT:
                    RIGHT[Rel] = 1
                else:
                    RIGHT[Rel] += 1
                    if RIGHT[Rel] == 2:
                        RIGHTF += 2
                    else:
                        RIGHTF += 1

                if LEFT[Rel] > 2:
                    LEFTF -= 1
                elif LEFT[Rel] == 2:
                    LEFTF -= 2
                LEFT[Rel] -= 1

                if LEFTF + RIGHTF < Min_fight:
                    DIS = [index]
                elif LEFTF + RIGHTF == Min_fight:
                    DIS.append(index)

            for index in DIS:
                AI = getEff2(Relative[:index], K) + getEff2(Relative[index:], K)
                if AI < min_answer:
                    min_answer = AI
            Answer = min_answer
    return Answer


def main():
    TestCase = Int()
    for _ in range(TestCase):
        _, K = Ilist()
        Relative = Ilist()
        print(getEff(Relative, K))


if __name__ == "__main__":
    main()
    exit(0)
