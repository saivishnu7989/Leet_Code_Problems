class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i ,j= 0, len(nums)-1

        while(i<j):
            mid=(i+j)//2
            if nums[mid] < nums[mid+1]:
                i=mid+1
            else:
                j=mid
        return i