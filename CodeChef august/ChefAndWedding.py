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


def getminjoin(Seperated,K,key, Dicts ):
    if key not in Dicts:
        if len( Seperated) == 1:
            dict_count = {}
            for r in Seperated[0]:
                if r not in dict_count:
                    dict_count[r] = 1
                else:
                    dict_count[r] += 1
            Dicts[key] = K + sum( [i for i in dict_count.values() if i >1])
        else:
            Dicts[key] = 0
            for sep in Seperated:
                dict_count = {}
                for r in sep:
                    if r not in dict_count:
                        dict_count[r] = 1
                    else:
                        dict_count[r] += 1
                Dicts[key] += K + sum([ i for i in Dicts.values() if i > 1])
            for i in range( len( Seperated) -1):
                tmp_key = key[:i] + str( int( key[i] )+ int(key[i+1])) +key[i+2:]
                tmp_join = Seperated[:i]+ [Seperated[i]+ Seperated[i+1]]+ Seperated[i+2:]
                Dicts[key] = min(
                    Dicts[key],
                    getminjoin( tmp_join, K, tmp_key, Dicts)
                )
    return Dicts[key]

def wed(Relative, K):
    Seperated = []
    tmp_array = []
    for r in Relative:
        if r not in tmp_array:
            tmp_array.append(r)
        else:
            Seperated.append(tmp_array)
            tmp_array = [r]
    if tmp_array:
        Seperated.append(tmp_array)
    if K == 1:
        return len( Seperated )
    key = ''.join( [str(i) for i in range(1, len(Seperated) + 1)] )
    return getminjoin( Seperated,K, key, {})
    

def main():
    TestCase = Int()
    for _ in range(TestCase):
        _, K = Ilist()
        Relative = Ilist()
        print(wed( Relative,K))


if __name__ == "__main__":
    main()
    exit(0)
