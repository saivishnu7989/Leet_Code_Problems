class Solution(object):
    def mySqrt(self, x):
        if x<2:
            return x
        a,b=0,x
        result=0
        while a<=b:
            mid= (a+b) //2
            if mid*mid ==x:
                return mid
            elif mid*mid<x:
                result=mid
                a=mid+1
            else:
                b=mid-1
        return result