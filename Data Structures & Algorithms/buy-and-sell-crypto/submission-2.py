class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b,s = 0,1
        maxP = 0

        while s < len(prices):
            Profit = prices[s] - prices[b]
            if Profit < 0:
                b = s
            maxP = max(maxP, Profit)
            s+=1
        return maxP