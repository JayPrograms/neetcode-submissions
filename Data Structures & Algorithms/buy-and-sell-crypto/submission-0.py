class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        for i in range(len(prices)):

            for j in range(i + 1, len(prices)):
                maxPrice = max((prices[j] - prices[i]), maxPrice)

        return maxPrice
                    