class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        r = 0
        for i in nums:
            if i %2 == 0:
                r += 1
        return [0]*r + [1]*(len(nums)-r)