

def main():
    N = int( input())
    Bride = input()
    Grooom = input()
    Bride_dict = {
        'r' : 0,
        'm' : 0
    }
    Groom_dict = {
        'r' : 0,
        'm' : 0
    }
    for b in Bride:
        Bride_dict[b] += 1
    for g in Grooom:
        Groom_dict[g] += 1
    i = 0 
    while i < N:
        b = Bride[i]
        if not Groom_dict[b]:
            break
        Groom_dict[b] -= 1
        i += 1
    print( N - i )
if __name__ == "__main__":
    main()
    exit(0)