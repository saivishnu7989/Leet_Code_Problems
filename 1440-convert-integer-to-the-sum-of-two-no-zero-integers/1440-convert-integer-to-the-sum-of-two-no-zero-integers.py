class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(1,n):
            j=n-i
            if self.is_zero(i) and self.is_zero(j):
                return [i,j]
        return []
    def is_zero(self,k):
        return "0" not in str(k)
        