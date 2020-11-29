class Solution:
    def jump(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return 0
        des = size - 1
        cur, pre = 0, 0
        nJump = 0
        for i in range(size):
            cur = max(cur, i + nums[i] )
            if i == pre:
                pre = cur
                nJump += 1
                if cur >= des:
                    return nJump
        return nJump
