class Solution:
    replace = {
        '(': ')',
        ')': '('
    }

    def rev(self, string):
        return ''.join([self.replace[s] for s in string[::-1]])

    def generateParenthesis(self, n: int) -> [str]:
        if n < 1:
            return []
        sets = [[], ["()"]]

        for i in range(2, n + 1):
            Newsets = set()
            for k in range(1, i // 2 + 1):
                for bracket in sets[i - k]:
                    start = "("*k
                    end = ")"*k
                    a = start + end + bracket
                    b = start + bracket + end
                    Newsets.add(a)
                    Newsets.add(self.rev(a))
                    Newsets.add(b)
                    Newsets.add(self.rev(b))
            for k in range(1, i//2 + 1):
                for start in sets[k]:
                    for end in sets[i - k]:
                        Newsets.add(start + end)
                        Newsets.add(end + start)
                        Newsets.add(self.rev(start + end))
                        Newsets.add(self.rev(end + start))
            sets.append(list(Newsets))
        return sets[n]
