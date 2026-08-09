class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b,s = 0,1
        maxP = 0

        while s < len(prices):
            if prices[s] < prices[b]:
                b = s
            else:
                Profit = prices[s] - prices[b]
                maxP = max(maxP, Profit)
            s+=1
        return maxP