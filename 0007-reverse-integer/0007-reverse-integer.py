class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        min,max=-2**31,(2**31)-1
        res=0
        if x>0:
            while x!=0:
                digit=x%10
                res=res*10+digit
                x=x//10
        elif x<0:
            x=x*-1
            while x!=0:
                digit=x%10
                res=res*10+digit
                x=x//10
            res=res*-1
        else:
            return 0
        if res>max or res<min:
            return 0
        return res
        