'''
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if sorted(prices, reverse=True) == prices:
            return 0
        
        #3 options, buy sell or skip
        #Compare every day to the day before it, if the day before was lower buy, else we skip
        p = 0
        for i in range(1, len(prices)):
            curr = prices[i]
            prev = prices[i-1]
            if curr > prev:
                p += abs(curr - prev)
        return p
            
            
            
