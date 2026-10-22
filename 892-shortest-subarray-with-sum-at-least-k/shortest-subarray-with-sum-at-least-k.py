class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] + num

        dq = deque()
        answer = n + 1

        for i in range(n + 1):
            while dq and prefix[i] - prefix[dq[0]] >= k:
                answer = min(answer, i - dq.popleft())

            while dq and prefix[dq[-1]] >= prefix[i]:
                dq.pop()

            dq.append(i)

        return answer if answer <= n else -1
