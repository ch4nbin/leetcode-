class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # you want to find the lowest buy and the highest price after that
        # two pointer where you update buy (when you come across a lower
        # buy) and then the valure youre currently looking at to see if you
        # surpass the global max diff

        l = 0
        maxprof = 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            if prices[r] - prices[l] > maxprof:
                maxprof = prices[r] - prices[l]
        return maxprof

        