
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()
        ans = []

        for r in range(len(nums)):
            # Remove indices outside the window
            while dq and dq[0] <= r - k:
                dq.popleft()

            # Remove smaller values from the back
            while dq and nums[dq[-1]] <= nums[r]:
                dq.pop()

            dq.append(r)

            # Add maximum once the first window is complete
            if r >= k - 1:
                ans.append(nums[dq[0]])

        return ans
