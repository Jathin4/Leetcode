class Solution:
    def maxFreqSum(self, s: str) -> int:
        h = {}
        for i in range(len(s)):
            h[s[i]] = h.get(s[i],0)+1
        a = 0
        c = 0
        for k,v in h.items():
            if k in 'aeiou':
                if v > a:
                    a = v
            else:
                if v > c:
                    c = v
        return c+a



        