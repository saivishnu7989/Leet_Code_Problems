class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        max=(2**31)-1
        min=-2**31
        if x>max or x<min :
            return False
        res=0
        temp=x
        if x<0:
            x=x*-1
        
        while x!=0:
            digit=x%10
            res=res*10+digit
            x=x//10
        if res==temp:
            return True
        else:
            return False
        