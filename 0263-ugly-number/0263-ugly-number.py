class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<1:
            return False
        for pf in [2,3,5]:
            while n%pf==0:
                n//=pf
        return n==1
        
        