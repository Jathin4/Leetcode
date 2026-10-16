class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        w = 0
        m = 0
        f = {}

        for i in range(len(nums)):
            w += nums[i]
            f[nums[i]] = f.get(nums[i], 0) + 1

            if i >= k:
                w -= nums[i-k]
                f[nums[i-k]] -= 1

                if f[nums[i-k]] == 0:
                    del f[nums[i-k]]

            if i >= k-1 and len(f) == k:
                m = max(m, w)

        return m