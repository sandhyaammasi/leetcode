class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n==1):
            return 1
        prev = 1
        x = 1

        for i in range(n):
            if i > 0:
                ans = prev + x
                x = prev
                prev = ans
        return ans

        
                