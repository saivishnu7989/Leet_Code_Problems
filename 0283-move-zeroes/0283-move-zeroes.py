class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                nums[k]=nums[i]
                k+=1
        while(k<len(nums)):
            nums[k]=0
            k+=1
        return nums
        
        