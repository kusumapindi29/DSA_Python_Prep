'''
Problem : Best Time to buy and sell stocks 2
Platform : Leetcode

Time complexity : O(n)
Space Complexity : O(1)

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # for every consecutive combination, we will sell for high prices and get for low, so in profit we do sell- bought 
        profit =0
        i=1
        while i<len(prices):
            if prices[i]>prices[i-1]:
                profit += prices[i] -prices[i-1]
            i+=1
        return profit
