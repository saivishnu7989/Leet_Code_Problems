class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if n==0:
            return nums1
        k=n-1
        j=(m+n)-1
        i=m-1
        while i>=0 and k>=0:
            if nums1[i]>nums2[k]:
                nums1[j]=nums1[i]
                i-=1
            else:
                nums1[j]=nums2[k]
                k-=1
            j-=1
        while k>=0:
            nums1[j]=nums2[k]
            k-=1
            j-=1
        return nums1
        