class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        maximum = float('-inf')

        for i in range(len(prices)):
            profit = prices[i] - minimum
            if(profit > maximum):
                maximum = profit
            if(prices[i] < minimum):
                minimum = prices[i]                                                 

            return maximum
                                                                                                                                                        
