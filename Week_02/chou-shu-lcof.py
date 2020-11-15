class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [0] * n
        res[0] = 1
        p2, p3, p5 = 0, 0, 0
        for i in range(1, n):
            tmp = min(res[p2] * 2, res[p3] * 3, res[p5] * 5)
            if tmp == res[p2] * 2:
                p2 += 1
            if tmp == res[p3] * 3:
                p3 += 1
            if tmp == res[p5] * 5:
                p5 += 1
            res[i] = tmp
        return res[-1]

# Build three pointers and calculate the minimum val for pointer moving
