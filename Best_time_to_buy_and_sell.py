class Solution(object):
    def maxProfit(self, prices):
        Max_profit=0
        Min_price=float('inf')
        for i in prices:
            if i<Min_price:
                Min_price=i
            else:
                profit=i-Min_price    
              
                if profit>Max_profit:
                    Max_profit=profit
        
        return Max_profit

obj=Solution()
prices=[7,1,5,3,6,4]
print(obj.maxProfit(prices))
        
