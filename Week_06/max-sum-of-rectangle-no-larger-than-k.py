class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix)
        if row == 0:
            return 0
        col = len(matrix[0])
        ans = float('-inf')
        for left in range(col):
            row_sum = [0] * row
            for right in range(left, col):
                for i in range(row):
                    row_sum[i] += matrix[i][right]
                sums = [0]
                cur_sum = 0
                for rs in row_sum:
                    cur_sum += rs
                    idx = bisect.bisect_left(sums, cur_sum - k)
                    if idx < len(sums):
                        ans = max(ans, cur_sum - sums[idx])
                    bisect.insort(sums, cur_sum)
        return ans
