
def main():
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        Laddu = 0
        Activities, Origin = input().split()
        for i in range( int( Activities)):
            Activity = input().split()
            if Activity[0] == 'CONTEST_WON':
                rank = int(Activity[1])
                Laddu += 300
                if rank < 20:
                    Laddu += 20 -rank
            elif Activity[0] == 'TOP_CONTRIBUTOR':
                Laddu += 300
            elif Activity[0] == 'BUG_FOUND':
                Laddu += int( Activity[1])
            else:
                Laddu += 50
        if Origin == 'INDIAN':
            Divider = 200
        else:
            Divider = 400
        print( Laddu // Divider)
    return

if __name__ == "__main__":
    main()
    exit(0)