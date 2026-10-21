class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)

        while l < r:
            mid = (l + r) // 2
            parts = 1
            curr = 0

            for n in nums:
                if curr + n > mid:
                    parts += 1
                    curr = n
                else:
                    curr += n

            if parts <= k:
                r = mid
            else:
                l = mid + 1

        return l