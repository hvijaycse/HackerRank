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


def VowelCount(string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    vc = 0
    for v in vowel:
        vc += string.count(v)
    return vc


def getVowles():
    one = ('one', 'two', 'three', 'four', 'five',
           'six', 'seven', 'eight', 'nine')
    tens = ('ten', 'twenty', 'thirty', 'forty', 'fifty',
            'sixty', 'seventy', 'eighty', 'ninety')
    eleven = ('eleven', 'twelve', 'thirteeen', 'fourteen', 'fifteen',
              'sixteen', 'seventeen', 'eighteen', 'nineteen')
    V_count = {}

    for number in range(1, 101):
        if number < 10:
            word = one[number - 1]
        elif number == 10:
            word = 'ten'
        elif number < 20:
            word = eleven[number - 11]
        elif number < 100:
            word = tens[number // 10 - 1]
            if number % 10 > 0:
                word += one[number % 10 - 1]
        else:
            word = 'hundred'
        V_count[number] = VowelCount(word)
    return V_count


def main():
    Vdict = getVowles()
    N = Int()
    Numbers = Ilist()
    total_vowels = 0
    for number in Numbers:
        total_vowels += Vdict[number]
    Final_sets = []
    Numbers.sort()
    back = 0
    ahead = 0
    tmp_sum = 0
    print( total_vowels)
    while True:
        while ahead < N  and tmp_sum < total_vowels:
            tmp_sum += Numbers[ahead]
            ahead += 1
        if tmp_sum == total_vowels:
            if Numbers[back : ahead] not in Final_sets:
                Final_sets.append(Numbers[back: ahead])
            ahead += 1
            back += 1
        while back < N and tmp_sum > total_vowels:
            tmp_sum -= Numbers[back]
            back += 1
        if tmp_sum == total_vowels:
            if Numbers[back : ahead] not in Final_sets:
                Final_sets.append(Numbers[back: ahead])
            ahead += 1
            back += 1
        if ahead == N or back == N:
            break

    print(len(Final_sets))


if __name__ == "__main__":
    main()
    exit(0)
