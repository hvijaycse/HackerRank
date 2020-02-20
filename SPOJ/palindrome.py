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
    times = int( stdin.readline().strip() )
    Output = ""
    for t in range(times):
        Number = stdin.readline().strip()
        num = [i for i in Number]
        Length = len(num)
        if num.count('9') == Length:
            Output += '1' + '0'*(Length -1 ) + '1' + '\n'
            continue
        Original_num = list(num)
        Mid_ELement = Length >> 1
        if  Length & 1:
            # numeber is of odd length
            try:
                num[Mid_ELement + 1 : ] = list( reversed( num[ : Mid_ELement]))
            except :
                pass
        else:
            # number is even 
            try:
                num[Mid_ELement : ] = list( reversed( num[ : Mid_ELement]))
            except:
                pass
            Mid_ELement -= 1 
            
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
    exit(0)
                                    
