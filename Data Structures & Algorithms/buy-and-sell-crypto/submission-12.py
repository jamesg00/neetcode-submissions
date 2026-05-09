class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        profit = 0

        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                sell = prices[j]

                profit = max(profit, sell-buy)
        return profit 
        '''

        #O(n^2) Time O(1) Space 

        #Two Pointer Approach
        l,r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        return max_profit


        



        #O(n) Time || O(1) Space 
                


        



#   i j
#   0 1 2 3 4 5               
# [10,1,5,6,7,1]
        