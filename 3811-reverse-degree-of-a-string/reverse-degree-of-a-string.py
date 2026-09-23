class Solution:
    def reverseDegree(self, s: str) -> int:
        r = 0
        k = 1
        for i in range(len(s)):
            r += k*(123-ord(s[i]))
            k += 1
        return r