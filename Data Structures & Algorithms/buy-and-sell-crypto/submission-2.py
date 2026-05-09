class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_prof = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):

                profit = prices[j] - prices[i]

                if profit > 0:
                    max_prof = max(max_prof, profit)
        return max_prof


                

        