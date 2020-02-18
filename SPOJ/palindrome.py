
from time import perf_counter as  time
from sys import stdout, stdin

Changers = {
    '0':'1',
    '1':'2',
    '2':'3',
    '3':'4',
    '4':'5',
    '5':'6',
    '6':'7',
    '7':'8',
    '8':'9',
    '9':'0'
}

if __name__ ==  "__main__":
    # times = int( stdin.readline().strip() )
    file = open('palindrome_testcase.txt','r')
    times = int(file.readline().strip())
    Output = ""
    Start = time()
    for t in range(times):
        # Number = int( stdin.readline().strip())
        Number = int( file.readline().strip())
        if not Number:
            Output += '1\n'
            continue
        num = [i for i in str(Number)]
        Length = len(num)
        if num.count('9') == Length:
            Output += str( Number + 2) + '\n'
            continue
        Mid_ELement = Length >> 1
        if  not Length & 1:
            Mid_ELement -= 1
        Original_num = list(num)
        temp = 0
        while temp <= Mid_ELement:
            num[ -temp - 1] = num[temp]
            temp += 1
        if num <= Original_num:
            temp = Mid_ELement
            num[temp] = Changers[ num[temp] ]
            num[-temp -1] = num[temp]
            while num[temp] == '0':
                temp -= 1
                num[temp] = Changers[ num[temp] ]
                num[-temp -1] = num[temp]
        Output += ''.join(num) + '\n'
    stdout.write(Output)
    End = time()
    stdout.write('Time taken = '+ str( End - Start))
    exit(0)
                                        