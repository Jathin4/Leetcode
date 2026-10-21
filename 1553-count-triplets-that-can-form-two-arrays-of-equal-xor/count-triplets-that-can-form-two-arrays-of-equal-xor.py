class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        c = {0: 1}
        t = {0: 0}
        p = 0
        a = 0

        for i, num in enumerate(arr, start=1):
            p ^= num

            a += c.get(p, 0) * (i - 1) - t.get(p, 0)

            c[p] = c.get(p, 0) + 1
            t[p] = t.get(p, 0) + i

        return a
