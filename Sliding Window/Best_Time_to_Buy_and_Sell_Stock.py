class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        max_val = 0
        indexes = [0, 0]
        for s in range(len(prices)):
            if prices[s] - prices[b] > max_val:
                max_val = prices[s] - prices[b]
                indexes[0] = b
                indexes[1] = s
            if prices[b] > prices[s]:
                b = s
        return prices[indexes[1]] - prices[indexes[0]] 