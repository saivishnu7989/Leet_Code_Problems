class Solution(object):
    def isHappy(self, num):
        s=set()
        while num != 1:
            if num in s:
                return False
            s.add(num)
            sum=0
            while(num>0):
                digit=num%10
                sum+=digit**2
                num=num//10
            num=sum
        return num==1