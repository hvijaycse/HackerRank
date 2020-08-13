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


def AddDict(Dict1, Dict2):
    tmp_dict = {}
    for k, v in Dict1.items():
        tmp_dict[k] = v
    for k, v in Dict2.items():
        if k in tmp_dict:
            tmp_dict[k] += v
        else:
            tmp_dict[k] = v
    return tmp_dict


def GetJoined(CD, K, Key, VD):
    DKey = ''.join(Key)
    if DKey not in VD:
        if len(CD) == 1:
            VD[DKey] = K + sum([f for f in CD[0].values() if f > 1])
        else:
            VD[DKey] = 0
            for count in CD:
                VD[DKey] += K + sum([r for r in count.values() if r > 1])
            for I in range(0, len(CD) - 1):
                tmp_dict = AddDict(CD[I], CD[I + 1])
                tmp_CD = CD[:I] + [tmp_dict] + CD[I+2:]
                tmp_Key = Key[: I] + \
                    [str(int(Key[I]) + int(Key[I+1]))] + Key[I + 2:]
                VD[DKey] = min(
                    VD[DKey],
                    GetJoined(tmp_CD, K, tmp_Key, VD)
                )
    return VD[DKey]


def getEff(Relative, K):
    CD = []
    tmp_dict = {}
    for r in Relative:
        if r not in tmp_dict:
            tmp_dict[r] = 1
        else:
            CD.append(tmp_dict)
            tmp_dict = {
                r: 1
            }
    if tmp_dict:
        CD.append(tmp_dict)
    if K == 1 or len(CD) == 1:
        return K * len(CD)
    Key = [str(i) for i in range(1, len(CD) + 1)]
    return(GetJoined(CD, K, Key, {}))


def main():
    TestCase = Int()
    for _ in range(TestCase):
        _, K = Ilist()
        Relative = Ilist()
        print(getEff(Relative, K))


if __name__ == "__main__":
    main()
    exit(0)
