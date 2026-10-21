
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        seen = set()

        for length in range(1, n // 2 + 1):
            for i in range(n - 2 * length + 1):
                mid = i + length
                end = mid + length

                if text[i:mid] == text[mid:end]:
                    seen.add(text[i:end])

        return len(seen)
