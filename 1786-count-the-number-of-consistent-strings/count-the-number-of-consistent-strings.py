class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = 0
        for i in words:
            for j in i:
                if j not in allowed:
                    c += 1
                    break
        return len(words)-c