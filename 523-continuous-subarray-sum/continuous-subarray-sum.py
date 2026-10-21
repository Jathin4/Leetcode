
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        p = 0
        s = {0: -1}

        for i, num in enumerate(nums):
            p += num

            r = p if k == 0 else p % abs(k)

            if r in s:
                if i - s[r] >= 2:
                    return True
            else:
                s[r] = i

        return False
