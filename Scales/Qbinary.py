def solve2(A, B):
    Answers = []
    for Query in B:
        L, R = Query
        L -= 1
        R -= 1
        ans = 0
        while L < R:
            if A[L] != '1': L += 1
            if A[R] != '1': R -= 1
            if A[L] == '1' and A[R] == '1':
                break
        if L != R:
            ans = A[L:R].count('0')
        Answers.append(ans)
    return Answers