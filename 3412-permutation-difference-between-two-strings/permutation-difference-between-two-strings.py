class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        h = {}
        for i in range(len(s)):
            h[s[i]] = i
        r = 0
        for i in range(len(t)):
            r += abs(i - h[t[i]])
        return r