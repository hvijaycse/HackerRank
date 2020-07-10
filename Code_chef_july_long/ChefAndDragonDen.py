
def main():
    N, Q = map( int, input().split())
    H = list( map( int, input().split() ) )
    A = list( map( int, input().split() ) )
    while Q:
        Q  -= 1
        Choice, Start, End = map( int, input().split())
        if Choice == 1:
            A[ Start - 1] = End
        else:
            Start = Start - 1
            End = End - 1
            if H[ Start ] <= H[End]:
                print(- 1)
            else:
                Maximum_Taste = 0
                Start_Height = H[ Start]
                Index_stack = [ Start]
                if Start == End:
                    Maximum_Taste = A[ Start]
                elif Start > End:
                    i = Start -1 
                    while i >= End:
                        if H[i] >= Start_Height:
                            Maximum_Taste = -1
                            break
                        else:
                            while H[i] >= H[ Index_stack[ - 1]]:
                                Index_stack.pop()
                            Index_stack.append( i )
                        i -= 1
                else:
                    i = Start + 1
                    while i <= End:
                        if H[i] >= Start_Height:
                            Maximum_Taste = -1
                            break
                        else:
                            while H[i] >= H [ Index_stack[-1] ]:
                                Index_stack.pop()
                            Index_stack.append( i)
                        i += 1
                if Maximum_Taste != -1:
                    for index in Index_stack:
                        Maximum_Taste += A[ index]
                print( Maximum_Taste)
if __name__ == "__main__":
    main()
    exit(0)