class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit: sell (later date/bigger index) > buy (smaller date)    
        # two pointer start at origin together
        seen_bought = 0  
        to_sell = 1
        max_profit = 0
        
        while to_sell < len(prices) :     # iterate through the list 
                if prices[seen_bought] > prices[to_sell]:  # compare the value 
                    # max_profit = to_sell - seen_bought 
                    seen_bought += 1
                else:
                    max_profit = max(max_profit, prices[to_sell] - prices[seen_bought])
                    to_sell += 1
        return max_profit