class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=0
        for i in range(0,len(digits)):
            num=num*10+digits[i]
        num+=1
        lst=[]
        while num>0:
            digit=num%10
            lst.append(digit)
            num=num//10
        return lst[::-1]

        