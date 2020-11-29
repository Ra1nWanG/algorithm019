class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        l = len(prices)
        if l < 2:
            return 0 
        '''
        for i in range(1, l):
            if prices[i] > prices[i - 1]:
                ans += (prices[i] - prices[i - 1])
        return ans
        '''
        dp0, dp1 = 0, -prices[0]
        for i in range(1, l):
            dp0 = max(dp0, dp1 + prices[i])
            dp1 = max(dp1, dp0 - prices[i])
        return dp0
