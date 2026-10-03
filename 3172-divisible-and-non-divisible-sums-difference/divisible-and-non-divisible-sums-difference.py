class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        r = 0 
        for i in range(1,n+1):
            if i % m == 0:
                r -= i
            else:
                r += i
        return r
