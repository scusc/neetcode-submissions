class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # We bought the first stock, so we are "down" that money
        stock_in_pocket = -prices[0] 

        # We haven't sold anything, so no money here
        just_sold_it = 0

        # We start with 0 dollars and haven't done anything
        ready_to_buy = 0

        for i in range(1, len(prices)):
            prev_stock = stock_in_pocket
            prev_sold = just_sold_it
            prev_ready = ready_to_buy

            # Either keep the stock we had, or buy a new one using "Ready" money
            stock_in_pocket = max(stock_in_pocket, prev_ready - prices[i])

            # The only way to sell is if we had a stock in our pocket yesterday
            just_sold_it = prev_stock + prices[i]

            # Either we were already ready, or we just finished our "Just Sold" cooldown
            ready_to_buy = max(prev_ready, prev_sold)

        return max(just_sold_it, ready_to_buy)

        