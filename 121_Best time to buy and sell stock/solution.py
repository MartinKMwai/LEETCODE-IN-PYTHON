class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #initialize the left and right pointers
        left = 0
        #initialize our maximum profit which is 0 right now
        maxProfit = 0

        #make sure that the right pointer is always less than the length of the list
        for right in range(1, len(prices)):
            #if the price at left pointer is less than the price in right, find profit
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                #we then update MaxProfit if the new profit is greater than the MaxProf
                maxProfit = max(maxProfit, profit)
            else:
                #if the price on the left is greater than the right one, move the left pointer forward by 1
                left = right
                
        return maxProfit