class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        w = sum(nums[:k])
        m = w
        for i in range(k,len(nums)):
            w += nums[i] - nums[i-k]
            m = max(m,w)
        return m/k 