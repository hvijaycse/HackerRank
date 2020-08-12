class Solution:

    def GetRoman(self, Number, Div, Great='',  Big='', Small=''):
        Roman = ''
        if Number // Div:
            Hun = Number // Div
            if Hun == 9:
                Roman += Small + Great
            elif Hun >= 5:
                Roman += Big + Small*(Hun % 5)
            elif Hun == 4:
                Roman += Small + Big
            else:
                Roman += Small * Hun
        return Roman

    def intToRoman(self, num: int) -> str:
        Roman = ''
        Roman += self.GetRoman(num, 1000, Small='M')
        num = num % 1000
        Roman += self.GetRoman(num, 100, Great='M', Big='D', Small='C')
        num = num % 100
        Roman += self.GetRoman(num, 10, Great='C', Big='L', Small='X')
        num = num % 10
        Roman += self.GetRoman(num, 1, Great='X', Big='V', Small='I')
        return Roman
