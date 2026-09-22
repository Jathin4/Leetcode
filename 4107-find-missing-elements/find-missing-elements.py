class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = min(nums)
        l = max(nums)
        r = []
        for i in range(s,l+1):
            if i not in nums:
                r.append(i)
        return r