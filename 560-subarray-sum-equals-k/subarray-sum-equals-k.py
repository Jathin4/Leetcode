class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        p = 0
        c = 0
        f = {0:1}
        for i in nums:
            p += i
            c += f.get(p-k,0)
            f[p] = f.get(p,0)+1
        return c