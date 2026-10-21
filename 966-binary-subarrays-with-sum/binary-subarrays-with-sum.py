class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0: 1}
        s = ans = 0

        for n in nums:
            s += n
            ans += count.get(s - goal, 0)
            count[s] = count.get(s, 0) + 1

        return ans