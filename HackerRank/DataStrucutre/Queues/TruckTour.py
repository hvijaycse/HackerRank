#!/bin/python3

def truckTour(petrolpumps):
    Indexs = []
    Extras = []
    for index, truck in enumerate(petrolpumps):
        Petrol, Km = truck
        Extra = Km - Petrol
        Extras.append( Extra)
        if Extra < 1:
            Indexs.append(index)
    Length = len( Extras)
    for possible_index in Indexs :
        start = possible_index
        Extra = Extras[possible_index]
        possible_index += 1
        while start != possible_index:
            if possible_index == Length:
                possible_index = 0
            Extra = Extra + Extras[ possible_index]
            if Extra > 0 :
                break
            possible_index += 1
        if start == possible_index:
            return possible_index
        else:
            continue

if __name__ == '__main__':
    n = int(input())
    petrolpumps = []
    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))
    result = truckTour(petrolpumps)
    print(result)
    exit(0)
