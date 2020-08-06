def Int():
    return int( input() )

def List():
    return input().split()

def Ilist():
    return list( map( int, input().split()))

def yes():
    print('YES')

def no():
    print('NO')

def isConsonant(char):
    if char not in 'aeiou':
        return True
    return False
def possiblities( curr_string, remaninng_employes, curr_users):
    ans = 0 
    if remaninng_employes ==0  and len( curr_string) == 0 :
        return 1
    if len( curr_string) < 4:
        return ans
    start = 0
    end = start + 3
    for i in range( end, len( curr_string)):
        curr_user_id = curr_string[start: i + 1]
        if  isConsonant( curr_string[start]) and isConsonant( curr_string[i])  and curr_user_id not in curr_users:
            curr_users.add( curr_user_id)
            ans += possiblities( curr_string[i+1: ], remaninng_employes -1, curr_users)
            curr_users.remove( curr_user_id)
    return ans


def main():
    Employes = Int()
    String = input()
    curr_users = set()
    ans = possiblities( String, Employes, curr_users)
    print( ans )
        

if __name__ == "__main__":
    main()
    exit(0)