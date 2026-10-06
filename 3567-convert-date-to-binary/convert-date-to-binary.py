class Solution:
    def convertDateToBinary(self, date: str) -> str:
        r = ""
        d = date.split('-')
        l = len(d)
        for i in range(l):
            a = bin(int(d[i]))[2:]
            r += str(a)
            if i != l-1:
                r += '-'
        return r
