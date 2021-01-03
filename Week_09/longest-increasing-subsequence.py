class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        tails = [float('-inf')]
        for num in nums:
            if num > tails[-1]:
                tails += [num]
            else:
                i, j = 0, len(tails) - 1
                while i < j:
                    m = i + (j - i) // 2
                    if tails[m] < num:
                        i = m + 1
                    else:
                        j = m
                tails[i] = num
        return len(tails) - 1
