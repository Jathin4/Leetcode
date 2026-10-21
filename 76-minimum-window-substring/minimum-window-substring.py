class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        left = 0
        required = len(t)
        start = 0
        min_len = float('inf')

        for right in range(len(s)):
            c = s[right]

            if need.get(c, 0) > 0:
                required -= 1

            need[c] = need.get(c, 0) - 1

            while required == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                left_char = s[left]
                need[left_char] = need.get(left_char, 0) + 1

                if need[left_char] > 0:
                    required += 1

                left += 1

        return "" if min_len == float('inf') else s[start:start + min_len]