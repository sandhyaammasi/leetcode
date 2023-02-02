class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            if (max(prices[(i+1):len(prices)]) - prices[i] > profit):
                profit = max(prices[(i+1):len(prices)]) - prices[i] 
        return profit