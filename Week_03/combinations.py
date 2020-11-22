class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = [x for x in range(1, n + 1)]
        def back(nums_b, tmp):
            if len(tmp) == k:
                res.append(tmp[:])
                return
            for i in range(len(nums_b)):
                if len(tmp) > 0 and nums_b[i] < tmp[-1]:
                    continue
                tmp.append(nums_b[i])
                back(nums_b[:i] + nums_b[i + 1:], tmp)
                tmp.pop()
        back(nums, [])
        return res
