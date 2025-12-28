class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i in range(0,len(nums)):
            diff = target - nums[i]
            if diff in d:
                return [i,d[diff]]
            d[nums[i]]=i

        return []
        