
def primerange( n1, n2 ):
    prime = [True] *( n2 + 1)
    prime[1] = False
    for i in range( 2, int( n2**0.5) + 1 ):
        if prime[i]:
            a = i*i
            while a <= n2:
                prime[a] = False
                a = a + i
    primels = []
    for i in range(n1, n2 + 1):
        if prime[i]:
            primels.append( i)
    return primels

def Check_Prime( Num):
    for i in range(2, int(Num ** 0.5) + 2):
        if Num % i == 0:
            return False
    return True

def main():
    n1, n2 = map( int, input().split())
    primels = primerange(n1, n2)
    combinations = []
    for index, value in enumerate( primels):
        InnerLs = primels[: index] + primels[index + 1: ]
        for value2 in InnerLs:
            tmp = int( str( value) + str(value2))
            combinations.append(tmp)
    combinations = list( set( combinations))
    count = 0
    prime_ls = []
    for comb in combinations:
        if Check_Prime(comb):
            prime_ls.append( comb)
    count= len( prime_ls)
    prime_ls.sort()
    min_prime = prime_ls[0]
    max_prime = prime_ls[-1]
    if count <3:
        if count == 1:
            print( min_prime)
        else:
            print( max_prime) 
    else:           
        count -= 2
        while count:
            count -= 1
            tmp = max_prime
            max_prime = max_prime + min_prime
            min_prime = tmp
        print( max_prime)
                               

if __name__ == "__main__":
    main()
    exit(0)