class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        prev = 0
        for i in range(1, n):
            if nums[i] != nums[prev]:
                prev += 1
                nums[prev] = nums[i]
        return prev + 1
