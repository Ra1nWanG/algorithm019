class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        left = 0
        right = n 
        while left < right:
            mid = left + (right - left) // 2
            if (nums[mid] < nums[0]) == (target < nums[0]):
                num = nums[mid]
            else:
                if target < nums[0]:
                    num = float("-inf")
                else:
                    num = float("inf")
            if num < target:
                left = mid + 1
            elif num > target:
                right = mid
            else:
                return mid
        return -1
