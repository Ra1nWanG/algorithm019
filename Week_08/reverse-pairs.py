class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        tb, res = [], 0
        for n in reversed(nums):
            res += bisect.bisect_left(tb, n)
            n2 = n * 2
            idx = bisect.bisect_left(tb, n2)
            tb.insert(idx, n2)
        return res
