class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        p = [0]

        for num in arr:
            p.append(p[-1] ^ num)

        a = []

        for l, r in queries:
            a.append(p[r + 1] ^ p[l])

        return a
