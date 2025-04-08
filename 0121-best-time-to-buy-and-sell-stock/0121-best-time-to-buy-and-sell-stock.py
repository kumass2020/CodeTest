class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if len(prices) == 1:
        #     return 0

        # lst = [[prices[i], i] for i in range(len(prices))]
        # lst.sort(key=lambda x: x[0])
        
        # i = 0
        # j = len(prices)-1
        # while i < j:
        #     # print(i, j)
        #     if lst[i][1] < lst[j][1]:
        #         return lst[j][0] - lst[i][0]
        #     else:
        #         if lst[j-1][0] - lst[i][0] > lst[j][0] - lst[i+1][0]:
        #             j -= 1
        #         else:
        #             i += 1
        # return 0

        min_price = 10001
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if max_profit < profit:
                max_profit = profit

        return max_profit