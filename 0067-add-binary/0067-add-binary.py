class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        total=int(a,2)+int(b,2)
        return bin(total)[2:]

        