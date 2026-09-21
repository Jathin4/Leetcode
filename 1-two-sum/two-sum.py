class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        r = {}
        for i in range(len(nums)):
            num = nums[i]
            c = target-num
            if c in r:
                return[r[c],i]
            r[num] = i
        return []
