class Solution:
    def isValid(self, string: str) -> bool:
        Stack = ['']
        poper = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for s in string:
            if s not in poper:
                Stack.append(s)
            elif Stack[-1] == poper[s]:
                Stack.pop()
            else:
                break
        if Stack[1:]:
            return False
        else:
            return True
