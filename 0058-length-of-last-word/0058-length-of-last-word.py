class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        res=""
        for i in range(1,len(s)+1):
            if s[-i] == " ":
                break
            res+=s[-i]
        return len(res)


        