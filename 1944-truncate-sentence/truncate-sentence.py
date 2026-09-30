class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        r = s.split()
        return " ".join(r[:k])