class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_min = [prices[0]]
        min_price = prices[0]

        for i in range(1,len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            buy_min.append(min_price)
        return max(prices[i]-buy_min[i] for i in range(len(prices)))

                




        