class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        m = 0
        freq = {}

        for r in range(len(fruits)):
            freq[fruits[r]] = freq.get(fruits[r], 0) + 1

            while len(freq) > 2:
                freq[fruits[l]] -= 1
                if freq[fruits[l]] == 0:
                    del freq[fruits[l]]
                l += 1

            m = max(m, r - l + 1)

        return m