class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        l = 0
        z = 0
        m = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                z += 1

            while z > 1:
                if nums[l] == 0:
                    z -= 1
                l += 1

            m = max(m, r - l)

        return m
