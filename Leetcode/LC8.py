class Solution:
    def myAtoi(self, string: str) -> int:
        Number = [str(i) for i in range(0, 10)]
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)
        string = string.strip()
        i = 0
        Positive = True
        if i < len(string) and (string[i] == '+' or string[i] == '-'):
            if string[i] == '-':
                Positive = False
            i += 1
        num = 0
        while i < len(string) and string[i] in Number:
            num = num*10 + int(string[i])
            i += 1
        if not Positive:
            num *= -1

        if num > INT_MAX:
            return INT_MAX
        elif num < INT_MIN:
            return INT_MIN
        else:
            return num
