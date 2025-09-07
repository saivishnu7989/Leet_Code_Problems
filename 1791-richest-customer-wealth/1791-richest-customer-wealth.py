class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        res=0
        s=0
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                s+=accounts[i][j]
            if s>=res:
                res=s
            s=0
        return res

        