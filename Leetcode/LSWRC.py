

# LEET CODE TEMPLATE

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        tmp_string = ''
        for char in s:
            if char not in tmp_string:
                tmp_string += char
            else:
                if len( tmp_string) > maxlen:
                    maxlen = len( tmp_string)
                tmp_string = tmp_string[ tmp_string.index(char) + 1:] + char
        if len( tmp_string ) > maxlen:
            maxlen = len( tmp_string)
        return maxlen