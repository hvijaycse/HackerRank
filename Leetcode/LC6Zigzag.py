class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows ==1:
            return s

        Ans = ''.join( [s[i] for i in range(0,len(s), 2*(numRows - 1))])
        Index = []
        i =1 
        while i < len(s) + numRows - 1:
            Index.append(i)
            i = i + 2*( numRows - 2)
            if i < len(s) + numRows -1:
                Index.append(i)
            i += 2
        for _ in range( numRows-2):
            Ans += ''.join([ s[i] for i in Index if i < len(s)])
            for i in range(0, len(Index),2):
                Index[i] += 1
            for i in range(1, len(Index),2):
                Index[i] -= 1
        Ans += ''.join( [s[i] for i in range(numRows-1,len(s), 2*(numRows - 1))])
        return Ans
        

