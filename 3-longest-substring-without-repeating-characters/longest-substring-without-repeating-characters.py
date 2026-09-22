class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {} 
        a = 0
        l = 0 
        for r in range(len(s)):
            c = s[r]
            if c in seen and seen[c]>=l:
                l = seen[c]+1
            seen[c] = r
            size = r-l+1
            if size > a:
                a = size

        return a
