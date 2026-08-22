class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_val = prices[1]
        profit = 0
        min_val_index = 0
        for i in prices:
            if i < min_val:
                min_val = i
    
        min_val_index = prices.index(min_val)

        if min_val_index + 1 == len(prices):
            profit = 0
            return 0
        else:
            for i in range(prices[min_val_index + 1], len(prices)):
                if i - profit > profit:
                    profit = i - profit

        print(profit)

S1 = Solution()
# S1.maxProfit([7,6,4,3,1])

