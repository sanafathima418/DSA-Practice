# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = float('inf')
        maxProfit = 0
        
        # An entry in the array can either be
        # 1. The minimum price seen so far
        # 2. Can give the best profit 
        
        # After traversing the array, return the last value of max price
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif (prices[i] - minPrice) > maxProfit:
                maxProfit = prices[i] - minPrice
        return maxProfit
        