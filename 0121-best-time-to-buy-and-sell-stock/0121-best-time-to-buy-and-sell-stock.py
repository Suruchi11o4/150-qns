class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Track the lowest buying price seen so far
            if price < min_price:
                min_price = price
            # Calculate profit if sold today and update max profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit