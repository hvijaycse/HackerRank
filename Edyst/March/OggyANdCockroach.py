


def main():
    TestCase = int( input())
    for _ in range( TestCase):
        Data = list( map( int, input().split()))
        N = Data[0]
        Line = Data[1:]
        assert( N == len( Line))
        C = 0
        Index = 1
        Steps = Line[0]
        while Index < N:
            C += 1
            Till = Index + Steps
            New_max = float('-inf')
            for tmp_index in range( Index, min((Till, N))):
                result_step = Line[tmp_index] - ( Till - 1 - tmp_index)
                if result_step >= New_max:
                    New_max = result_step
            Index = Till
            Steps = New_max
        print( C)

if __name__ == "__main__":
    main()
    exit()