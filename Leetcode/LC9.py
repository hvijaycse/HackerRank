class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev = 0
        tmpx = x
        while tmpx:
            rev = rev * 10 + tmpx % 10
            tmpx = tmpx // 10
        if rev == x:
            return True
        else:
            return False
