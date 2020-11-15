class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        dic = {}
        for i in range(l):
            if not dic.get(target - nums[i]) == None:
                return [dic.get(target - nums[i]), i]
            dic[nums[i]] = i
        return []

# Usage of dictionary/hashmap and dict.get function
