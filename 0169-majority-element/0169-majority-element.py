class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)//2
        nums.sort()
        return nums[n]
        