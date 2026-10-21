
class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        ans = 0

        for top in range(rows):
            col_sum = [0] * cols

            for bottom in range(top, rows):
                for c in range(cols):
                    col_sum[c] += matrix[bottom][c]

                prefix = 0
                freq = {0: 1}

                for num in col_sum:
                    prefix += num
                    ans += freq.get(prefix - target, 0)
                    freq[prefix] = freq.get(prefix, 0) + 1

        return ans
