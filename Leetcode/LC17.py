class Solution:
    Words = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i'],
        ['j', 'k', 'l'],
        ['m', 'n', 'o'],
        ['p', 'q', 'r', 's'],
        ['t', 'u', 'v'],
        ['w', 'x', 'y', 'z']
    ]

    def letterCombinations(self, digits: str) -> [str]:
        Answer = []
        if len(digits) > 0:
            Answer = self.Words[int(digits[0]) - 2]
        for num in digits[1:]:
            tmp_ans = []
            for w in self.Words[int(num) - 2]:
                tmp_ans += [I + w for I in Answer]
            Answer = tmp_ans
        return Answer
