class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit =  0
        profit = 0

        #create a window using l r pointers. start at first index
        #if next num is less than the curr num, move left and right pointer to num

        #if next num is larger than curr num, move right pointer right

        #count profit as you slide

        l = 0
        r = 1

        while l < (len(prices)) and r < (len(prices)):
            if prices[l] > prices[r]:
                l = r
                r = r+1
            else:
                profit = prices[r] - prices[l]
                maxprofit = max(maxprofit, profit)
                r = r+1
        return maxprofit

            


        