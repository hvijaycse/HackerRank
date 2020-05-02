
def Gcd( a, b):
    while b:
        a, b = b, a % b
    return a

if  __name__ == '__main__':
    BotCount = int( input())
    Bots_time = list( map( int, input().split()[:BotCount] ))
    Times = int(input())
    gcd = 1
    for bot_time in Bots_time:
        if bot_time != 1:
            gcd = bot_time
            break
    if gcd == 1:
        Time_Total = Times 
    else:
        Time_Total = 1
        for bot_time in Bots_time:
            Time_Total = Time_Total * bot_time
            New_gcd = Gcd( gcd, bot_time)
            if New_gcd != 1 :
                gcd = New_gcd
        Time_Total = ( Time_Total // gcd)* Times
    print( Time_Total % 1000000007 )