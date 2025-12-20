class Solution(object):
    def maxProfit(self, prices):
        Max_profit=0
        for i in range(1,len(prices)):
            if prices[i-1]<prices[i]:
                Max_profit+=prices[i]-prices[i-1]          
        return Max_profit              
