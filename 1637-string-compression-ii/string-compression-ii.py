
from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)

        @lru_cache(None)
        def dp(i, prev, count, k):
            if k < 0:
                return float('inf')

            if i == n:
                return 0

            # Option 1: Delete the current character
            delete = dp(i + 1, prev, count, k - 1)

            # Option 2: Keep the current character
            if s[i] == prev:
                add = 1 if count in (1, 9, 99) else 0
                keep = add + dp(i + 1, prev, count + 1, k)
            else:
                keep = 1 + dp(i + 1, s[i], 1, k)

            return min(delete, keep)

        return dp(0, '', 0, k)
