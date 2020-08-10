class Solution:
    def getPlain(self, Index, array):
        ans = array[Index][0]*array[Index][1]
        back = Index - 1
        front = Index + 1   
        while back >= 0 and front < len( array):
            if array[back][0] == array[front][0]:
                if array[back][1] == array[front][1]:
                    ans = array[back][0]* array[ back][1] + ans + array[back][0]* array[ back][1] 
                    back -= 1
                    front += 1
                else:
                    minimum = min( array[back][1], array[front][1])
                    ans = array[back][0]* minimum + ans + array[back][0]* minimum
                    break
            else:
                break    
        return ans   

    def longestPalindrome(self, s: str) -> str:
        if len(s) >1:
            array = []
            start = 0
            while start < len( s):
                end = start + 1
                while end < len(s) and s[end] == s[start]:
                    end += 1
                array.append( ( s[start], end - start) )
                start = end
            ans = ''
            for _ in range( array[0][1]):
                ans += array[0][0]
            for Index in range( 1, len( array)):
                tmp_ans = self.getPlain(Index, array)
                if len( tmp_ans) > len( ans):
                    ans = tmp_ans
            return ans 
        else:
            return s
        