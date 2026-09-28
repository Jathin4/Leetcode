class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c =m=0
        for i in s:
            if i == 'R':
                c += 1
            if i == 'L':
                c -= 1
            if c == 0:
                m += 1
        return m